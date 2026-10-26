# AGENTS.md

You are working with the **my_skill** plugin — a self-improving personal engineering
workflow plugin (20 skills, 10 slash commands) originally built for Claude Code, but
usable by any agent that can read markdown files.

Version: 1.6.0 · License: MIT · Author: Sothy Eng ([albkue](https://github.com/albkue))

## Universal rule: read the workflow profile first

**Before starting any engineering task, read [`docs/workflow-profile.md`](docs/workflow-profile.md).**
It defines the user's current roles, projects, tech stacks, and priorities. Every
skill assumes it has been read. If the profile is missing, contradicts the request,
or looks stale (>3 months), confirm or correct it with the user before applying any
role, project, or stack assumptions.

## How to find and load a skill

Open [`README.md`](README.md) → **Skill catalog** table, or list folders in
`skills/`. Each skill lives at `skills/<skill-name>/SKILL.md` and is self-contained
plain markdown.

1. Match the user's request against the skill descriptions below.
2. Read the matched skill's `SKILL.md` **in full** and follow it exactly.
3. If two skills match, the more specific one wins; if genuinely ambiguous,
   ask one clarifying question.
4. Deep-reference material is on demand, never preloaded: `references/*.md`
   (production checklists, question bank), `examples/*.md` (worked requests).
5. If nothing matches: do the task normally, then note the gap
   (see "Improvement loop" below).

## When to which skill (short index)

| Trigger in the request | Load `skills/<name>/SKILL.md` |
|---|---|
| Paid backend work: Spring/FastAPI/Java/Python, Kafka, Redis, Postgres, APIs, Docker | `backend-job` |
| Implementing a feature assigned by an internship team | `software-internship` |
| Designing new endpoints / REST contracts, pagination, versioning, OpenAPI | `api-design` |
| Reviewing an API contract quality (even "is this endpoint right?") | `api-design` |
| Debugging failing backend systems: HTTP/DB/Kafka/Redis errors, latency, deploys | `backend-debugging` |
| Code review of PRs/diffs/services (verdicts + issue lists, not rewrites) | `backend-code-review` |
| Security review of the same: auth, BOLA/IDOR, SSRF, injection, hardening | `backend-code-review` |
| Writing unit/integration/Kafka/API/DB/contract tests, planning test coverage | `backend-testing` |
| Release planning: Docker, CI/CD, blue-green/canary/rolling, rollback, incident prep | `backend-deployment` |
| Post-ship monitoring: logs, metrics, SLOs, runbooks, alert design | `observability` |
| Writing READMEs, ADRs, API docs, setup guides grounded in real code | `documentation` |
| Delivering a feature with tests and review or end-to-end "ship X" | `production-delivery` |
| ML/CV experiment → usable, defensible artifact (provenance, `[REP]` labels) | `applied-ai-delivery` |
| Car-part image retrieval thesis: YOLOv8, CLIP, FAISS/HNSW, CBIR pipeline design + code | `car-part-retrieval` |
| Structuring, drafting, editing the thesis document itself | `thesis-helper` |
| Kafka, CDC, Debezium, Airflow, dbt, warehouses, lakehouses (as a learning domain) | `data-engineering` |
| Weekly/monthly study plans, milestones, small projects, what to learn next | `learning-roadmap` |
| Mock interviews, STAR practice, resume/portfolio feedback, technical Q&A | `interview-prep` |
| Read-only plugin quality audit (0–10 scores, overlap, vague triggers) | `skill-health-check` |
| Professional messages to the internship team: standups, blockers, PR notes | `internship-communication` |
| Retros / feedback → SKILL.md edits (gated self-improvement) | `continuous-improvement` |
| Profile drift: "my job changed", "we moved to X", role/stack/priority updates | `workflow-adapter` |

⚠️ **Hard routing rule:** `backend-job` (paid work) and `software-internship`
(internship) are separate contexts and never mix. If a request could belong to
either and context is unstated, ask: *"Is this for your backend part-time job or
your software developer internship?"* before doing anything.

## Improvement loop (what makes this plugin self-improving)

- After a real task that used a skill, the user may ask to "review how the plugin
  handled the last task" → follow `skills/continuous-improvement/SKILL.md`: compare
  request vs output, gather 2–4 feedback points, propose a **before/after diff** of
  the affected `SKILL.md`, and apply **only after approval**. Never rewrite, rename,
  split, or delete skills autonomously.
- Periodic audits → `skills/skill-health-check/SKILL.md` (read-only; reports scores
  and recommendations; edits are delegated to `continuous-improvement`).
- Workflow-profile reality changes → `skills/workflow-adapter/SKILL.md`
  (drift table → approved diff; SKILL.md edits stay out of its reach).
- Real-usage lessons land in `docs/lessons-learned.md`.

## Output conventions

- Skills define a numbered **Output contract** — deliver every section it names.
- Fabricated numbers, citations, or "presented-as-real" unverified results are
  hard errors. Mark unverifiable items `[TO VERIFY]` / `[REP: …]`.
- No secrets, real company names, internal URLs, or client data in any output or
  file edit.
