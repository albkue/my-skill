# Backend Checklist

Production checklists for `backend-job` work. Pull the sections relevant to the change; don't pad with irrelevant items. Adapt to the team's actual conventions when known — these are defaults, assuming a Spring Boot / FastAPI / Go + PostgreSQL + Redis + Kafka + Docker shop.

## Security checklist
- [ ] Authentication applied to every endpoint; anonymous routes are exceptions, explicitly justified.
- [ ] Authorization checked on resources the user accesses (ownership/role), not just "a valid token".
- [ ] Input validation at the boundary (body, path, query, headers); reject early with clear errors.
- [ ] Output encoding / parameterized queries everywhere; no string-concatenated SQL.
- [ ] No secrets, tokens, internal URLs, or connection strings in code, logs, error responses, or repos.
- [ ] Dangerous endpoints (export, delete, admin) have rate limiting and audit logging.
- [ ] Sensitive data in logs is redacted; PII minimized in responses.
- [ ] Dependencies scanned / updated for known CVEs.
- [ ] Error responses leak no stack traces, SQL, or schema details.

## API checklist
- [ ] Resource names consistent (plural nouns, existing convention).
- [ ] Correct methods and status codes: 4xx client vs. 5xx server; no fake-200 errors.
- [ ] Pagination on all unbounded collections.
- [ ] Filtering/sorting explicitly allowed and validated (dataclasses/DTOs, whitelist).
- [ ] Standard error body shape documented.
- [ ] Idempotency for non-GET mutations where retries are plausible (`Idempotency-Key` or natural key).
- [ ] Rate limiting on expensive or public endpoints.
- [ ] Versioning strategy decided before the first breaking change.
- [ ] OpenAPI/docs updated in the same change.

## Database checklist
- [ ] Every new query column combination has an index (verify with `EXPLAIN ANALYZE` at prod-like volume).
- [ ] Migration tested on staging with production-like row counts; forward + rollback verified.
- [ ] Destructive migrations (drop, truncate, type change) are two-phase (expand → contract) across releases.
- [ ] Transactions are short; no external calls inside open transactions.
- [ ] Connection pool sized for real concurrency; no unbounded query growth per request.
- [ ] No N+1 patterns; batch operations for bulk work.
- [ ] Timezone/currency/precision types chosen deliberately, not defaulted.
- [ ] Backup exists and restore was tested before any risky change.

## Kafka checklist
- [ ] Message schema defined and versioned; consumers tolerate unknown fields.
- [ ] Key chosen deliberately for ordering/partitioning, not accidentally by null.
- [ ] Producer: idempotence/acks set correctly; retries with potential reorder accounted for.
- [ ] Consumer: processing time < `max.poll.interval.ms`; offsets committed only after processing.
- [ ] Idempotent handlers (duplicates are guaranteed, not theoretical).
- [ ] DLQ or retry-topic strategy defined; poison pills cannot loop forever.
- [ ] Consumer lag monitoring + alert on threshold.
- [ ] Replay story exists for historical disaster recovery / backfills.
- [ ] Graceful startup/shutdown handling that doesn't lose in-flight messages.

## Redis checklist
- [ ] Keys follow a naming convention (e.g., `entity:id:field`) with the ownership documented.
- [ ] Every cache entry has a TTL; no infinite caching of mutable data.
- [ ] Cache-invalidation strategy is explicit (write-through vs. short-TTL vs. event-driven).
- [ ] Stampede protection for hot keys (jittered TTL, lock, or request coalescing).
- [ ] Fallback behavior when Redis is down defined and tested (fail open? fail closed? DB direct?).
- [ ] Serialization format consistent for producers/consumers of keys.
- [ ] Eviction policy (`allkeys-lru` vs. `volatile-*`) matches how keys are used.
- [ ] Big keys/large values avoided; hot keys monitored.

## Testing checklist
- [ ] Happy path covered at the API/contract level, not only unit level.
- [ ] Validation, failure, and edge cases covered (including 4xx paths).
- [ ] Concurrency/idempotency cases for anything with "only once" expectations.
- [ ] Auth tests: no-token, wrong-user (403), admin-only.
- [ ] Tests run in CI and pass; no skipped/mostly-ignored tests shipped knowingly.
- [ ] Integration tests use real dependencies where risk matters (Testcontainers etc.).
- [ ] Test data factory/clean-up prevents cross-test coupling.

## Deployment checklist
- [ ] Change reviewed and approved by another engineer.
- [ ] All environments' config accounted for (new env vars, secrets in the store, toggles).
- [ ] Migrations deployed/tested before the app code that depends on them.
- [ ] Backward compatibility verified (old version survives during rolling deployment).
- [ ] Rollback tested or at minimum rehearsed mentally: artifact, data reversibility, feature toggle.
- [ ] Health checks pass post-deploy; smoke test of the critical path executed.
- [ ] Monitoring/alerts exist for the feature's own failure modes before rollout starts.
- [ ] Deployment in a safe window; team informed; change recorded.
- [ ] Post-deploy watch period assigned (first 24–48h).
