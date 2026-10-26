---
name: backend-debugging
description: Debug backend issues systematically - root-cause analysis before fixes. Use when a backend system is failing or misbehaving - HTTP errors, database errors, Kafka issues (lag, rebalances, serialization), Redis issues, authentication failures, high latency, memory pressure, race conditions, or deployment failures. Do NOT use for design-time API decisions (api-design), code review of a working PR (backend-code-review), or general feature work (backend-job / software-internship). If the incident belongs to the backend part-time job vs. the internship and it matters, ask which context first.
version: 1.1.0
author: Sothy Eng
---

# Backend Debugging

## Purpose
Turn vague complaints ("it's slow", "500s spiked") into a hypothesis-driven diagnosis: collect symptoms, form candidate causes, confirm the cheapest way, then fix and prevent.

## When to use
- A concrete error, exception, or wrong behavior in a backend system.
- Performance or latency problems, memory growth, thread/connection pool exhaustion.
- Kafka consumer lag, rebalance storms, deserialization errors; Redis eviction/latency; DB deadlocks, timeouts, replication lag; auth/permission failures; flaky behavior under load; deployment or rollout failures.

## When not to use
- Designing a new endpoint or fixing the design (not a defect) → `api-design`.
- Reviewing code quality of a working change → `backend-code-review`.
- Writing the regression test suite for the fix → `backend-testing`.
- General feature implementation → `backend-job` or `software-internship`.

## Context intake
- Environment (local/staging/prod), when behavior changed, and whether a fast mitigation or the full root-cause chain is wanted first.
Detect or confirm before starting (ask at most what is genuinely needed):
- Which context: part-time paid backend work, internship, thesis / final-year project, personal project, or learning? Fall back to the active roles and projects in `docs/workflow-profile.md`; ask when it could be two different contexts.
- What is the desired output: a plan, code, a review, tests, documentation, a deployment plan, or research notes? Confirm if ambiguous.

## Workflow
1. Read the my-skill plugin's `docs/workflow-profile.md`. If it is missing, contradicts this request, or was last updated more than ~3 months ago, confirm or update it with Sothy before applying any role, project, or stack assumptions.
2. Collect symptoms. If evidence is missing, ask for the smallest set of facts needed — never guess silently.
3. List 2–4 plausible root causes, ranked by likelihood, each with the evidence that would confirm/deny it.
4. Suggest the **fastest safe confirmation** step per hypothesis (log query, metric, `EXPLAIN ANALYZE`, kcat/redis-cli probe, canary) — production-safe actions first.
5. Once the likely root cause is identified, give the fix: smallest reversible change first; include exact code/config where possible.
6. Add prevention: the code/config change, a rule (lint, CI check, alert), or a runbook note.
7. Suggest monitoring or alerting so recurrence is detected within minutes, not days. For day-2 coverage design (dashboards, SLOs, full runbooks), route to `observability` instead of duplicating it here.
8. After the fix is agreed, offer the implementation path: provide the regression test plan via `backend-testing`, and route code changes through `backend-job` (backend job) or `software-internship` (internship) — ask which context if relevant.

## Adaptation rules

- Discriminating probes follow the stack: EXPLAIN for SQL, kcat/offset math for Kafka, redis-cli for Redis, profiler/backtraces for leaks.
- ML/CV pipeline failures: add data-shape and experiment-config checks to the hypothesis list.
- Personal/thesis environments: cheaper instrumentation is fine, but the hypothesis-rank-confirm discipline stays identical.

## Inputs needed
- Exact error message / log excerpts (redacted), stack traces, HTTP status.
- Endpoint, service, and environment (local/staging/prod), and when it started.
- Frequency, blast radius, and recent changes (deploy, config, migration, traffic).
- Infrastructure facts known so far: DB engine and version, Kafka setup, Redis mode, deployment target.

## Output contract
- **Symptoms** — what is observed, where, since when.
- **Possible causes** — ranked, with expected confirming evidence.
- **Diagnostic steps** — concrete commands/queries per cause, ordered cheapest-first.
- **Likely root cause** — stated, or explicitly "not yet confirmed, best current hypothesis".
- **Fix** — concrete change(s), smallest first.
- **Prevention** — code/test/checklist changes that stop recurrence.
- **Monitoring or alerting suggestions** — specific metric/log/threshold ideas.

## Rules and constraints
- Do not jump to a fix without asking for key evidence when the failure mode is genuinely ambiguous.
- Prioritize production safety: no destructive operations, no `DROP`/`TRUNCATE`/`rm -rf`, no restarting customer traffic without flagging consequences. Recommend read-only diagnostics first.
- Prefer reversible changes (feature flags, config, targeted fix) over irreversible ones.
- Never ask for or repeat secrets; tell Sothy to redact tokens/PII from logs before sharing.
- If the incident is in the internship's project instead of the backend job, switch to the correct context and say so.

## Quality checklist

- [ ] Root cause confirmed or explicitly labeled as best current hypothesis.
- [ ] Diagnostic steps are read-only and production-safe.
- [ ] Fix is reversible, or irreversibility is flagged.
- [ ] Prevention step + monitoring suggestion included.

## Examples
1. **Request:** "Kafka consumer keeps restarting every few minutes."
   **Behavior:** Ask for consumer logs, group config (max.poll.*, session.timeout), broker settings, message payloads. Rank causes (processing time > max.poll.interval.ms, deserialization crash, rebalance loop). Give a safe check (compare poll durations in logs), fix, prevention (durable offset handling, alerting on lag), and monitoring suggestions.
2. **Request:** "An endpoint started returning 500 after yesterday's release."
   **Behavior:** Ask specific evidence (stack trace, error log, deploy diff). Rank causes (migration mismatch, N+1 → pool exhaustion, config regression). Give diagnostic steps in environment order, a minimal reversible fix, regression test suggestion, prevention (CI contract check), and an alert on 5xx rate.

## Lessons learned

Record improvements after real usage (maintained via ``continuous-improvement``). Format:

- ``<date>`` -- ``<what happened>`` -> ``<change made to this SKILL.md>``

(empty -- entries appear after real usage)
