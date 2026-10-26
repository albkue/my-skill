---
description: Update the workflow profile when Sothy's roles, projects, stacks, or priorities changed, and resolve context drift
argument-hint: "[what changed: e.g. 'my internship ended', 'we moved to Postgres-only', 'new priorities']"
---

# workflow-adapter

1. Read `skills/workflow-adapter/SKILL.md` and follow it exactly.
2. Use `$ARGUMENTS` as the statement of change. If empty, ask one question: "What changed — a role, project, stack, or priority?"
3. Show the drift table and the proposed `docs/workflow-profile.md` diff; apply only after approval.
4. Hand any skill-level knock-on effects to `continuous-improvement`; record the change in `docs/CHANGELOG.md`.
