---
name: learning-roadmap
description: Create realistic study and project roadmaps for Sothy Eng. Use when asked for weekly or monthly study plans, roadmaps for backend engineering, data engineering, MLOps, system design, computer vision, or interview preparation, small project ideas with milestones, or help deciding what to learn next. Do NOT use for teaching a specific concept (data-engineering, backend-job, car-part-retrieval by topic) or interview Q&A practice (interview-prep).
version: 1.0.0
author: Sothy Eng
---

# Learning Roadmap

## Purpose
Turn vague ambitions ("learn data engineering", "get better at system design") into realistic weekly plans that fit Sothy's actual schedule: a part-time backend job, an internship, and a thesis simultaneously. Plans must survive busy weeks without collapsing.

## When to use
- "Help me plan X" — weekly or monthly plans for backend, data engineering, MLOps, system design, computer vision, or interviews.
- Deciding what to learn next given everything already in flight.
- Scoping small practice projects tied to learning goals.
- Re-planning after a stalled stretch (transparently cutting scope, not rescheduling everything).

## When not to use
- Teaching the content itself → route to the topical skill (`data-engineering`, `backend-job`, `car-part-retrieval`, `api-design`, `thesis-helper`).
- Practicing interview answers → `interview-prep` (but an interview-prep phase belongs inside an interview roadmap).
- Internship deliverables or backend-job deadlines → those are obligations, not learning plans; reflect them as constraints here.

## Context intake
- Available hours, deadline, current level, and learning style; read active commitments from `docs/workflow-profile.md` and ask only for what it lacks.
Detect or confirm before starting (ask at most what is genuinely needed):
- Which context: part-time paid backend work, internship, thesis / final-year project, personal project, or learning? Fall back to the active roles and projects in `docs/workflow-profile.md`; ask when it could be two different contexts.
- What is the desired output: a plan, code, a review, tests, documentation, a deployment plan, or research notes? Confirm if ambiguous.

## Workflow
1. Read the my-skill plugin's `docs/workflow-profile.md`. If it is missing, contradicts this request, or was last updated more than ~3 months ago, confirm or update it with Sothy before applying any role, project, or stack assumptions.
2. Ask for available hours/week, deadline, current level, and learning style if not stated.
3. Define ONE measurable outcome for the plan — not three ("implement a CDC pipeline end-to-end", not "learn Kafka, Spark, and Airflow").
4. Confirm the plan must fit around job + internship + thesis; budget realistic hours and reserve a slack buffer.
5. Break the outcome into weekly milestones; each week has: learning topics, one hands-on task, a deliverable, resources (free/low-cost), and success criteria.
6. Schedule heavier weeks early in the plan; front-load setup friction so later weeks are the payoff.
7. Add a weekly review checkpoint (15 min): what shipped, what slipped, what's cut.
8. Include at least one small project with checkboxes so progress is visible.
9. State clearly what is deliberately excluded — a roadmap that doesn't cut scope fails silently.

## Adaptation rules

- ONE measurable outcome per plan, always; hours come from the profile, not assumptions.
- Plans re-plan around whatever is currently in flight (job, internship, thesis, new roles) - the structure survives context changes.
- Hands-on project themes align with the profile's active roles so learning compounds.

## Inputs needed
- Available hours per week (real number, including bad weeks).
- Deadline or target date (job switch, exam, graduation, interview).
- Current level and known gaps.
- Preferred learning style for retention (project-first, video-first, book-first).
- Existing commitments: backend job, internship hours, thesis milestones.

## Output contract
- **Objective** — single measurable outcome.
- **Duration** — weeks + total hours available.
- **Weekly plan table** — week | topics | hands-on task | deliverable | success criteria.
- **Deliverables** — list of concrete artifacts by end.
- **Practice project** — scoped small end-to-end project with milestones.
- **Review checklist** — weekly self-review questions.
- **What's excluded** — explicitly cut topics and why.

## Rules and constraints
- Prioritize practical implementation over passive tutorials; every week produces an artifact.
- Prefer free or low-cost resources (official docs, Dockerized repos, open courses) unless Sothy asks for paid options; never invent courses/books — recommend only verifiable well-known ones or link-free guidance.
- Align topics with his backend job, internship, thesis, and data-engineering interests; cross-pollinate (e.g., CDC learning uses Postgres, which he already knows).
- Avoid overload: if hours are tight, shrink the objective, don't cram.
- Plans are hypotheses: include a mid-point checkpoint decision (continue / cut / swap).

## Quality checklist

- [ ] ONE measurable objective sized around real hours.
- [ ] Weekly deliverables + review checkpoint included.
- [ ] Exclusions stated explicitly.
- [ ] Slack buffer + mid-point continue/cut/swap decision present.

## Examples
1. **Request:** "I want a 6-week plan; I can do ~7 h/week; goal is basic streaming data engineering with Kafka."
   **Behavior:** Objective = "build an event pipeline: Kafka producer → consumer → Postgres + dashboard". Six weekly rows (Docker Compose setup; core Kafka concepts; local producer app; consumer group; Postgres sink + freshness checks; review + demo write-ups), deliverable list, review checklist, exclusions ("no Debezium/Spark in this plan"), slack buffer for the thesis.
2. **Request:** "Am I spreading myself too thin?"
   **Behavior:** Ask for current commitments/hours; show the arithmetic honestly (job + internship leave X); recommend ONE track to keep active until the next review, a date to defer others to, and a cut decision; output format applied compactly.

## Lessons learned

Record improvements after real usage (maintained via ``continuous-improvement``). Format:

- ``<date>`` -- ``<what happened>`` -> ``<change made to this SKILL.md>``

(empty -- entries appear after real usage)
