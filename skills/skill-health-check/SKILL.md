---
name: skill-health-check
description: Audit the my-skill plugin's own skill inventory - every skill's purpose, version, last-updated state, overlap, vague triggers, 0-10 quality scores, and missing workflows; recommends merge/split/rename/archive/delete actions plus at most 2-5 genuinely new skills, and always shows the proposal before creating anything. Use for "audit my skills", "are any skills outdated/duplicated/unused", "what should be merged or renamed", or a periodic plugin health check. Do NOT use to actually edit skills (that's continuous-improvement) or to handle work tasks.
version: 1.0.0
author: Sothy Eng
---

# Skill Health Check

## Purpose
A periodic read-only review of my-skill's inventory against Sothy's current profile: catch drift, overlap, stale wording, and structural gaps — and produce a ranked, human-approved action list.

## When to use
- "Audit my skills" / "check plugin health" / monthly check.
- "Are any skills outdated, duplicated, or unused?"
- Before/after a workflow-profile change, to see which skills match the new situation.
- Deciding whether a suspected gap justifies a new skill.

## When not to use
- Actually applying edits → `continuous-improvement`.
- Reviewing a *specific task's output* → `continuous-improvement`.
- Any work task → route to the task's own skill.

## Context intake
- Read `docs/workflow-profile.md` first — the health verdict is "skills vs profile", not generic quality.
- Any specific concern (a skill that triggered wrongly, one that never fires)?
- Scope: all skills, or a subset?

## Workflow
1. Read `docs/workflow-profile.md` and every `skills/*/SKILL.md` in the my-skill plugin.
2. Build the inventory table: skill | purpose (1 line) | version | last-updated | usage status (from lesson entries; "unknown" if none yet).
3. Overlap detection: pair up skills whose descriptions or "When to use" claim the same trigger zone; verify against each one's "When not to use" whether the boundary is real or blurred.
4. Structure audit per skill: frontmatter completeness, description specificity (would this description trigger correctly on its own?), workflow concreteness (numbered, bounded, no "be helpful" fluff), presence of Context intake / Adaptation rules / Quality checklist / Lessons learned.
5. Profile match: for each skill, is its target context still active in the profile? Retired contexts become candidates for repurpose/redirect, not automatic deletion.
6. **Quality score (0–10 per skill)**, four sub-criteria worth 2.5 each:
   - *Description specificity (2.5)* — concrete trigger vocabulary + explicit non-triggers; vague wording loses points.
   - *Workflow measurability (2.5)* — numbered steps with exits/outputs per step; "be helpful" filler loses points.
   - *Contract testability (2.5)* — output contract falsifiable against a delivered response; quality checklist items falsifiable.
   - *Adaptation breadth (2.5)* — Adaptation rules genuinely cover >1 stack/team/project without hard-coding a person or job.
   Report score trend when prior entries exist (lessons-learned/history); a drop >1 point since last check is itself a finding.
7. Produce recommendations, each labeled and reasoned: `merge`, `split`, `rename`, `archive`, `delete`, `description fix`, `keep as is`. Deletions always require explicit confirmation.
8. Propose at most **2–5 new skills**, only for repeated real gaps — name, trigger description, why the workflow repeats (evidence from lessons-learned or Sothy's report). Present as proposals, never created automatically.
9. End by asking which actions to apply; applying anything hands off to `continuous-improvement`.

## Adaptation rules
- Nothing here assumes the current job/thesis; "health" is judged against the profile as it stands.
- If the profile itself is stale, stale-profile issues outrank wording nits — fix context intake ordering first.
- Weight recent usage evidence (lessons entries) over speculation; "unused" requires profile evidence, not guesses.

## Inputs needed
- No files from Sothy normally; optionally his recent task notes/feedback.
- Green light for any acting beyond reporting (never auto-applied).

## Output contract
- **Inventory table** — skill | purpose | version | last-updated | usage status | **quality score (0–10)**.
- **Score breakdown** — the four sub-criteria per skill with where points were lost, so scores are actionable, not vibes.
- **Findings** — overlap pairs, vague triggers, missing structure, profile mismatches; each with evidence.
- **Ranked recommendations** — labeled merge/split/rename/archive/delete/fix, smallest-first order.
- **Proposed new skills** — max 5, draft descriptions only.
- **Next step** — which actions (if any) Sothy wants applied; `continuous-improvement` does the edits.

## Quality checklist
- [ ] Every skill row includes a last-updated date and purpose line.
- [ ] Every finding has concrete evidence (quoted text, profile mismatch).
- [ ] Recommendations are each actionable in one edit session.
- [ ] Nothing was created, modified, or deleted during the check itself.
- [ ] New-skill proposals have a repeated-gap justification, not vibes.

## Rules and constraints
- Strictly read-only: report, never mutate (creating even a draft file is a mutation — output drafts in chat instead).
- Never invent usage statistics; only evidence from lessons-learned/profile/Sothy.
- Delete/archive recommendations must be justified and require confirmation — treat existing skills as Sothy's work, protected by default.
- No gratuitous reformatting during this check; cosmetic churn is itself a health issue — recommend "keep as is" when edits don't earn their cost.

## Lessons learned
Format: `<date>` — `<what happened>` → `<change made>`. (empty)

## Examples
1. **Request:** "Monthly health check."
   **Behavior:** Read profile + all 15+ SKILL.md files; inventory table; note overlap pair X/Y with quoted trigger zones; rank: (1) description fix for skill Z, (2) merge candidates, (3) proposed new skill for repeated debug-log analysis; end asking what to apply.
2. **Request:** "Is `api-design` still pulling its weight?"
   **Behavior:** Check its description vs neighbors, its lessons entries, profile activity; verdict with evidence — e.g. "keep as is; it's the contract-owner in product-to-production" — plus any wording fix, shown as a before/after.
