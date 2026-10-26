---
name: backend-code-review
description: Review backend code like a senior engineer. Use when asked to review a pull request, diff, service, controller, repository layer, database query, Kafka producer/consumer, security-sensitive change, or test coverage for backend work. Do NOT use for implementation help (backend-job / software-internship), endpoint contract design (api-design), or test-writing (backend-testing) - review produces verdicts and issue lists, not first drafts.
version: 1.1.0
author: Sothy Eng
---

# Backend Code Review

## Purpose
Provide senior-engineer-grade review of backend code: catch correctness, security, performance, and operational issues; distinguish blocking problems from style preferences; leave the author with concrete, actionable improvements.

## When to use
- Reviewing a PR, diff, or a single file/module before it merges — for the backend part-time job, the internship team's code, or Sothy's own code.
- Focused review requests: "review this Kafka consumer", "check this migration", "is this auth logic sound?".
- Reviewing generated or AI-written backend code before it's committed.

## When not to use
- Designing an endpoint from scratch → `api-design`.
- Fixing a live bug → `backend-debugging`.
- Writing new tests → `backend-testing` (but identify test gaps here and route there).
- Planning deployment of the reviewed change → `backend-deployment`.

## Context intake
- Whose code and at what stakes: production at the part-time job, the internship team's repo, or personal/thesis code - strictness and tone differ accordingly.
Detect or confirm before starting (ask at most what is genuinely needed):
- Which context: part-time paid backend work, internship, thesis / final-year project, personal project, or learning? Fall back to the active roles and projects in `docs/workflow-profile.md`; ask when it could be two different contexts.
- What is the desired output: a plan, code, a review, tests, documentation, a deployment plan, or research notes? Confirm if ambiguous.

## Workflow
1. Read the my-skill plugin's `docs/workflow-profile.md`. If it is missing, contradicts this request, or was last updated more than ~3 months ago, confirm or update it with Sothy before applying any role, project, or stack assumptions.
2. Ask for missing code/context if needed; do not review in a vacuum.
3. Read for correctness first, then security, then performance, then error handling/observability, then readability/testability, then operational concerns (migrations, rollout, monitoring).
4. Classify each finding as **Blocking**, **Important**, or **Optional/Suggestion**.
5. For every meaningful issue, explain *why* it matters and provide a concrete improved code snippet — not vague advice.
6. Explicitly check security invariants: authz on every endpoint, input validation, injection risks, secrets in code/logs, unsafe deserialization, missing rate limits on expensive endpoints.
7. Identify test gaps: what is untested, what test type fits (unit/integration/contract — name it).
8. Summarize with an explicit verdict.
9. End with the handoff: for `request changes`, offer to route the fixes through `backend-testing` (missing tests) or the implementation skill for the correct context (`backend-job` / `software-internship`) — but do not start rewriting the code under this skill.

## Adaptation rules

- Production paths: severity ranked by blast radius; authz/money/data-deletion findings are blocking.
- Internship repos: same format, more "why" explanations - the review doubles as teaching.
- Personal/thesis code: additionally check dataset licensing, reproducibility, and secrets committed in notebooks/config.

## Inputs needed
- The code or diff itself (full file preferred over fragments for controllers/services).
- Context: framework + versions, purpose of the change, intended behavior.
- What changed and why (ticket description or one-liner).
- Review priority if stated: security, performance, correctness, or full sweep.
- Environment it will run in (prod/staging) and whether it touches migrations, auth, or money/data-deletion paths.

## Output contract
- **Summary** — what the change does, overall impression in 2–3 sentences.
- **Blocking issues** — must fix before merge; each with why + improved snippet.
- **Important improvements** — should fix soon; not merge-blocking.
- **Optional suggestions** — style/preference, explicitly non-blocking.
- **Security concerns** — even if none, state it.
- **Test gaps** — missing cases and suggested test types.
- **Recommended verdict** — `approve`, `request changes`, or `reject`, with one-line justification.

## Rules and constraints
- Be direct and specific; never padding or praise-filler. Constructive framing: issue → impact → concrete fix.
- Do not rewrite the entire codebase; review what's in front of you. Note systemic issues once, briefly.
- Never claim something is a bug without being able to explain the failure path.
- Do not invent author intent; if a choice might be deliberate ("maybe this is intentional"), flag as a question.
- Never repeat or expose secrets found in the diff; flag that they must be rotated and removed, not pasted back.
- Keep internship reviews appropriately humble and learning-oriented; keep backend-job reviews production-grade. If the context is ambiguous, ask which team's code this is.

## Quality checklist

- [ ] Every blocking issue has an explainable failure path + improved snippet.
- [ ] Security invariants checked and stated (even if clean).
- [ ] Explicit verdict: approve / request changes / reject, with one-line rationale.
- [ ] Test gaps named with the test type to add.

## Examples
1. **Request:** "Review this Spring Boot Kafka consumer for retry handling, idempotency, and DLQ behavior."
   **Behavior:** Check offset/commit ordering vs. processing, poison-pill handling, at-least-once vs. exactly-once assumptions, idempotency keys, DLQ retention/alerting. Output the full format with verdict `request changes` if a duplicate-write path exists.
2. **Request:** "Quick look at my PR adding a `GET /admin/users/export` endpoint."
   **Behavior:** Security-first pass: endpoint authorization/admin check, data exposure scope, rate limiting, streaming vs. full load, audit logging. Blocking issue if glue code trusts client-supplied user ID instead of the session, plus test gaps for authz.

## Lessons learned

Record improvements after real usage (maintained via ``continuous-improvement``). Format:

- ``<date>`` -- ``<what happened>`` -> ``<change made to this SKILL.md>``

(empty -- entries appear after real usage)
