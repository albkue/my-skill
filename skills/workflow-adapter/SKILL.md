---
name: workflow-adapter
description: Detect and reconcile drift between docs/workflow-profile.md and the user's actual current work. Use when the request mentions a role, project, stack, team, or priority the profile doesn't reflect, when the user says "my workflow changed", "update my workflow profile", "I'm moving to X", "I finished Y", or when two skills disagree about which context applies. Do NOT use to edit skill workflows or descriptions (that's continuous-improvement), to audit the whole inventory (that's skill-health-check), or to do the actual work task itself.
version: 1.0.0
author: Sothy Eng
---

# Workflow Adapter

## Purpose
Keep the profile — and therefore the whole plugin — truthful about the user's current reality. Work requests routinely mention facts that outdate the profile ("my internship ended", "I'm on a data job now", "we moved to Postgres-only"). This skill converts those facts into confirmed profile changes, so every other skill starts from the right context.

## When to use
- "My workflow changed" / "update my workflow profile".
- A request names a role, project, stack, team, or priority that the profile contradicts or lacks.
- Two skills argue over context because each reads the profile differently.
- A big life event class: new job, internship ended, project shipped/abandoned, new tech to learn, priorities re-ranked.

## When not to use
- Editing skill files / descriptions / workflows → `continuous-improvement`.
- Whole-inventory audit → `skill-health-check`.
- The work task itself → whatever task skill applies (this skill only updates the profile first, then gets out of the way).

## Context intake
- What changed, when, and is it effective now or dated (e.g., internship ends next month)?
- Is the change replacing something (move the old entry to Completed/paused) or adding?
- Read `docs/workflow-profile.md` before asking anything — many "changes" are already recorded.

## Workflow
1. Read `docs/workflow-profile.md`. If the request is already consistent with it, say so and stop.
2. Classify the drift: retired role/project · new role/project · stack change · team-convention change · priority re-rank · environment change.
3. Show the drift as a side-by-side table: profile says X ↔ request says Y.
4. Ask at most 2–3 clarifying questions for genuinely ambiguous parts (effective date, stack specifics, what to deprecate) — never re-ask what the request already states.
5. Propose the exact `docs/workflow-profile.md` diff: edits + dated entries moved to *Completed / paused workflows*.
6. After approval, apply the edit and update `Last updated:`.
7. If the drift implies skill-level consequences (e.g., a context skill now points at a retired role), hand off to `continuous-improvement` with a one-line rationale — do not edit SKILL.md files here.
8. Record the change in `docs/CHANGELOG.md` under the current version.

## Adaptation rules
- Role changes (job/internship ended): mark *Completed / paused* with date; if an equivalent new role exists, map personal context skills to it only via `continuous-improvement`.
- Stack changes: update only the stacks the user actually confirmed; skills' Adaptation rules absorb the rest.
- Minor drift (one tool, one convention): a one-line profile edit is fine; don't over-ceremonize.
- If the user's reason is temporary ("for this month"), record it in *Current priorities* rather than retiring anything.

## Inputs needed
- The statement of change (one sentence is enough).
- Optionally: effective date, replacing/retiring details, new team conventions.
- The current `docs/workflow-profile.md`.

## Output contract
1. **Drift table** — profile vs reality, classified.
2. **Clarifying questions asked** (if any) + answers.
3. **Proposed profile diff** — exact before/after.
4. **Applied change** — confirmation + `Last updated` bump.
5. **Knock-on effects** — skills affected, handed to `continuous-improvement` if warranted (never edited here).
6. **Changelog note** — entry added.

## Rules and constraints
- The profile is the output; SKILL.md files are never edited by this skill.
- Nothing about the user's identity is invented — placeholders like `<my-github-username>` only where applicable.
- No private data: team names, internal URLs, client names stay generic or out.
- Deletion from the profile always means *move to Completed/paused with a date*, never silent removal.

## Quality checklist
- [ ] Drift classified and shown side-by-side before any edit.
- [ ] Proposed diff shown and approved before applying.
- [ ] Profile `Last updated` date refreshed.
- [ ] Retired items moved to *Completed / paused*, with dates.
- [ ] Knock-on skill effects identified and correctly routed.
- [ ] CHANGELOG entry recorded.

## Lessons learned

Record improvements after real usage (maintained via `continuous-improvement`). Format:

- `<date>` — `<what happened>` → `<change made to this SKILL.md>`

(empty — entries appear after real usage)

## Examples
1. **Request:** "My internship ended; I'm applying for data jobs."
   **Behavior:** Drift table (profile lists intern role ↔ request says ended); propose moving *Software Developer intern* to Completed with date + updating *Current priorities* to rank job search first; after approval, hand `software-internship`/`internship-communication` redirect work to `continuous-improvement`; changelog.
2. **Request:** "We switched from Kafka to RabbitMQ at work, adapt."
   **Behavior:** Update *Main tech stacks* + *Team conventions* for the paid-work context; note which skills read stacks from the profile (backend-*) adapt automatically via Adaptation rules; ask whether any checklists should mention RabbitMQ; changelog.
