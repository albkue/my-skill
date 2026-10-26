# Example: software-internship

## Request
> "I received an internship task to add pagination to an API. Help me plan and implement it."

Payload provided by the plugin:

## What the plugin does

**Route:** `software-internship` — but the routing rule fires first:

> "Is this for your backend part-time job or your software developer internship?"

Sothy confirms: internship.

**Output**

**Task understanding:** Add pagination to the internship team's `GET /orders` listing endpoint. Assumption to verify: team prefers page/size params (many Java shops do) or cursor; no spec was given.

**Implementation plan**
1. Find the current endpoint and how the list query is built (Spring Data repository? MyBatis? JPA?). Read tests to learn conventions.
2. Pick the pagination convention the codebase already uses elsewhere (check other list endpoints — copying an existing pattern is the safest move).
3. Add pagination params + validation (default `page=0`, `size=20`, max size).
4. Return the list in a documented envelope with counts and page navigation.
5. Tests: page/size validation, filtering composes with pagination, `size=0` rejected.
6. Update the endpoint docs and team wiki, if it exists.

**Code changes:** per-step snippets matching Spring Data's `Pageable`, consistent with what Sothy pastes from the repository (the skill asks for the existing controller/repository code first — nothing invented).

**Tests:** JUnit5 defaults matching the repo's test layout.

**PR description (paste-ready):**
> **Add pagination to GET /orders**
> - Adds `page`/`size` params (default 20, max 100) to the orders list, using the same response envelope as `/invoices` per team convention.
> - Adds validation + tests for invalid size and out-of-range pages.
> - Screenshots: list page at default, filtered, page 3.

**Questions for supervisor (only if unanswered by the repo):**
- "Is page/size enough, or do we want cursor pagination for this table going forward?"
- "Should the count query stay, for the total-pages display, or is 'next page exists' cheaper for us?"

**Guardrails applied:** no assumption of repo access — asks Sothy to paste the controller; suggests reading conventions before coding; flags anything about a destructive operation or DB migration as needing a second opinion.
