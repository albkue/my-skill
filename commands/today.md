---
description: Set today's working context (any context defined in your workflow profile) so skills stop asking which one and apply that context's safety rules
argument-hint: "[a context id defined in workflow-profile.md]"
---

# today

1. Read `docs/active-context.md` and the "Contexts" section of `docs/workflow-profile.md`; the valid ids are its `###` headings.
2. If `$ARGUMENTS` is one of the valid ids, set `Current:` to it and `Set on:` to today's date (YYYY-MM-DD). Edit only those two lines.
3. If `$ARGUMENTS` is empty, show the current value and ask which valid id to set (use a selection tool if available).
4. If `$ARGUMENTS` is anything else, say it is not a defined context and list the valid ids (suggest `/my-skill:setup` to define new ones); change nothing.
5. Confirm in one line, then print that context's rules and any `Defer to` skills from its `###` block in the profile so they are visible for the session.
