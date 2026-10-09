"""Build the Claude.ai upload zip from the full skill folder.

Claude.ai accepts at most 200 files in a skill zip. The full skill has 1,300+ files (one per module,
one per template sheet). This packs the same content into far fewer files without changing the folder
layout SKILL.md relies on:

  references/<system>/<course>/part1.md, part2.md ...   modules of a course, packed by size
  references/INDEX.md                                   every module, the file it is in, and its line
  assets/templates/<slug>/<slug>.md                     README + content + sheets + formulas in one file
  assets/templates/INDEX.md, scripts/*, SKILL.md        unchanged

Why the file count can't run away (the daily scraper adds content forever):
- Ordinary courses are packed up to WORDS_PER_FILE words per file.
- Courses that grow every day have a fixed FILE BUDGET instead (call recordings, member Q&A). When they
  grow, their files get bigger, not more numerous.
- INDEX.md gives the line each module starts on, so Claude jumps straight to it no matter how big the
  file is.
- Last safety net: if the total is still over the limit, everything is repacked with bigger files until it
  fits. The build never fails on file count.

Usage: python3 build_claudeai_zip.py <skill_dir> <out_dir>
Writes <out_dir>/matt-ai/ and <out_dir>/matt-ai.zip (zipped from the parent, as Claude.ai expects).
"""
import os, re, sys, shutil, subprocess, json, math

SRC, OUT = sys.argv[1], sys.argv[2]
NAME = os.path.basename(SRC.rstrip("/"))
DST = os.path.join(OUT, NAME)
FILE_LIMIT = 200       # Claude.ai's limit
TARGET = 190           # stay a little under it
WORDS_PER_FILE = 25000 # ordinary courses: one module larger than this gets its own file
FILE_BUDGETS = {       # courses that grow every day: at most this many files, however big they get
    "00-core/07-matt-s-call-recordings": 30,
    "00-core/58-member-questions-and-answers": 12,
}


def read(p):
    return open(p, encoding="utf-8").read()


def write(p, text):
    os.makedirs(os.path.dirname(p), exist_ok=True)
    open(p, "w", encoding="utf-8").write(text)


def pack(modules, limit):
    """Group (name, text, words) in order into parts of at most `limit` words."""
    parts, cur, cur_words = [], [], 0
    for m in modules:
        if cur and cur_words + m[2] > limit:
            parts.append(cur)
            cur, cur_words = [], 0
        cur.append(m)
        cur_words += m[2]
    if cur:
        parts.append(cur)
    return parts


def pack_with_budget(modules, limit, budget):
    """Like pack(), but never more than `budget` parts: the limit grows until it fits."""
    total = sum(m[2] for m in modules)
    limit = max(limit, math.ceil(total / budget))
    parts = pack(modules, limit)
    while len(parts) > budget:
        limit = math.ceil(limit * 1.1)
        parts = pack(modules, limit)
    return parts


