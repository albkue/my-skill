# Data Engineering Checklist

Default pipeline quality gates for `data-engineering` projects. Apply to every real pipeline; small learning projects can use a subset if the subset is chosen deliberately.

## Ingestion checklist
- [ ] Source identity/contracts known: APIs/DB tables/files, change semantics (append-only? mutable?), required permissions.
- [ ] Watermark/sync mechanism defined: CDC offset, incremental cursor, full-load cadence.
- [ ] Ingestion is idempotent: re-running a load does not duplicate rows (natural keys, MERGE/UPSERT, or delete-reinsert within a transaction).
- [ ] Backpressure/rate limits on sources respected; no hammering a shared prod API.
- [ ] Schema of incoming data validated early (type checks, required fields).
- [ ] Late-arriving or out-of-order source data handled (event time vs. processing time decision documented).
- [ ] CDC-specific: replica identity/keys set, snapshot phase behavior tested, Debezium resume works after restart.

## Schema checklist
- [ ] Storage layout decisions recorded: landing/raw zone (immutable), curated/warehouse zone.
- [ ] Types chosen explicitly (dates as DATE, not strings; decimals for money; UTC timestamps).
- [ ] Primary keys/dedup keys defined per table.
- [ ] Schema evolution policy: add-with-default tolerated, type change = deliberate breaking change.
- [ ] Partitioning/clustering aligned with the dominant query/filter pattern (usually date).
- [ ] Source-to-target field mapping documented (which weird source column feeds which target).
- [ ] Column naming convention consistent (snake_case or project standard everywhere).

## Transformation checklist
- [ ] Transformations declared/testable (dbt models/versioned SQL), not scattered scripts.
- [ ] Transformation logic idempotent and deterministic given the same inputs.
- [ ] Destination tables under version control with tests as store/table name.
- [ ] Aggregations have defined grain and time bounds; recompute semantics stated.
- [ ] Deleted rows in source: hard delete vs. soft delete decided (tombstones/late deletion windows).
- [ ] Slowly changing attributes handled (SCD or last-write-wins, explicitly chosen).

## Data-quality checklist
- [ ] Freshness check per pipeline stage (source → raw lag, raw → warehouse lag).
- [ ] Volume anomaly check: today's inbound row count vs. historical band.
- [ ] Schema check: unexpected/missing columns alert, don't silently pass.
- [ ] Null/ratio checks for critical fields; uniqueness on declared keys.
- [ ] Referential/entity checks where applicable (event's user exists).
- [ ] Predefined behavior on quality failure: block down-stream table publishing? Warn only? Decide, don't default.
- [ ] Quality summary visible somewhere (dashboard, scheduled report, or at minimum a log the team reads).

## Orchestration checklist
- [ ] DAG/task definitions in code (Airflow/Dagster/cron scripts), versioned, no clickpath deployment.
- [ ] Dependencies explicit; parallelism safe (no writers to the same table racing).
- [ ] Retries configured with backoff; failure alerting exists (not silent).
- [ ] Runtime/SLA expectations stated per task; late flagging for breaches.
- [ ] Credentials from a secret store/env, never hardcoded in DAGs.
- [ ] Local dev runnable via Docker Compose or equivalent; no hidden documented dependencies.

## Monitoring checklist
- [ ] Pipeline success/failure metrics recorded (runs, duration, retries).
- [ ] End-to-end lag visible (event time in source vs. availability downstream).
- [ ] Data volume trend visible and alertable.
- [ ] On-call/who-to-tell defined when a pipeline fails during the night.
- [ ] Incidents post-mortemed with a concrete pipeline/quality improvement recorded.

## Backfill and replay checklist
- [ ] Raw/immutable storage retained long enough to rebuild curated zones from scratch.
- [ ] Backfill procedure documented: how to trigger for a date range/entity, and where results land.
- [ ] Backfill is throttled (doesn't overwhelm source or swamp live ingestion).
- [ ] Replay of CDC/stream offsets tested at least once.
- [ ] Idempotency verified by actually running the same range twice somewhere first.
- [ ] Backfill progress measurable (rows processed), resumable if interrupted.
