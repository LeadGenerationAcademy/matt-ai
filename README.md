# Matt AI

An AI assistant built on Matthew Larsen's Lead Generation Academy. It answers the way Matt would, from his
courses, weekly call recordings, templates, and calculators. Runs on your own Claude account, so there is
nothing to host and nothing to pay for beyond your own Claude plan.

## Install

### Step 1: Download Matt AI

**[Click here to download matt-ai.zip](https://github.com/LeadGenerationAcademy/matt-ai/releases/latest/download/matt-ai.zip)**

This link always gives you the newest version. You can also find it under **Releases** on the right side of
this page: click **Matt AI (latest)**, then **matt-ai.zip**.

- Do **not** use the green **Code** button. That gives you the wrong file.
- Do **not** unzip it. Claude needs the whole `.zip` file as it is.
- On a Mac, Safari sometimes unzips downloads by itself and you end up with a `matt-ai` folder. Ignore the
  folder and use the file that ends in **.zip**.

### Step 2: Turn on code execution in Claude (one time only)

1. Open [claude.ai](https://claude.ai) or the Claude desktop app.
2. Click your **name** at the bottom of the left sidebar.
3. Click **Settings**.
4. Click **Capabilities**.
5. Make sure **Code execution and file creation** is turned on. Matt AI needs it to read its files and run
   the calculators.

### Step 3: Upload Matt AI to Claude

1. Still in **Settings**, click **Skills** (under Customize).
2. Click the **+ Add** button at the top right.
3. Click **Upload skill**.
4. Drag **matt-ai.zip** into the box, or click the box and choose **matt-ai.zip** from your Downloads folder.
   Choose the whole `.zip` file, not a folder.
5. Click **Upload** and wait for the security scan to finish.
6. Make sure the switch next to **matt-ai** is turned on (blue).

### Step 4: Use it

1. Start a **new chat** in Claude.
2. Type **/matt-ai** followed by your question, or just ask your question. Claude turns Matt AI on by itself
   when your question is about your business.

### Updating to a new version

Matt AI gets new material regularly. To get the newest version:

1. Download the zip again from the link in Step 1.
2. Go to **Settings**, then **Skills**, and click **matt-ai**.
3. Click the **three dots** at the top right, then **Replace**.
4. Choose the new **matt-ai.zip** and click **Upload**.

### Claude Code, Codex, Cursor and other agents

```
npx skills add LeadGenerationAcademy/matt-ai
```

To update later:

```
npx skills check
npx skills update
```

## Use it

Describe your business and ask what Matt would do. Paste your copy, your numbers, or your funnel link.
It will ask for anything it needs, run Matt's calculators on your numbers, and point you to the exact
module in Skool for every recommendation.

Try: "Here is my offer and my last 30 days of funnel numbers. What is the biggest constraint?"

## What is inside

- `skills/matt-ai/SKILL.md`: how Matt diagnoses a business, his targets, benchmarks, and what he will not recommend.
- `skills/matt-ai/references/`: every course module, one file each, with video transcripts and Skool links.
- `skills/matt-ai/assets/templates/`: Matt's templates, converted so the AI can fill them in with you.
- `skills/matt-ai/scripts/`: the Unit Economics Model, Reverse Engineering, and Core Metrics calculators.
- `tools/build_claudeai_zip.py`: packs the skill into the under-200-file zip that Claude.ai accepts. The Action runs it on every push.

## Updates

Lessons change. Every change is listed in `CHANGELOG.md`. Claude.ai users follow "Updating to a new
version" above; everyone else runs `npx skills update`.
