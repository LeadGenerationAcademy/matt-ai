"""Build the Claude.ai upload zip from the full skill folder.

Claude.ai accepts at most 200 files in a skill zip. The full skill has 1,300+ files (one per module,
one per template sheet). This packs the same content into about 140 files without changing the
folder layout SKILL.md relies on:

  references/<system>/<course>/part1.md, part2.md ...   modules of a course, grouped by size
  references/INDEX.md                                   every module, with the file it is in
  assets/templates/<slug>/<slug>.md                     README + content + sheets + formulas in one file
  assets/templates/INDEX.md, scripts/*, SKILL.md        unchanged

Usage: python3 build_claudeai_zip.py <skill_dir> <out_dir>
Writes <out_dir>/matt-ai/ and <out_dir>/matt-ai.zip (zipped from the parent, as Claude.ai expects).
"""
import os, re, sys, shutil, subprocess, json

SRC, OUT = sys.argv[1], sys.argv[2]
NAME = os.path.basename(SRC.rstrip("/"))
DST = os.path.join(OUT, NAME)
MAX_WORDS = 9000     # per part file; one module larger than this gets its own part

if os.path.exists(DST):
    shutil.rmtree(DST)
os.makedirs(DST)


def read(p):
    return open(p, encoding="utf-8").read()


def write(p, text):
    os.makedirs(os.path.dirname(p), exist_ok=True)
    open(p, "w", encoding="utf-8").write(text)


# ---------- SKILL.md (two path tweaks so every reference points at something that exists here) ----------
skill = read(os.path.join(SRC, "SKILL.md"))
skill = skill.replace("references/03-marketing-system/45-all-setup-assets/01-master-list.md",
                      "references/03-marketing-system/45-all-setup-assets/")
skill = skill.replace("Open `references/INDEX.md`, then the course's `INDEX.md`, then only the module files you need.",
                      "Open `references/INDEX.md`. It lists every module and the file it is in. Open only that file.")
write(os.path.join(DST, "SKILL.md"), skill)

# ---------- references ----------
manifest = json.load(open(os.path.join(SRC, "manifest.json")))
ref_src = os.path.join(SRC, "references")
index = ["# Course Index", "",
         "Every module in every course, and the file it is in. Open the file, then find the module heading.", ""]
shared = [f for f in os.listdir(os.path.join(ref_src, "00-core")) if f.endswith(".md")]
os.makedirs(os.path.join(DST, "references", "00-core"), exist_ok=True)
for f in shared:
    shutil.copy(os.path.join(ref_src, "00-core", f), os.path.join(DST, "references", "00-core", f))
    index.append(f"Shared module (same in every course): 00-core/{f}")
index.append("")

current_system = None
for c in manifest:
    if c["system"] != current_system:
        current_system = c["system"]
        index += [f"## {current_system}", ""]
    cdir = os.path.join(ref_src, c["dir"])
    files = sorted(f for f in os.listdir(cdir) if f.endswith(".md") and f != "INDEX.md")
    course_index_lines = [l for l in read(os.path.join(cdir, "INDEX.md")).split("\n") if l.startswith("- ")]
    # group module files into parts
    parts, cur, cur_words = [], [], 0
    for f in files:
        text = read(os.path.join(cdir, f))
        w = len(text.split())
        if cur and cur_words + w > MAX_WORDS:
            parts.append(cur); cur, cur_words = [], 0
        cur.append((f, text)); cur_words += w
    if cur:
        parts.append(cur)
    n = len(parts)
    index.append(f"### {c['course']} ({len(files)} modules, {n} file{'s' if n != 1 else ''}) `{c['dir']}/`")
    if c["course_link"]:
        index.append(f"Skool course link: {c['course_link']}")
    for i, part in enumerate(parts, 1):
        pname = f"part{i}.md"
        body = [f"# {c['course']} (file {i} of {n})", "", f"System: {c['system']}"]
        if c["course_link"]:
            body.append(f"Skool course link: {c['course_link']}")
        body += ["", "Modules in this file:"]
        for f, _ in part:
            title = next((l for l in course_index_lines if l.startswith(f"- {f}:")), f"- {f}")
            body.append(title.replace(f"- {f}: ", "- ", 1))
            index.append(f"- {pname}: " + title.replace(f"- {f}: ", "", 1))
        body.append("")
        for f, text in part:
            body += ["", "=" * 70, "", text.rstrip(), ""]
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

# ---------- zip from the parent folder ----------
zip_path = os.path.join(OUT, f"{NAME}.zip")
if os.path.exists(zip_path):
    os.remove(zip_path)
subprocess.run(["zip", "-qr", f"{NAME}.zip", NAME], cwd=OUT, check=True)
count = sum(len(fs) for _, _, fs in os.walk(DST))
size = os.path.getsize(zip_path) // 1024
print(f"{count} files in {DST}; {zip_path} is {size} KB")
if count > 200:
    print("TOO MANY FILES for Claude.ai (limit 200)"); sys.exit(1)
