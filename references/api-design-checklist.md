# API Design Checklist

Default contract standards for `api-design`. Use team/company conventions where they exist and differ.

## Resource naming
- [ ] Nouns in plural for collections: `/orders`, `/order-items`.
- [ ] Nested resources reflect real ownership, max 2 levels deep: `/users/{id}/orders`.
- [ ] No verbs in paths (use methods); exceptions for deliberate domain actions (`/orders/{id}/cancel` assumed as sub-resource or POST action when justified).
- [ ] Kebab-case paths; camelCase JSON fields (or the project's existing convention).
- [ ] No internal/database vocabulary leaking into the contract (`/accounts`, not `/tbl_accounts/crud`).

## HTTP methods
- [ ] GET: safe, no side effects; POST: create or non-idempotent actions; PUT/PATCH: update (full/partial); DELETE: remove.
- [ ] POST for any operation that doesn't fit CRUD cleanly, with the intent in the path (`/payments`, not `/doPayment`).
- [ ] No GETs that mutate state.

## Status codes
- [ ] 200 success / 201 + `Location` on create / 204 on delete or empty update.
- [ ] 400 validation, 401 unauthenticated, 403 unauthorized, 404 not found or deliberately hidden, 409 conflict, 422 semantic validation, 429 rate-limited.
- [ ] 500 reserved for server faults; specific client problems never map to 500.
- [ ] No 200-with-error-body pattern.

## Pagination
- [ ] All list endpoints paginated; no unbounded lists.
- [ ] Cursor-based for large/mobile-fed sets, offset acceptable for small admin sets.
- [ ] Response envelope exposes cursors/next pages; max page size enforced with defaults.

## Filtering
- [ ] Whitelisted filter fields; unknown filter params rejected or ignored (decide, then document).
- [ ] Sorting via `sort=field,-other`; validated against allowed fields.
- [ ] Filtering composes with pagination predictably.

## Errors
- [ ] Consistent error envelope (`code`, `message`, `details`, optional traceId).
- [ ] Validation errors are field-level, not one blob.
- [ ] Internal details (stack traces, SQL, table names) never exposed; traceId included for support.
- [ ] Error codes documented for consumers.

## Authentication
- [ ] Scheme stated (Bearer/OAuth2/API-key) and consistent.
- [ ] 401 vs. 403 semantics applied correctly.
- [ ] Token scopes/roles defined per endpoint where relevant.
- [ ] Public endpoints identified deliberately, not accidentally.

## Versioning
- [ ] Version decided up front (`/v1/`, header, or content negotiation) — not required on day one, but the change mechanism must be known.
- [ ] Breaking changes flagged: removed fields, renamed fields, changed types/status codes, pagination semantics.
- [ ] Additive changes preferred; deprecation policy communicated ("new field appears before old field is removed").

## Idempotency
- [ ] Non-GET mutations safe to retry (`Idempotency-Key`, natural dedupe key, or upsert semantics).
- [ ] Duplicate-submission behavior defined (409 vs. same-result) and documented.
- [ ] Webhooks/callbacks (if any) replay-tolerant: idempotent receiver side assumed.
