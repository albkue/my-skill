---
name: applied-ai-delivery
description: Deliver an applied ML/CV feature end to end with evaluation discipline - baseline first, leakage-safe splits, seeded configs, and provenance-tracked results on the way to a usable, deployable, or written-up deliverable. Use when the task is "take this model/experiment to something usable", "make the demo real", "package and hand over the model", or any request to turn an ML idea into a delivered artifact. Do NOT use for designing the retrieval pipeline itself (car-part-retrieval), for building data pipelines/infrastructure (data-engineering), for pure learning plans (learning-roadmap), or for academic writing (thesis-helper).
version: 1.0.0
author: Sothy Eng
---

# Applied AI Delivery

## Purpose
Own the *delivery* of an applied ML/CV result: from a promising experiment to an artifact someone else can run, evaluate, or read with confidence. The craft of the model belongs to domain skills; this skill ensures the result survives contact with real users — with an evaluation protocol and result provenance that make the numbers defensible.

## When to use
- "Take this model/experiment to something usable / deployable / written up."
- "Make the demo a real deliverable" (API wrapper, CLI, notebook-to-script, packaging).
- Preparing a handover: README for the model, evaluation report, reproducibility instructions.
- Turning ad-hoc notebooks into a reproducible experiment protocol.

## When not to use
- Designing the CV retrieval system itself (layers, embeddings, indexes) → `car-part-retrieval`.
- Building the data pipeline/infrastructure around it → `data-engineering`.
- Writing thesis chapters or academic prose → `thesis-helper`.
- Pure mock-interviews/study plans → `interview-prep` / `learning-roadmap`.

## Context intake
- Deliverable target: demo, API endpoint, CLI, model handover (README + artifacts), evaluation report, thesis-section support?
- What evidence already exists (numbers, artifacts, configs) and — critically — how each number was produced?
- Serving constraints: target latency/throughput, hardware (GPU availability), batch vs online.

## Workflow
1. Read `docs/workflow-profile.md` and `docs/active-context.md`; confirm the project stack and serving constraints, and apply the active context's rules (its rules live in the profile's Contexts section).
2. Write the **experiment charter**: deliverable + acceptance criteria ("correct artifacts, seeded reruns within tolerance, latency X on hardware Y") + named risks.
3. Verify evaluation hygiene before any delivery work: a baseline exists, splits are leakage-safe, configs seeded, and a minimal rerun command works. If absent, doing this first is step zero.
4. **Provenance audit**: list every number/artifact claimed; map each to its generating run/config; label any unverifiable number `[REP: rerun before claim]` — never present it as real.
5. Deliver in slices, each with a runnable artifact:
   - **Pack:** wrapper (CLI/API), minimal README, run + eval instructions, artifact list with hashes.
   - **Defend:** evaluation report — protocol first, then results with provenance, then limitations.
   - **Hand over:** a stranger's success path ("clone → install → rerun eval → read report").
6. Route craft work out: model/embedding design → `car-part-retrieval`; serving/API contract → `api-design` + `backend-*`; pipeline infra → `data-engineering`.
7. End each slice with a checkpoint: what runs now, what is claimed with provenance, what is next.

## Adaptation rules
- Academic deliverable (thesis section/report): provenance rules stricten — every number needs a rerunnable source and `[REP]` labels; wording support routes to `thesis-helper` afterward.
- Demo/marketing deliverable: latency and UX matter more than marginal accuracy; provenance still applies to claimed numbers.
- Model handover to a team: strengthen the README-with-repro path; artifact hashes + environment spec become mandatory.
- No GPU: prefer small-model, distance-metric-first delivery; inference-time trade-offs stated in the charter.

## Inputs needed
- Existing artifacts, experiment configs, and any claimed numbers with their sources.
- Target deliverable type + acceptance criteria + serving constraints.
- A path where current eval reruns can execute.

## Output contract
1. **Experiment charter** — deliverable, acceptance criteria, risks (short).
2. **Evaluation hygiene check** — baseline/split/seed status; found gaps listed as actions.
3. **Provenance table** — claim → source run → status (verified / `[REP]`).
4. **Slice deliverables** — runnable artifacts with run commands and file lists.
5. **Processed-in-order handover doc** — stranger's success path.
6. **Next checkpoint** — what runs now, what is proven, next step.

## Rules and constraints
- Hard rule: no unproven number is presented as a result; `[REP: ...]` markers for anything not yet rerun-verified.
- Never promise accuracy/latency under test conditions only — always state the run environment.
- Do not invent dataset/artifact sources; if unknown, mark `[TO VERIFY]`.
- Pack artifacts minimally: no secrets, no client data inside model/config artifacts.
- Craft belongs to domain skills; this skill never redesigns the model.

## Quality checklist
- [ ] Charter has measurable acceptance criteria.
- [ ] Baseline, splits, and seeds verified (or gap-fix listed before delivery).
- [ ] Every claimed number has provenance or an explicit `[REP]` label.
- [ ] Slice deliverable runs from a stranger's path (instructive commands).
- [ ] Limitations section included in the evaluation report.
- [ ] Next checkpoint named.

## Lessons learned

Record improvements after real usage (maintained via `continuous-improvement`). Format:

- `<date>` — `<what happened>` → `<change made to this SKILL.md>`

(empty — entries appear after real usage)

## Examples
1. **Request:** "I have a CLIP fine-tune notebook with 0.83 recall@10 — package it so my team can reuse it."
   **Behavior:** Charter (team-run artifact, rerun eval under tolerance); provenance audit of the 0.83 (config recorded? seeded? `[REP]` until rerun); pack: CLI wrapper + README + artifacts with hashes; evaluation report with protocol; handover success path.
2. **Request:** "Make the demo real for my defense — I need a search API plus a results write-up."
   **Behavior:** Charter; hygiene check (baseline + split provenance); deliver API slice (routes to `api-design` for the contract, `backend-testing` for tests); write-up slice routes wording to `thesis-helper` with provenance table carried over; +1h/+24h post-launch validation handled by `backend-deployment`/`production-delivery`.
