---
name: observability
description: Instrument and monitor running backend services for production readiness. Use when adding or reviewing logs, metrics, dashboards, alerts, SLOs/error budgets, health checks, tracing, or day-2 runbooks for a service - e.g. "what metrics should this Kafka consumer expose", "design alerts for our orders API", "is this SLO healthy", "write a runbook for consumer lag". Do NOT use for pre-launch deployment planning (backend-deployment) or root-cause analysis of an active incident (backend-debugging).
version: 1.0.0
author: Sothy Eng
---

# Observability

## Purpose
Make production services observable day-2: the right metrics/logs/traces for the *actual* failure modes, dashboards a teammate can read, alerts that select actionable signal from noise, SLOs that reflect user experience, and runbooks that turn an alert into a first action.

## When to use
- "What should this service/consumer/endpoint be monitored for?"
- Adding or improving logging (levels, correlation/request IDs, redaction) in a service.
- Designing dashboards, alerts, paging thresholds, or SLOs/error budgets.
- Writing or reviewing a runbook entry for a known failure mode (alert → check → action).
- Health-check and readiness/liveness design for deploys.

## When not to use
- Something is broken right now → `backend-debugging`.
- Planning how a change ships → `backend-deployment` (its verification/monitoring section stays there for that change).
- Reviewing code quality → `backend-code-review`.

## Context intake
- Monitoring stack, alert channel, and on-call reality (detect first; never invent the tooling).
Detect or confirm before starting (ask at most what is genuinely needed):
- Which context: part-time paid backend work, internship, thesis / final-year project, personal project, or learning? Fall back to the active roles and projects in `docs/workflow-profile.md`; ask when it could be two different contexts.
- What is the desired output: a plan, code, a review, tests, documentation, a deployment plan, or research notes? Confirm if ambiguous.

## Workflow
1. Read the my-skill plugin's `docs/workflow-profile.md`. If it is missing, contradicts this request, or was last updated more than ~3 months ago, confirm or update it with Sothy before applying any role, project, or stack assumptions.
2. Ask for tooling, environment, and past incident history; never assume a monitoring stack.
3. Inventory the user journey first: list the 2–4 golden signals per surface (latency p50/p95/p99, traffic/error rate, saturation) and the business metrics behind them.
4. Map each to concrete instrumentation: metric names/labels (beware high-cardinality explosion), log line + level, trace spans, Kafka consumer lag / offset metrics, DB pool + Redis hit-rate metrics.
5. Write dashboard design: one row per user journey, key metric → supporting metric; mark which panel answers "is the user OK" vs "is the component OK".
6. Design alerts with: symptom-based triggers (user-visible) over cause-based ones, concrete threshold + `for` duration, severity/page vs ticket, and the linked first-runbook-questions.
7. SLOs target a minimal viable set: pick 1–2 user-journey SLOs, compute error budget, define the review cadence; skip SLO theater for small teams unless asked.
8. Produce the runbook table: alert → meaning → first three checks (concrete queries/commands) → likely actions → escalation.
9. Add a logging hygiene pass: log at the moment you handle or fail, include request/consumer/correlation IDs, never log secrets or PII raw.

## Adaptation rules

- Instrumentation план adapts per profile stack: Spring Micrometer, FastAPI metrics, Kafka lag monitoring - names and labels follow the actual tooling.
- Alert volume scales to team reality: no paging targets for hours nobody is on-call.
- Same golden-signals-first discipline for any service type (API, consumer, pipeline).

## Inputs needed
- The service/component and what user-facing thing it protects (orders, search, exports).
- Stack and where it runs (Spring Boot/FastAPI/Go; Docker/K8s/VM; PostgreSQL/Redis/Kafka).
- Existing tooling if any: Prometheus/Grafana, CloudWatch, Datadog, ELK — never invent their tooling; ask.
- Known failure modes or past incidents worth guarding against.
- Who is paged (on-call reality: is anyone truly on-call at a startup/small team?).

## Output contract
- **Service surface** — user journeys and what protects them.
- **Metrics/instrumentation plan** — service → tools with names and labels (flag cardinality risk).
- **Dashboard wire-up** — described per row: journey, panels, layout logic.
- **Alert catalog** — table: alert, metric + threshold + duration, severity, action link.
- **SLO proposal** — journeys, targets, error budget, review cadence (only when asked or applicable).
- **Runbook draft** — table of alert → meaning → checks → actions → escalation.
- **Gaps and risks** — blind spots that remain (e.g., no trace stack, sampling too thin).

## Rules and constraints
- Symptom alerts (user-visible pain) come before cause alerts (CPU, restarts); if list gets long, cut, don't add noise.
- Never invent the monitoring stack, cloud provider, or alert channel. Ask if unknown; propose candidates only after they answer.
- Never log or alert with secrets, tokens, or PII content; redact or hash identifiers.
- SLOs are commitments made by a team — recommend only what Sothy's team can realistically honor; question paging for hours no one is on-call.
- Keep runbook actions production-safe: read-only checks first, reversible actions only.
- One responsibility = observability; don't re-derive the fix (that's `backend-debugging`) or the ship plan (that's `backend-deployment`).

## Quality checklist

- [ ] Alerts are symptom-based, thresholded, and actionable.
- [ ] Metric labels avoid cardinality explosion.
- [ ] Runbook covers: alert -> meaning -> first checks -> action -> escalation.
- [ ] Monitoring stack confirmed with Sothy; remaining blind spots listed.

## Examples
1. **Request:** "What metrics and alerts do we need for our new Kafka consumer writing to Postgres?"
   **Behavior:** Golden signals for the write path (consumer lag, poll-vs-process rate, DB insert latency/error rate, DLQ offset growth), concrete metric names with labels, lag-based page alert with `for` window, dashboard rows, runbook table starting with `kafka-consumer-groups --describe`. Ask which alerting tool they use before writing config.
2. **Request:** "Write a runbook for the 500s-spike alert."
   **Behavior:** One page: what it means (likely causes in one line), first three read-only checks with exact queries/commands, decision tree (new deploy → rollback; DB errors → check pool/lock metrics), escalation owner placeholder. Output applies this skill's runbook-table format.

## Lessons learned

Record improvements after real usage (maintained via ``continuous-improvement``). Format:

- ``<date>`` -- ``<what happened>`` -> ``<change made to this SKILL.md>``

(empty -- entries appear after real usage)
