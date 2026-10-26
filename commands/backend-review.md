---
description: Run a senior-grade backend code review on a PR, diff, or file using the backend-code-review skill
argument-hint: "[what to review: pasted code, diff, PR description, or file paths]"
---

# backend-review

1. Read `skills/backend-code-review/SKILL.md` and follow it exactly.
2. Use `$ARGUMENTS` as the review target. If there is no actual code/diff to review yet, ask for it (full files preferred for controllers/services) plus the skill's Required inputs — do not review in a vacuum.
3. Produce the skill's Output format: Summary, Blocking issues, Important improvements, Optional suggestions, Security concerns, Test gaps, Recommended verdict.
4. If the change turns out to need implementation work rather than review, say which skill to use next (`backend-job` for the backend part-time job, `software-internship` for internship work — ask if context is unclear).
