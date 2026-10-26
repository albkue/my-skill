---
name: backend-deployment
description: Prepare safe backend deployments. Use when planning Docker packaging, CI/CD pipelines, environment configuration, database migrations, release/rollout strategies (blue-green, canary, rolling), pre-deployment checklists, monitoring/alerting setup, rollback plans, or incident response for a backend service. Do NOT use for writing the release notes (internship-communication), reviewing the deploy scripts' code (backend-code-review), or debugging a failed deployment in flight (backend-debugging).
version: 1.1.0
author: Sothy Eng
---

# Backend Deployment

## Purpose
Make deployments boring: every change goes out with known risk, a verified checklist, health checks, monitoring, and a rollback plan written before it ships.

## When to use
- Planning a release or rollout for the backend part-time job.
- Designing Docker images, CI/CD pipeline stages, or environment configuration.
- Planning risky changes: schema migrations, new dependencies, infra changes, new integrations.
- Writing runbooks: health checks, alerts, rollback steps, incident response.

## When not to use
- The deployment is currently broken mid-rollout → `backend-debugging`.
- Ongoing observability work beyond this change's verification (dashboards, SLOs, full runbooks) → `observability`.
- Reviewing the code of the deploy scripts → `backend-code-review`.
- Writing or updating repo docs for the release → `documentation`.
- Learning about deployment concepts for interview prep → `interview-prep`.
- Internship status updates about a release → `internship-communication`.

## Context intake
- Deploy method and who owns it (K8s/VM/PaaS/university server), environment count, migrations involved, and whether the release is team-owned or personal.
Detect or confirm before starting (ask at most what is genuinely needed):
- Which context: part-time paid backend work, internship, thesis / final-year project, personal project, or learning? Fall back to the active roles and projects in `docs/workflow-profile.md`; ask when it could be two different contexts.
- What is the desired output: a plan, code, a review, tests, documentation, a deployment plan, or research notes? Confirm if ambiguous.

## Workflow
1. Read the my-skill plugin's `docs/workflow-profile.md`. If it is missing, contradicts this request, or was last updated more than ~3 months ago, confirm or update it with Sothy before applying any role, project, or stack assumptions.
2. Ask for the missing deployment facts above; do not assume cloud provider or infrastructure details.
3. Identify breaking changes and dependencies: API contract changes, migration order, config/env vars, client compatibility, third-party limits.
4. Build the pre-deployment checklist (use `references/backend-checklist.md` deployment section, tailored).
5. Define deployment steps in order, with the safe bit-size: migrate → deploy → verify. Migrations are backward-compatible or explicitly coordinated with app versions.
6. Define verification: health checks, smoke tests, key business metrics to watch for the first 24–48h.
7. Write the rollback plan concretely: previous artifact, data reversibility, feature-flag off, who executes.
8. Define monitoring + alerts that would catch this specific change's failure modes (route deep observability design to `observability`).
9. Add the post-launch validation checkpoint: what is verified at +1h, +24h, and +48h (error rates, latency p95, business metrics, data sanity), who reviews it, and the go/no-go to close the change out.

## Adaptation rules

- The process shape is constant across environments: checklist -> ordered steps -> verification -> rollback -> post-launch validation; only the tooling changes.
- Personal/thesis deployments: free tiers and simplified checklists are fine, but data-changing steps still require backup + rollback.
- Internship/team releases: adopt the team's existing release process when known instead of proposing a parallel one.

## Inputs needed
- Deployment target and method: Docker/Kubernetes/VM/platform-as-a-service; how the team currently deploys.
- Environment(s): staging, production; promotion path.
- Tech stack and runtime (Spring Boot/FastAPI/Go), config approach (env vars, secret store).
- Database changes: new migrations? destructive columns? data backfill?
- Rollout method available: rolling, blue-green, canary, feature flags.
- Who deploys and when (business hours constraint? on-call?).

## Output contract
- **Change summary** — what ships and why.
- **Risk assessment** — ranked failure modes with likelihood and blast radius.
- **Pre-deployment checklist** — checked actions (tests, migrations verified, config, secrets, backup).
- **Deployment steps** — ordered, copy-pasteable where possible.
- **Verification steps** — health checks + smoke tests post-deploy.
- **Rollback plan** — exact steps, data handling, decision criteria for triggering it.
- **Monitoring checklist** — metrics/logs/alerts specific to this change.

## Rules and constraints
- Never recommend deploying untested or unreviewed database migrations; forward-test on staging with production-like data volume first.
- Every plan must include a rollback plan; if a change is irreversible (destructive migration), state that explicitly and propose a safe two-phase alternative (expand → migrate → contract).
- Ask before assuming cloud provider, container orchestrator, or internal deployment tooling.
- Never include real secrets, internal hostnames, or credentials in plans; use placeholders.
- Production changes get explicit "what could hurt users" language, not just steps.

## Quality checklist

- [ ] Pre-deployment checklist complete (tests, migration verified, config, secrets, backup).
- [ ] Rollback plan is concrete: artifact, data handling, trigger criteria.
- [ ] Destructive migrations converted to expand-contract where possible.
- [ ] Post-launch validation checkpoints defined (+1h / +24h / +48h).

## Examples
1. **Request:** "We're adding a `status` column to orders and deploying next week."
   **Behavior:** Flag destructive risk, propose expand-contract (nullable column + backfill + later `NOT NULL` in a separate release), checklist (tested migration on prod-like data size, backup), steps, rollback (drop column if pre-geo, or revert code reading it), monitoring for query-plan changes.
2. **Request:** "First Kafka consumer going to prod — what do I need?"
   **Behavior:** Ask about cluster access, deployment infra, and on-call setup. Checklist: consumer group config, DLQ, lag alerting, idempotency, startup behavior on missing topics, feature-flagged consumption, rollback = disable + retain offsets, monitoring checklist.

## Lessons learned

Record improvements after real usage (maintained via ``continuous-improvement``). Format:

- ``<date>`` -- ``<what happened>`` -> ``<change made to this SKILL.md>``

(empty -- entries appear after real usage)
