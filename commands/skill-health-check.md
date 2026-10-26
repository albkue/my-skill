---
description: Audit my-skill's own skill inventory (freshness, overlap, vague triggers, profile match) and get ranked merge/split/rename/proposal recommendations - read-only
argument-hint: "[scope: all skills | a skill name | a concern to check]"
---

# skill-health-check

1. Read `skills/skill-health-check/SKILL.md` and follow it exactly.
2. Read `docs/workflow-profile.md` first — health is judged as "skills vs profile".
3. If `$ARGUMENTS` names a specific skill or concern, focus there; otherwise sweep all skills.
4. Deliver the skill's Output format: inventory table, findings with evidence, ranked recommendations (merge/split/rename/archive/delete/description fix), at most 2–5 new-skill proposals.
5. Strictly read-only during the check — nothing is created or modified. Ask which recommendations to apply, and hand any approved edits to `continuous-improvement`.
