---
description: Show the my-skill menu and route the request to the right skill
argument-hint: "[request]"
---

# my-skill dispatcher

You are routing a request for Sothy Eng through the `my-skill` plugin. Follow these steps.

## Step 1 — Parse the request

If `$ARGUMENTS` is empty, go directly to Step 2. Otherwise treat the argument text as the user's request and go to Step 3.

## Step 2 — Show the menu and ask for context

Show this menu, then ask which context the user wants (use a question/selection tool if available; otherwise ask as a numbered list and wait for a reply):

1. **Backend part-time job** → route to `backend-job` (use `api-design`, `backend-debugging`, `backend-code-review`, `backend-testing`, or `backend-deployment` when the request clearly fits one of them).
2. **Software Developer internship** → route to `software-internship` (use `internship-communication` when the request is about messages, standups, or professional communication).
3. **Final-year car-part retrieval project** → route to `car-part-retrieval` (use `thesis-helper` when the request is about thesis writing, structure, or academic sections).
4. **Data engineering learning** → route to `data-engineering`.
5. **Interview preparation** → route to `interview-prep`.
6. **Learning roadmap** → route to `learning-roadmap`.

## Step 3 — Route the request

1. Decide which context the request belongs to using the table above.
2. **Critical routing rule:** `backend-job` is ONLY for the part-time Backend Developer job. `software-internship` is ONLY for the Software Developer internship. Never mix these two contexts.
3. If the request could belong to either the backend job or the internship and the user has not stated which, ask exactly:
   > "Is this for your backend part-time job or your software developer internship?"
   Wait for the answer before proceeding.
4. If the request fits thesis writing, interviews, roadmaps, references, or checklists, route accordingly (thesis-helper, interview-prep, learning-roadmap, or load the matching file from `references/`).
5. If still ambiguous after asking, ask one short clarifying question — do not guess.

## Step 4 — Execute the routed skill

Follow the routed skill's `SKILL.md` completely:

- Read the skill file at `skills/<routed-skill>/SKILL.md` before answering.
- Collect the skill's "Required inputs"; ask at most the minimum clarifying questions needed.
- Follow its "Workflow" steps.
- Produce exactly its "Output format".
- Enforce its "Rules and constraints" (secrets, production safety, scope boundaries).
- Reference the matching checklist in `references/` when producing checklists or review verdicts.

## Step 5 — Naming expectations

When answering, briefly state which skill/context you are using, e.g. "Using `backend-job` (backend part-time job context)". This keeps contexts visibly separated, especially for backend-job vs. software-internship.
