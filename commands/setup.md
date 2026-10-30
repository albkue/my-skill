---
description: First-run onboarding - interview the user and generate their workflow profile with their own contexts and rules, so my-skill fits their situation
argument-hint: "[optional: 'redo' to rebuild an existing profile]"
---

# setup

1. Read `docs/workflow-profile.example.md` (the template) and, if present, `docs/workflow-profile.md`. If a real profile already exists and `$ARGUMENTS` is not `redo`, show it, say setup is only needed for a rebuild, and suggest `/my-skill:workflow-adapter` for incremental changes. Stop.
2. Interview the user, a few questions at a time, waiting for answers (use a selection tool when available):
   - Name and current roles (paid work, study, side projects).
   - For each role or project: one-line description, stack, who reviews/approves work, where it ships.
   - Which of these must never be mixed (separate employers, client data, graded coursework). Each becomes a context.
   - Safety rules per context: what needs confirmation first, what must never leave that context.
   - Top 3 priorities, ranked.
3. Propose a context id (short, lowercase, hyphenated) per distinct role/project. Show the full draft profile in the template's structure and ask for approval. Write nothing before approval.
4. On approval: write `docs/workflow-profile.md` (set `Last updated` to today), reset `docs/active-context.md` to `Current: unset`, and tell the user to run `/my-skill:today <id>`.
5. Remind the user that skills named after the original author's contexts (`backend-job`, `software-internship`, `internship-communication`, `car-part-retrieval`, `thesis-helper`) are examples; see `docs/CUSTOMIZATION.md` section 2 to repoint or delete them. Offer to run `/my-skill:skill-health-check` against the new profile.
