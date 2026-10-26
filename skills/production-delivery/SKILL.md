---
name: production-delivery
description: Own one deliverable from idea to verified production - acceptance criteria, sliced plan, build with per-slice tests and review, deploy, post-launch validation (+1h/+24h/+48h), and a closure retro. Use when the user says "ship X", "take this to production", "deliver this end to end", or when the product-to-production command needs a phase orchestrator. Do NOT use to replace the individual craft skills (api-design, backend-testing, backend-code-review, backend-deployment, documentation) - this skill orchestrates and sequences them, it does not do their work itself.
version: 1.0.0
author: Sothy Eng
---

# Production Delivery

## Purpose
Be the accountable spine of one deliverable: nothing ships as a pile of good intentions. This skill sequences the craft skills behind phase gates — plan → build → verify → ship → validate → retro — so that each phase has an owner, an output, and an exit criterion.

## When to use
- "Ship X" / "take this to production" / "deliver this end to end" / "I need this live by Y".
- An existing deliverable stalled mid-way: recover the state and continue from the right phase.
- `/my-skill:product-to-production` — this skill is the orchestrator behind it.

## When not to use
- Doing the craft inside a phase (designing an API, writing tests, reviewing code) — delegate per phase and stay in the orchestrator seat.
- ML-experiment delivery specifically → `applied-ai-delivery`.
- Single-skill tasks that don't need sequencing (one review, one debug) → the craft skill directly.

## Context intake
- The deliverable, its owner, deadline, and where it currently stands (map existing artifacts to phases: nothing / plan / partially built / built / deployed / validated).
- Which phases are already complete (reuse evidence; never redo silently).
- Constraints from `docs/workflow-profile.md`: team release process, environments, deployment target.

## Workflow
1. Read `docs/workflow-profile.md` + intake.
2. **Phase map:** table of phases — Phase 1 Design, Phase 2 Plan, 3 Build, 4 Verify, 5 Ship, 6 Validate, 7 Close — each with owner skill, inputs, and exit criterion. Mark what already exists and with what evidence.
3. For each incomplete phase in order:
   - Run the phase's owner skill (`api-design` for contracts, `backend-deployment` for release planning, etc.). **You sequence, they craft.**
   - Collect the phase output and check it against the exit criterion.
   - **Pause after each risky phase** (Design, Plan, Ship) and ask the user for a go/no-go — never chain Ship without approval.
4. Phase gates and owners:
   - **Design** — owner `api-design` (+ `car-part-retrieval` if ML system). Exit: contract or architecture agreed by user.
   - **Plan** — owner: slices created here. Exit: slices with acceptance criteria, correct dependency order, no slice missing craft-skill coverage.
   - **Build** — owner `backend-testing`, `backend-code-review`, `documentation`. Exit: each slice lands with tests + review + docs notes.
   - **Verify** — exit criteria: tests pass, review verdicts addressed, no unresolved `[TO VERIFY]` markers.
   - **Ship** — owner `backend-deployment`. Exit: deploy checklist + rollback executed or artifact ready.
   - **Validate** — owner `backend-deployment`'s +1h/+24h/+48h checkpoints + `observability` for new alerts/dashboards. Exit: validation checklist concluded.
   - **Close** — retro scheduled.
5. **Closure retro:** what shipped, what differed from the plan, what rework happened, and which lessons go into the plugin via `continuous-improvement`.
6. Maintain a running **delivery status block** the user can ask for at any time ("where are we?").

## Adaptation rules
- ML/CV deliverables: Slots 3–4 remain craft (tests + review) with `applied-ai-delivery` owning the model/provenance slice; Ship phase becomes deploy + demo path validation.
- Internship/team context: adopt the team's own release handshake when the profile documents one; phase structure maps onto it instead of overriding it.
- Grand-scale work (weekend project): phases compress but gates and the retro never disappear — Ship still pauses, retro still writes.
- Deadline pressure: cut scope, not the Verify or Phase 7 gates.

## Inputs needed
- Deliverable description + deadline + current state (or existing artifacts).
- Team release process details (or the captured *Team conventions* in the profile).
- Approval authority confirmed per phase gate.

## Output contract
1. **Phase map** — phases, owner skills, exit criteria, evidence for completed ones.
2. **Delivery status block** (living) — current phase, what's done, what's next, blockers.
3. **Phase outputs** — each phase's craft output attached to the map.
4. **Gate decisions** — explicit user go/no-go records at Design/Plan/Ship.
5. **Closure retro** — shipped state vs plan; rework causes; lesson candidates with suggested `SKILL.md` targets.

## Rules and constraints
- Never silently redo a phase that has recorded evidence — flag the delta first.
- Ship never chains automatically: a phase gate pause is mandatory even under deadline.
- Craft decisions (contract shape, model design, test depth) stay with the owner skills; the orchestrator records, does not redesign.
- Retro conclusions target `skills/<skill>` edits only through `continuous-improvement` (proposed diffs, human-approved).
- No private data in any status block or deliverable artifact.

## Quality checklist
- [ ] Phase map exists with owners + exit criteria before any work starts.
- [ ] Each phase's output verified against its exit criterion.
- [ ] User gate decisions recorded at Design/Plan/Ship (never auto-chained).
- [ ] Delivery status block is current at any time it is asked for.
- [ ] Closure retro produced, with lesson candidates routed to `continuous-improvement`.
- [ ] Craft quality (tests, review verdicts, docs) delegated out, not improvised.

## Lessons learned

Record improvements after real usage (maintained via `continuous-improvement`). Format:

- `<date>` — `<what happened>` → `<change made to this SKILL.md>`

(empty — entries appear after real usage)

## Examples
1. **Request:** "Ship the search API before my defense — two weeks."
   **Behavior:** Phase map (Design via `api-design`; Plan → 4 slices; Build/Verify via `backend-testing`/`backend-code-review`; Ship via `backend-deployment`; Validate +1h/+24h/+48h; Close retro). Pause after Design and Plan gates; live status block; retro at the end with lesson candidates.
2. **Request:** "We built it last month but never validated — where are we?"
   **Behavior:** Phase map with evidence (build/ship evidence found); resume at *Validate* phase (`backend-deployment`'s checkpoints + `observability` gap check), then close with recovery retro noting what surprised the plan.
