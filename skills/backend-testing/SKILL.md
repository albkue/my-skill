---
name: backend-testing
description: Create practical backend tests. Use when asked to write unit tests, integration tests, API tests, database tests, Kafka tests, contract tests, or regression tests, or to plan what tests a change needs. Use the right framework for the stack (JUnit/Mockito/Testcontainers for Spring, pytest for FastAPI, Go testing). Do NOT use for finding where to focus during a review (backend-code-review) or general implementation help (backend-job / software-internship).
version: 1.0.0
author: Sothy Eng
---

# Backend Testing

## Purpose
Turn untested backend code into meaningfully tested backend code: choose the right test type per risk, name concrete cases, and generate runnable tests that won't rot.

## When to use
- Writing tests for services, controllers, repositories, Kafka producers/consumers, or scheduled jobs.
- Planning the test strategy for a new feature or a bug fix.
- Covering a regression before a fix ships.
- Deciding what to mock vs. what to run for real (Testcontainers, in-memory DB, embedded Kafka).

## When not to use
- Reviewing someone else's test quality → `backend-code-review`.
- Contract design for inter-service tests → `api-design` for the contract, `backend-testing` for the test.
- Implementation of the feature being tested → `backend-job` or `software-internship`.

## Context intake
- The repository's existing test framework and conventions (detect, don't impose) and what risk class the change is (auth/money/data vs cosmetic).
Detect or confirm before starting (ask at most what is genuinely needed):
- Which context: one of the contexts defined in `docs/workflow-profile.md` ("Contexts")? Read `docs/active-context.md` first: if `Current` names a context set within the last day, use it, apply its rules, and do not ask. Otherwise fall back to the active roles and projects in `docs/workflow-profile.md`; ask when it could be two different contexts.
- What is the desired output: a plan, code, a review, tests, documentation, a deployment plan, or research notes? Confirm if ambiguous.

## Workflow
1. Read the my-skill plugin's `docs/workflow-profile.md`. If it is missing, contradicts this request, or was last updated more than ~3 months ago, confirm or update it with Sothy before applying any role, project, or stack assumptions.
2. Identify code under test, dependencies, framework, and existing conventions. Match the conventions; don't introduce a competing style.
3. Enumerate test cases in classes: happy path, input validation, failure paths, edge cases, concurrency, security/authorization.
4. For each dependency, decide: real (integration), fake (in-memory), or mock (unit) — and justify briefly.
5. Generate test code: deterministic, isolated, descriptive names (*given/when/then* style), one behavior per test.
6. Give the commands to run the tests locally and in CI.
7. Identify remaining coverage gaps — the cases that would still be untested and their risk.

## Adaptation rules

- Framework follows the repo: JUnit/Mockito/Testcontainers, pytest, Go testing, JS - never introduce a competing style.
- Personal/thesis projects: pytest-first, lighter integration setups; ML experiment "tests" assert seeded metric ranges, not exact values.
- Same suite-shape rule everywhere: happy + validation + failure + edge + concurrency/security.

## Inputs needed
- The code under test (method, class, endpoint) and its dependencies.
- Test framework and existing test conventions (JUnit 5 + Mockito, pytest, Go `testing`, Testcontainers?).
- What the code should do — expected behavior, not implementation details.
- Which integration points exist (PostgreSQL, Redis, Kafka) and whether the team runs real ones in tests.

## Output contract
- **Test objective** — what behavior this test suite protects.
- **Test cases** — table or list, grouped by happy/validation/failure/edge/concurrency/security.
- **Test code** — complete, runnable test classes/functions.
- **Mocks/fixtures** — what's faked, how, and why.
- **Commands to run tests** — local + CI.
- **Coverage gaps** — what remains untested and the residual risk.

## Rules and constraints
- Prefer meaningful behavioral tests over chasing a coverage percentage; never generate coverage-farming tests.
- Avoid brittle tests tied to implementation details (internal method order, exact log text, private state).
- Every suite must include negative and failure-path tests, not just happy paths.
- No network calls, no shared mutable state between tests; clean data setup/teardown.
- Never invent team test conventions; if unknown, state the assumption and ask.
- Match the module's existing framework versions.

## Quality checklist

- [ ] Negative and failure-path cases included.
- [ ] Tests deterministic, isolated, behavior-named.
- [ ] Real/fake/mock choice justified per dependency.
- [ ] Run commands given for local + CI.

## Examples
1. **Request:** "Write tests for my Spring Boot service method that places an order."
   **Behavior:** Cases: valid order, invalid quantity, out-of-stock failure, concurrent duplicate request (idempotency), payment-gateway timeout. Unit tests with Mockito for the payment client, integration test with Testcontainers PostgreSQL for persistence. Full output format.
2. **Request:** "Test the Kafka consumer that updates order status."
   **Behavior:** Cases: valid event, duplicate event (idempotent no-op), malformed payload → DLQ/retry boundary, out-of-order events. Embedded/Testcontainers Kafka consumer test + a unit test of the handler. Include poison-pill test and the run commands.

## Lessons learned

Record improvements after real usage (maintained via ``continuous-improvement``). Format:

- ``<date>`` -- ``<what happened>`` -> ``<change made to this SKILL.md>``

(empty -- entries appear after real usage)
