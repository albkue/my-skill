# Contributing to my_skill

Thank you for improving it. Read this and `docs/CUSTOMIZATION.md` before writing anything — the plugin's longevity depends on skills staying focused and generic.

## New skill vs. improve an existing one

**Improve an existing skill** (almost always the right move) when:

- The same skill's workflow can absorb the case via its **Adaptation rules**.
- A step, input, checklist bullet, or negative example is missing.
- Routing missed because the **description** lacked a phrase — fix the description.

**Create a new skill** only when there is a **repeated real gap**: the same distinct workflow (not just content) came up 3+ times and belongs to no existing skill's purpose. If two skills would overlap, split their trigger zones explicitly ("When not to use" on both) instead of blurring them.

## Required folder structure

```
skills/<skill-name>/SKILL.md      # exactly one file per skill folder

Start from the scaffold: copy `templates/SKILL-template.md` (it pre-fills all twelve
sections in order, with the profile-read step in the Workflow).
```

Optionally a thin dispatcher in `commands/<skill-name>.md` if the skill deserves a manual entry point (frontmatter: `description`, optional `argument-hint`; the body routes to the skill file — do not duplicate its workflow).

## Required YAML frontmatter

```yaml
---
name: my-skill            # lowercase, hyphenated, unique, matches the folder name
description: >            # the routing surface — most important field
  One or two sentences: what it does, concrete trigger conditions, and
  a "Do NOT use" boundary routing the nearest conflicting skill.
version: 1.0.0
author: Your Name
---
```

## Required sections

In this order, inside `# <Skill Title>`:

1. `## Purpose` — the problem it solves, one or two sentences.
2. `## When to use` — concrete triggers ("Kafka consumer lag", "design a new endpoint").
3. `## When not to use` — boundaries pointing to the neighboring skills by name.
4. `## Context intake` — what to detect or ask first (context: job/thesis/personal/learning; desired output type). Workflow step 1 must read `docs/workflow-profile.md`.
5. `## Workflow` — numbered, ordered, from intake to delivered output.
6. `## Adaptation rules` — how behavior shifts for different stacks, teams, project types. This is what keeps the skill reusable.
7. `## Inputs needed` — files/facts required from the user.
8. `## Output contract` — the exact deliverable shape.
9. `## Rules and constraints` — hard guardrails (no fabrication, no secrets, etc.).
10. `## Quality checklist` — `- [ ]` items that must be true before done.
11. `## Lessons learned` — seeded empty, filled by `continuous-improvement` after real usage.
12. `## Examples` — 1–2 short worked request → behavior examples.

## Naming and description rules

- **Name:** lowercase, hyphenated (`backend-code-review`), unique across the plugin, matches folder name, no underscores.
- **Description:** specific enough to trigger on its own; concrete trigger vocabulary; explicit non-triggers. Ban vague wording: "helps with development", "useful for coding", "improves productivity" are unacceptable triggers.

## Review checklist before submitting

- [ ] `name` is unique, lowercase, hyphenated, matches the folder.
- [ ] Frontmatter parses (two `---` fences; stayed valid YAML).
- [ ] All twelve required sections present, in order.
- [ ] Description has concrete triggers and a "do NOT use" boundary; no vague wording.
- [ ] Workflow is numbered and reads the workflow profile first.
- [ ] Adaptation rules present — no stack/job hard-coding (no company names, internal URLs, client data).
- [ ] Quality checklist is checkable (each item is falsifiable).
- [ ] `python scripts/validate.py` passes, and the skill has 3 "should" + 2 "should_not" prompts in `evals/triggers.json`.

## Test locally

```bash
cd my-skill
claude --plugin-dir .
```

In that session: ① invoke `/my-skill:<your-skill>` (or the natural trigger) — it activates; ② try a near-miss request (meant for a neighbor skill) — it routes *away*; ③ check the output matches your Output contract; ④ if you added a command, `/my-skill:<command-name>` resolves.

## Update README.md and docs/CHANGELOG.md

- **README:** add the skill to the catalog table alphabetically; if it's a workflow jump, add one line under *What problems it solves*.
- **`docs/CHANGELOG.md`:** newest entry at the top under the version your change ships in: `- New skill \`<name>\`: <one-line purpose>.` Changing existing skills goes under *Changed*; deletions under *Removed*; route/namespace changes under *Breaking changes* + *Migration notes*.

## Submit a pull request

1. Fork the repository, clone it, and create a feature branch: `git checkout -b add/<skill-name>` (or `fix/<topic>`).
2. Make the change; keep it small and focused — one skill or one skill's improvement per PR.
3. Test locally (`cd my-skill && claude --plugin-dir .`) and run the checklist above.
4. Open the PR using [`.github/PULL_REQUEST_TEMPLATE.md`](.github/PULL_REQUEST_TEMPLATE.md) with this checklist:

- [ ] `plugin.json` is valid
- [ ] `SKILL.md` has valid YAML frontmatter
- [ ] Skill name is unique
- [ ] Skill description is specific
- [ ] README is updated
- [ ] CHANGELOG is updated
- [ ] Plugin loads locally
- [ ] No private or confidential information is included

5. **Before opening the PR**, run `skill-health-check` and resolve any findings it raises about your new/changed skills.
