---
description: Run a full product lifecycle pass over a feature or system - design, plan, build/verify, ship, operate, document, close - pausing at phase gates
argument-hint: "[what to run the lifecycle against, e.g. the search API, the indexing pipeline, the whole system]"
---

# product-to-production

This command is the lifted entry point to the `production-delivery` orchestrator skill, specialized for the car-part retrieval final-year project context.

## Steps

1. Read `skills/production-delivery/SKILL.md` — it owns phase sequencing, gate decisions, and the closure retro. Follow it exactly.
2. Read the phase-owner skills it delegates to as needed: `car-part-retrieval` (project + scope), `api-design`, `backend-testing`, `backend-code-review`, `backend-deployment`, `observability`, `documentation`, `applied-ai-delivery` (for model/provenance slices).
3. Read the checklists: `references/car-part-retrieval-checklist.md` and `references/backend-checklist.md`.
4. Use `$ARGUMENTS` as the deliverable target. If empty, ask for current state (stage, stack, existing evidence) before building the phase map. If the request belongs to the internship or paid job instead, stop and ask which context first.
5. Run the phases through `production-delivery`'s gates: **Design → Plan → Build → Verify → Ship → Validate (+1h/+24h/+48h) → Close retro**. Pause for user go/no-go at Design, Plan, and Ship — never chain Ship.
6. Label every artifact with its producing phase so the thesis and the system stay consistent; route retro lessons to `continuous-improvement`.
