---
name: api-design
description: Design clean, consistent, production-ready REST APIs and service contracts. Use when designing new endpoints or microservices, defining request/response schemas, choosing HTTP methods and status codes, specifying pagination/filtering/error handling, deciding auth/idempotency/rate limiting/versioning, or producing OpenAPI documentation. Do NOT use for debugging a failing endpoint (backend-debugging), reviewing existing API code (backend-code-review), or internship task implementation (software-internship) - design the contract here first, then route implementation to the right skill.
version: 1.0.0
author: Sothy Eng
---

# API Design

## Purpose
Help design clean, consistent, production-ready REST APIs and service contracts: correct resource modeling, conventional HTTP semantics, robust error handling, and explicit security/versioning decisions — documented enough to hand to a frontend, mobile, or service consumer.

## When to use
- New endpoint or new microservice design for any context (backend job, internship, or car-part retrieval project API).
- Defining request/response schemas and validation rules.
- Choosing pagination, filtering, sorting, idempotency, rate limiting, caching, or versioning strategies.
- Producing OpenAPI (Swagger) specifications.
- Reviewing a proposed contract before implementation.

## When not to use
- The endpoint is failing or slow → `backend-debugging`.
- Reviewing an implementation PR → `backend-code-review`.
- Implementing the endpoint within a specific task → `backend-job` (backend job) or `software-internship` (internship) — ask the routing question if the context is unclear.
- Data modeling for analytics/warehouse tables → `data-engineering`.

## Context intake
- API audience (web / mobile / partner / internal service) and whether the contract replaces an existing one - that decides breaking-change handling.
Detect or confirm before starting (ask at most what is genuinely needed):
- Which context: one of the contexts defined in `docs/workflow-profile.md` ("Contexts")? Read `docs/active-context.md` first: if `Current` names a context set within the last day, use it, apply its rules, and do not ask. Otherwise fall back to the active roles and projects in `docs/workflow-profile.md`; ask when it could be two different contexts.
- What is the desired output: a plan, code, a review, tests, documentation, a deployment plan, or research notes? Confirm if ambiguous.

## Workflow
1. Read the my-skill plugin's `docs/workflow-profile.md`. If it is missing, contradicts this request, or was last updated more than ~3 months ago, confirm or update it with Sothy before applying any role, project, or stack assumptions.
2. Clarify the business capability and consumers; ask one short clarifying round only if something essential is missing.
3. Identify resources, operations, ownership, and relationships. Model nouns, not actions; push behavior-driven endpoints toward sub-resources or domain operations deliberately when needed.
4. Propose endpoint paths and methods with concrete example request/response bodies for the happy path.
5. Specify for every endpoint: validation rules, auth/permissions, error responses, pagination, filtering, caching headers, idempotency, retry behavior, and versioning.
6. Produce an endpoint table (method, path, purpose, auth, key params, notes).
7. Write OpenAPI YAML when requested or when the consumer needs generated clients/docs.
8. List edge cases and the tests each consumer/reviewer should expect.

## Adaptation rules

- Web/mobile consumer APIs: cursor pagination + full error envelope; internal admin tools: simpler versioning but unchanged authz discipline.
- ML/vision endpoints (image upload / search jobs): prefer async 202 + job-resource or streaming responses; never expose model internals or raw index artifacts.
- Internship or team APIs: mirror the team's existing naming/envelope conventions instead of these defaults when they differ; say which won and why.

## Inputs needed
- The business capability in one or two sentences.
- Who consumes the API (frontend, mobile, partner, internal service).
- Existing conventions (if any) from the codebase or team.
- Whether the API is public, partner-facing, or internal.
- Any non-functional constraints: expected traffic, latency targets, consistency needs.

## Output contract
- **API goal** — capability + consumers.
- **Resource model** — resources, relationships, ownership.
- **Endpoint table** — method, path, purpose, auth, params, notes.
- **Example requests and responses** — JSON for the happy path and one representative endpoint set.
- **Error responses** — standard error body shape + status code usage table.
- **Security and validation rules** — auth, permission model, input validation, rate limiting, idempotency.
- **OpenAPI YAML** — only if requested.
- **Edge cases and tests** — short list.

## Rules and constraints
- Use consistent naming (plural nouns, kebab-case paths, camelCase JSON fields unless an existing convention differs) and conventional HTTP semantics; 4xx = client mistake, 5xx = server mistake, never 200 for errors.
- Never leak internal database details (IDs' internal meaning, SQL errors, table/column names, stack traces) in responses.
- Flag breaking changes explicitly (renamed fields, changed status codes, removed fields) and prefer additive changes versioned contracts.
- Do not invent company endpoints, data models, or a company name; design from what is given and mark assumptions clearly.
- Keep the contract implementable: concrete examples over abstract rules.

## Quality checklist

- [ ] Every endpoint: method/path/auth/validation/error shape defined.
- [ ] No internal schema or DB details leak into examples.
- [ ] Breaking changes flagged with migration notes.
- [ ] Examples are copy-pasteable, realistic JSON.

## Examples
1. **Request:** "Design the API for managing car-kit bundles in an internal admin tool."
   **Behavior:** Clarify admin vs. customer consumers. Produce a resource model (bundles, bundle items, SKUs), endpoint table, JSON examples, error shape, permission notes, and edge cases (bundle with discontinued part, concurrent edits).
2. **Request:** "Our mobile team needs an orders endpoint supporting status filter and cursor pagination."
   **Behavior:** Design `GET /v1/orders?status=shipped&cursor=...&limit=...`, define response envelope and cursor semantics, idempotent webhook for status updates if relevant, OpenAPI YAML on request, and flag pagination-strategy change as breaking if replacing page numbers.

## Lessons learned

Record improvements after real usage (maintained via ``continuous-improvement``). Format:

- ``<date>`` -- ``<what happened>`` -> ``<change made to this SKILL.md>``

(empty -- entries appear after real usage)
