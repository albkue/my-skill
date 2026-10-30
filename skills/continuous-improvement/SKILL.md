---
name: continuous-improvement
description: Improve my_skill after real tasks by reviewing feedback, identifying missing workflow steps, and updating the relevant SKILL.md files. Use when Sothy asks to review how a task was handled ("review how my_skill handled my last task"), improve a specific skill from feedback ("improve backend-review based on this"), update skills after a workflow change ("my workflow changed; update the relevant skills"), find weak/overlapping/unused skills, add a skill for a repeated workflow, or produce a periodic plugin improvement report. Do NOT use it for the underlying work tasks themselves - route those to their skills; this skill only edits and maintains the plugin.
version: 1.0.0
author: Sothy Eng
---

# Continuous Improvement

## Purpose
Keep my-skill aligned with Sothy's actual workflow as it evolves: turn real usage (what worked, what was missing, what caused rework) into concrete, small SKILL.md improvements — without deleting his existing skills or making skills broader.

## When to use
- "Review how my_skill handled my last task" / post-task retro.
- A skill gave a bad off-target response; feedback on a specific skill.
- "My workflow changed; update the relevant skills."
- "Find weak, overlapping, or unused skills."
- "Add a new skill for this repeated workflow" — after the pattern repeated 3+ times.
- Monthly improvement report pass.

## When not to use
- Doing the work itself (backend service, API, thesis, pipeline) → route to that task's skill.
- Pure inventory health audit with no change in mind → `skill-health-check` (lighter, read-first).

## Context intake
- Which task/skill is the target — or "sweep everything"?
- Was there a real task + final output to compare against? (most valuable evidence)
- What specifically felt wrong: wrong routing, missing step, wrong depth, wrong format, wrong assumptions?
- Does `docs/workflow-profile.md` (and `docs/active-context.md`) still match reality? (outdated profile causes most mis-adaptation)

## Workflow
1. Read `docs/workflow-profile.md`; flag staleness (>3 months or contradiction) and resolve it first. If `docs/usage-log.md` exists (written by the PostToolUse hook), read it too: skills never fired are candidates for archive, skills fired often with lessons are candidates for tightening.
2. Identify the target: last-task review / named skill / profile drift / new repeated gap / periodic report.
3. Gather evidence: original request text, the final output, and any rework Sothy did afterward. Read the target `SKILL.md` end to end.
4. Diagnose against evidence:
   - Wrong skill triggered → fix the **description** (routing is description-driven).
   - Repeated clarifying questions → add to **Context intake** / **Inputs needed**.
   - Missing or extra steps → edit **Workflow** (keep it ordered and small).
   - Redo/formatting complaints → tighten **Output contract**.
   - Caught risks too late → add to **Quality checklist** or **Rules and constraints**.
5. Ask Sothy 2–4 short feedback questions (one-line answers): "What's the one thing it should have done differently?" etc.
6. Convert to concrete edits. **Show a before/after diff or summary before applying anything that rewrites, renames, splits, or deletes.** Small additive edits (a line in Context intake, one bullet in a checklist) may be applied directly but must be reported.
7. Apply approved edits: bump the skill's `version`, append the change to `docs/CHANGELOG.md`, add a dated line to `docs/lessons-learned.md` (and to the skill's own Lessons learned section when it has real content).
8. Run the plugin validation (plugin.json valid; every skill has SKILL.md + valid frontmatter; names/descriptions unique; references resolve) and report results.
9. For a periodic report: summarize usage themes, gaps found, edit mode applied, skills untouched but aging, and profile changes needed.

## Adaptation rules
- Feedback about *content* edits that skill's existing sections; feedback about *routing* edits the description only.
- A repeated 3+ time workflow can be proposed as a new skill — as a **proposal** (name, trigger, one-paragraph draft), never auto-created.
- If a role/project retired (per profile), propose shifting its skills to the closest current context (e.g., internship → first dev job) rather than deleting.
- Cross-skill conflicts: route by updating the two descriptions' "When not to use" lines.

## Inputs needed
- Task request + final output (pasted or referenced) when reviewing a task.
- Concrete feedback lines (complaints count).
- Any changed facts for the profile (new role, project end, new stack, tool change).

## Output contract
- **Target + evidence** — what was reviewed and against what.
- **Diagnosis** — short bullet list: what worked / what was missing / what caused rework.
- **Feedback questions asked** (+ answers if given).
- **Proposed edits** — per file: before/after diff or summary; only applied ones after approval for major changes.
- **Applied changes** — file list + version bumps.
- **Validation results** — pass/fail per check.

## Quality checklist
- [ ] Every diagnosis point traced to actual evidence, not vibes.
- [ ] Before/after shown for any major change; approval recorded.
- [ ] Skills stay single-responsibility — no skill grew broader.
- [ ] `docs/CHANGELOG.md` and `docs/lessons-learned.md` updated.
- [ ] Full validation passes; no broken references.

## Rules and constraints
- Never delete or rename a skill without explaining why and getting explicit confirmation.
- Never create a skill automatically — proposals only, approved one file at a time.
- Do not broaden skills to "cover" a found gap; split or route instead.
- Keep examples grounded in real usage; redact secrets/internal names from any recorded evidence.
- Record changes only in the documented files (`SKILL.md` files, `docs/`, README); no side-channel edits.

## Lessons learned
Maintained across sessions in `docs/lessons-learned.md`. Format:
- `<date>` — `<skill>` — `<what happened>` → `<change made>`.

(empty — entries appear after real usage)

## Examples
1. **Request:** "my-skill stuck in an internship-routing loop when I asked about Kafka config at the job."
   **Behavior:** Read the transcript evidence; diagnosis = description gap; propose a tightened `backend-job` description line (before/after), bump version, changelog entry, validation.
2. **Request:** "My internship ended; I'm moving to a data engineering role."
   **Behavior:** Update `docs/workflow-profile.md` (roles, priorities, move internship to completed); propose redirect edits for `software-internship` and `internship-communication` (repurpose to general work communication), show diffs, wait for approval, then apply + changelog + validation.
