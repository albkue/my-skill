---
name: documentation
description: Write and maintain technical documentation grounded in real code - READMEs, setup guides, architecture overviews, API docs, environment-variable references, runbooks, ADRs, contribution guides, and changelogs. Use when the user asks to document a service, project, or feature, create a README, write an architecture decision record, or says documentation is missing or out of date. Do NOT use for academic thesis writing (thesis-helper), internship messages (internship-communication), or API contract design itself (api-design - document the decided contract here).
version: 1.0.0
author: Sothy Eng
---

# Documentation

## Purpose
Produce documentation a new teammate (or Sothy in three months) can act on: accurate to the actual code, structured for the reader's task, and honest about what is out of date.

## When to use
- Creating or refreshing a README, setup guide, or onboarding doc for any project (backend job, internship repo, car-part retrieval system, data pipelines).
- Writing architecture overviews, ADRs, API reference docs, environment-variable tables, runbooks, data dictionaries, or changelogs.
- "Document this service", "our docs are stale", "prepare handover notes".

## When not to use
- Designing the API contract to be documented → `api-design` first.
- Thesis chapters / academic prose → `thesis-helper`.
- Professional messages to people → `internship-communication`.
- Runbook content for production alerts → pair with `observability` (this skill formats it).

## Context intake
- Audience (new contributor / operator / API consumer / future self) and which docs already exist - prefer updating over creating.
Detect or confirm before starting (ask at most what is genuinely needed):
- Which context: one of the contexts defined in `docs/workflow-profile.md` ("Contexts")? Read `docs/active-context.md` first: if `Current` names a context set within the last day, use it, apply its rules, and do not ask. Otherwise fall back to the active roles and projects in `docs/workflow-profile.md`; ask when it could be two different contexts.
- What is the desired output: a plan, code, a review, tests, documentation, a deployment plan, or research notes? Confirm if ambiguous.

## Workflow
1. Read the my-skill plugin's `docs/workflow-profile.md`. If it is missing, contradicts this request, or was last updated more than ~3 months ago, confirm or update it with Sothy before applying any role, project, or stack assumptions.
2. Read the relevant code/config first; document what exists, not an idealized design.
3. Pick the smallest artifact that fits the need (add a section to an existing doc rather than a new file when possible).
4. Structure for the reader's job: setup docs ordered as copy-paste-able steps; API docs per endpoint; ADR = context → decision → consequences.
5. Verify every claim against the code: commands, flag names, env vars, endpoint paths must be copied from real files and match exactly.
6. Mark unknowns explicitly as `[TO VERIFY]` rather than guessing.
7. Recommend, don't just write: note where the doc should live (repo root, `docs/`, wiki) and what to delete/merge later.

## Adaptation rules

- Doc set scales with repo size: single README for small projects; add docs/ (adr/, runbooks) only when they earn their space.
- Every rule here is repo-type-agnostic - verify-against-code applies whether the repo is a job service, internship project, or thesis pipeline.

## Inputs needed
- The code, config, or diff to document (real files beat memory; read them before writing).
- Audience and purpose: new contributor, operator, API consumer, future self.
- Which docs already exist and where, so they are updated rather than duplicated.
- Any house style (tone, heading style) already present in the target repo.

## Output contract
- **Doc type + location** — what artifact, which file path, created vs updated.
- **Document** — ready-to-paste content.
- **Verified vs assumptions** — what was checked against code; what needs Sothy to confirm.
- **Follow-ups** — stale docs found en route that should be updated next.

## Rules and constraints
- Never document behavior the code doesn't show; if the intent differs from the implementation, flag the mismatch instead of papering over it.
- Copy exact names: no paraphrased env vars, commands, or placeholder values left in final docs.
- No secrets in docs — placeholders only (`${DB_URL}`), with a pointer to the secret store.
- Match the target repo's existing tone/structure; don't import a new style.
- Keep ADRs short (≤ 1.5 pages each): context, decision, consequences — history lives in git.

## Quality checklist

- [ ] Every command/field/endpoint verified against actual code.
- [ ] Unknowns marked [TO VERIFY], never guessed.
- [ ] No secrets - placeholders with secret-store pointers.
- [ ] Location recommendation + follow-up stale docs noted.

## Examples
1. **Request:** "Write a README for our retrieval API so my supervisor can run it."
   **Behavior:** Read the repo structure and config files; produce README with: what it does, prerequisites, exact setup commands (copied from real scripts/requirements), env var table with `[TO VERIFY]` for unknown values, a run example, and a project structure sketch. List follow-ups for stale docs found.
2. **Request:** "We switched from page-number to cursor pagination — write an ADR."
   **Behavior:** One-page ADR: context (inconsistent ordering under concurrent writes), decision (cursor tokens over pages), consequences (clients must migrate; no random page access), alternatives rejected (offsets, keyset-lite). Path suggestion `docs/adr/0003-cursor-pagination.md`.

## Lessons learned

Record improvements after real usage (maintained via ``continuous-improvement``). Format:

- ``<date>`` -- ``<what happened>`` -> ``<change made to this SKILL.md>``

(empty -- entries appear after real usage)
