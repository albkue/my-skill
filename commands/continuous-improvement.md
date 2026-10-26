---
description: Feed real task feedback back into my-skill - improve skills, update the workflow profile, maintain changelog and lessons learned
argument-hint: "[what to review/improve: last task, a skill name, 'my workflow changed', 'monthly report']"
---

# continuous-improvement

1. Read `skills/continuous-improvement/SKILL.md` and follow it exactly.
2. Use `$ARGUMENTS` as the target:
   - a task description / feedback → post-task retro, evidence-first
   - a skill name → improve that skill from the given feedback (ask for it if none given)
   - "my workflow changed" → update `docs/workflow-profile.md` first, then propose matching skill edits
   - "monthly report" → periodic improvement report pass
3. If `$ARGUMENTS` is empty, ask 2–3 short questions (which task felt off, what should it have done differently) before diagnosing.
4. Show a before/after diff or summary before applying any major SKILL.md change (rewrite/rename/split/delete). Small additive edits may be applied directly but must be reported.
5. After edits: bump the skill version, update `docs/CHANGELOG.md` and `docs/lessons-learned.md`, re-run the plugin validation, and report results.
