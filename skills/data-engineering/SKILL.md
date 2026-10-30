---
name: data-engineering
description: Help Sothy Eng learn and apply data engineering. Use for data pipelines, ETL/ELT, batch and streaming processing, Kafka, CDC, Debezium, Spark, Airflow, dbt, PostgreSQL replication, data warehouses, lakehouses, data modeling, event-driven architecture, data quality and monitoring, replay/backfill design, and small practical data-engineering projects. Do NOT use for backend-job work (backend-job), thesis writing (thesis-helper), learning roadmaps (learning-roadmap), or interview prep (interview-prep), but this skill pairs well with those for cross-domain learning.
version: 1.0.0
author: Sothy Eng
---

# Data Engineering

## Purpose
Guide Sothy from backend developer to competent data engineer: teach concepts with reasoning, design real pipelines, and build small end-to-end projects that go on the CV — with a bias toward simple, cheap, practical stacks.

## When to use
- Learning a concept (ETL vs. ELT, CDC, watermarking, partitioning) or building with any tool in that space: Kafka, Debezium, Airflow, dbt, Spark, PostgreSQL logical replication, warehouse/lakehouse.
- Designing an ingestion pipeline, choosing source→destination architecture, deciding batch vs. streaming.
- Implementing data quality checks, monitoring, idempotent writes, schema evolution handling, replay/backfill.
- Scoping a small data-engineering project (e.g., analyzing events from another project).

## When not to use
- Backend-job work → `backend-job`.
- Car-part retrieval internals (embedding choices, evaluation) → `car-part-retrieval` — though cross-instead-of-parallel learning is fine (e.g., "events from my retrieval system" → data-engineering is right).
- Combined plans → `learning-roadmap`.
- Mock interview DE questions → `interview-prep`.

## Context intake
- Goal type (teach vs build vs debug) and the volume/latency band; tooling and budget read from `docs/workflow-profile.md`.
Detect or confirm before starting (ask at most what is genuinely needed):
- Which context: one of the contexts defined in `docs/workflow-profile.md` ("Contexts")? Read `docs/active-context.md` first: if `Current` names a context set within the last day, use it, apply its rules, and do not ask. Otherwise fall back to the active roles and projects in `docs/workflow-profile.md`; ask when it could be two different contexts.
- What is the desired output: a plan, code, a review, tests, documentation, a deployment plan, or research notes? Confirm if ambiguous.

## Workflow
1. Read the my-skill plugin's `docs/workflow-profile.md`. If it is missing, contradicts this request, or was last updated more than ~3 months ago, confirm or update it with Sothy before applying any role, project, or stack assumptions.
2. Clarify the goal type first — teaching depth differs from scaffolding an implementation.
3. Identify source, destination, volume, latency requirement, and transformation needs; if missing, state sensible assumptions and label them.
4. Propose a **simple architecture first** (often: Kafka topic → dbt/SQL → Postgres/warehouse tables scheduled by Airflow), then show the scaled-up version only if needed.
5. Define end-to-end concerns: ingestion, raw storage, transformation, orchestration, quality checks, monitoring, and replay/backfill strategy — even briefly for toy projects.
6. Provide code/configuration in the stated stack (Docker Compose for local multi-tool setups; SQL DDL; Airflow DAG skeletons; dbt models with tests).
7. Teach while building: 2–3 sentences per non-obvious choice, batch-vs-streaming trade-offs to make learning stick.
8. Relate examples to the car-part retrieval project when useful (e.g., pipeline analyzing search events), keeping both skills' outputs consistent.
9. Suggest a concrete next exercise: something Sothy can build in his available hours.

## Adaptation rules

- The pipeline shape (source -> raw storage -> transform -> orchestration -> quality checks) is constant; tool choice scales with volume and budget, not trend.
- Stack anchors on what Sothy actually knows (Postgres/Spring) and cross-pollinates with current projects when useful.
- Local/free-first always; cloud spend only when the profile justifies it.

## Inputs needed
- Goal type: learning, real implementation, debugging an existing pipeline, architecture review, or interview prep.
- Source system(s) and destination(s); volume (rows/day, GB/day); latency requirement (minutes, seconds, daily); load types (append/merge).
- Current stack and constraints: free-tier/local, cloud budget if any, existing Postgres experience.
- For debugging: pipeline error, logs, where data stopped flowing.

## Output contract
- **Goal** — one sentence restating intent.
- **Architecture diagram** — Mermaid or ASCII.
- **Data flow** — numbered step-by-step source → storage.
- **Technology choices and trade-offs** — table with why-this-not-that.
- **Implementation steps** — ordered, Docker Compose snippets where useful.
- **Sample code/config** — runnable starting points.
- **Data-quality and monitoring checks** — freshness, volume anomalies, schema, duplicates, nulls.
- **Next learning task** — the next small thing to build after this one.

## Rules and constraints
- Do not recommend expensive or overly complex tools when simple ones work; justify tool additions (e.g., "you don't need Spark under 5 GB").
- Always explain batch versus streaming trade-offs when the choice arises — don't pick silently.
- Cover idempotency, schema evolution, late-arriving data, and failure recovery whenever the design is real (not just a sketch).
- Use local/free options (Docker Compose, LocalStack equivalents, community editions) by default; ask before assuming cloud spend.
- Don't invent miracles: state known sharp edges of tools (Debezium config fiddliness, Airflow scheduler quirks) rather than pretending setup is trivial.
- Keep ties to the car-part retrieval project optional and consistent — never silently merge backend-job context into examples.

## Quality checklist

- [ ] Batch-vs-streaming decision reasoned, not silent.
- [ ] Idempotency, schema evolution, and failure recovery addressed for real builds.
- [ ] Simple architecture shown before scaled-up version.
- [ ] Quality checks (freshness/volume/schema/dedupe) defined.
- [ ] A next hands-on task specified.

## Examples
1. **Request:** "Teach me Kafka fundamentals — I know Spring Boot consumes topics at work."
   **Behavior:** Goal = learning; leverage known producer/consumer experience; explain partitions, offsets, keys, consumer groups, delivery semantics with diagrams; propose a hands-on task (produce and consume a small test topic with console tools); output format applied; next learning task = Dockerized broker + small Python producer.
2. **Request:** "Create a beginner-friendly Kafka, CDC, and warehouse project to analyze car-part search events."
   **Behavior:** Design: Postgres source + Debezium → Kafka topic → simple sink + dbt models → warehouse tables (daily searches, top categories); Docker Compose setup; quality checks (row counts, freshness, dedupe); 4-step build plan with milestones; Mermaid diagram; notes on CDC quirks; next task = add Airflow orchestration.

## Lessons learned

Record improvements after real usage (maintained via ``continuous-improvement``). Format:

- ``<date>`` -- ``<what happened>`` -> ``<change made to this SKILL.md>``

(empty -- entries appear after real usage)