def build(scale):
    if os.path.exists(DST):
        shutil.rmtree(DST)
    os.makedirs(DST)

    # ---------- SKILL.md (path tweaks so every reference points at something that exists here) ----------
    skill = read(os.path.join(SRC, "SKILL.md"))
    skill = skill.replace("references/03-marketing-system/45-all-setup-assets/01-master-list.md",
                          "references/03-marketing-system/45-all-setup-assets/")
    skill = skill.replace(
        "Open `references/INDEX.md`, then the course's `INDEX.md`, then only the module files you need.",
        "Open `references/INDEX.md`. It lists every module, the file it is in, and the line it starts on. "
        "Open only that file, starting at that line. Some files are long: read the part you need, not the "
        "whole file.")
    write(os.path.join(DST, "SKILL.md"), skill)

    # ---------- references ----------
    manifest = json.load(open(os.path.join(SRC, "manifest.json")))
    ref_src = os.path.join(SRC, "references")
    index = ["# Course Index", "",
             "Every module in every course, the file it is in, and the line it starts on. Open the file at that "
             "line and read only that module.", ""]
    shared = sorted(f for f in os.listdir(os.path.join(ref_src, "00-core")) if f.endswith(".md"))
    os.makedirs(os.path.join(DST, "references", "00-core"), exist_ok=True)
    for f in shared:
        shutil.copy(os.path.join(ref_src, "00-core", f), os.path.join(DST, "references", "00-core", f))
        label = "Voice guide, read before every answer" if f == "voice.md" else "Shared module (same in every course)"
        index.append(f"{label}: 00-core/{f}")
    index.append("")

    current_system = None
    for c in manifest:
        if c["system"] != current_system:
            current_system = c["system"]
            index += [f"## {current_system}", ""]
        cdir = os.path.join(ref_src, c["dir"])
        files = sorted(f for f in os.listdir(cdir) if f.endswith(".md") and f != "INDEX.md")
        course_index_lines = [l for l in read(os.path.join(cdir, "INDEX.md")).split("\n") if l.startswith("- ")]
        modules = []
        for f in files:
            text = read(os.path.join(cdir, f))
            modules.append((f, text, len(text.split())))
        limit = WORDS_PER_FILE * scale
        if c["dir"] in FILE_BUDGETS:
            parts = pack_with_budget(modules, limit, max(1, FILE_BUDGETS[c["dir"]] // scale))
        else:
            parts = pack(modules, limit)
        n = len(parts)
        index.append(f"### {c['course']} ({len(files)} modules, {n} file{'s' if n != 1 else ''}) `{c['dir']}/`")
        if c["course_link"]:
            index.append(f"Skool course link: {c['course_link']}")
        for i, part in enumerate(parts, 1):
            pname = f"part{i}.md"
            titles = []
            for f, _, _ in part:
                line = next((l for l in course_index_lines if l.startswith(f"- {f}:")), f"- {f}")
                titles.append(line.replace(f"- {f}: ", "", 1))
            body = [f"# {c['course']} (file {i} of {n})", "", f"System: {c['system']}"]
            if c["course_link"]:
                body.append(f"Skool course link: {c['course_link']}")
            body += ["", "Modules in this file:"]
            body += [f"- {t}" for t in titles]
            body.append("")
            lines_so_far = len("\n".join(body).split("\n"))
            for (f, text, _), title in zip(part, titles):
                body += ["", "=" * 70, ""]
                lines_so_far += 3
                start = lines_so_far + 1       # 1-based line where this module's text begins
                index.append(f"- {pname} (line {start}): {title}")
                chunk = text.rstrip()
                body += [chunk, ""]
                lines_so_far += len(chunk.split("\n")) + 1
            write(os.path.join(DST, "references", c["dir"], pname), "\n".join(body))
        if not files:
            index.append("- (no modules yet)")
        index.append("")
    write(os.path.join(DST, "references", "INDEX.md"), "\n".join(index))

    # ---------- templates: one file per template ----------
    t_src = os.path.join(SRC, "assets", "templates")
    os.makedirs(os.path.join(DST, "assets", "templates"), exist_ok=True)
    shutil.copy(os.path.join(t_src, "INDEX.md"), os.path.join(DST, "assets", "templates", "INDEX.md"))
    for slug in sorted(os.listdir(t_src)):
        d = os.path.join(t_src, slug)
        if not os.path.isdir(d):
            continue
        out = [read(os.path.join(d, "README.md")).rstrip(), ""]
        for f in sorted(os.listdir(d)):
            p = os.path.join(d, f)
            if f == "README.md":
                continue
            if f.endswith(".md"):
                out += ["", "-" * 70, "", read(p).rstrip(), ""]
            elif f.endswith(".csv"):
                out += ["", f"## Sheet: {f[:-4]} (CSV)", "", "```csv", read(p).rstrip(), "```", ""]
        write(os.path.join(DST, "assets", "templates", slug, f"{slug}.md"), "\n".join(out))

    # ---------- scripts ----------
    os.makedirs(os.path.join(DST, "scripts"), exist_ok=True)
    for f in os.listdir(os.path.join(SRC, "scripts")):
        if f.endswith(".py"):
            shutil.copy(os.path.join(SRC, "scripts", f), os.path.join(DST, "scripts", f))

    return sum(len(fs) for _, _, fs in os.walk(DST))


scale = 1
count = build(scale)
while count > TARGET and scale < 64:
    print(f"{count} files is too close to the {FILE_LIMIT} limit. Repacking with bigger files.")
    scale *= 2
    count = build(scale)

# ---------- zip from the parent folder ----------
zip_path = os.path.join(OUT, f"{NAME}.zip")
if os.path.exists(zip_path):
    os.remove(zip_path)
subprocess.run(["zip", "-qr", f"{NAME}.zip", NAME], cwd=OUT, check=True)
size = os.path.getsize(zip_path) // 1024
print(f"{count} files in {DST} (limit {FILE_LIMIT}); {zip_path} is {size} KB")
if count > FILE_LIMIT:
    print("TOO MANY FILES for Claude.ai (limit 200)")
    sys.exit(1)
