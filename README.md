# Matt AI

An AI assistant built on Matthew Larsen's Lead Generation Academy. It answers the way Matt would, from his
courses, weekly call recordings, templates, and calculators. Runs on your own Claude account, so there is
nothing to host and nothing to pay for beyond your own Claude plan.

## Install

### Claude.ai (web or desktop app)

1. Download `matt-ai.zip` from the latest release on the right side of this page.
2. In Claude, open Customize, then Skills.
3. Click the plus button, then Create skill, then Upload a skill, and choose the zip.
4. Turn the skill on. It also appears in Claude Code if you are signed in with the same account.

### Claude Code, Codex, Cursor and other agents

```
npx skills add OWNER/matt-ai
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

## Updates

Lessons change. Every change is listed in `CHANGELOG.md`. Claude.ai users download the new zip from
Releases; everyone else runs `npx skills update`.
