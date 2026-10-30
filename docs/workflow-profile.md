# Workflow profile — Sothy Eng

> Every my-skill skill reads this file before starting. If it is missing, contradicts the
> request, or `Last updated` is more than ~3 months old, the agent asks you to confirm or
> update it instead of assuming. Update it whenever a role, project, stack, or priority
> changes — the plugin adapts from this file, so keeping it current is the whole mechanism.
> Last full review: `/my-skill:skill-health-check`.

Last updated: 2026-10-26

## Current roles
- Backend Developer (part-time job)
- Software Developer intern
- Final-year student — Data Science & Engineering

## Active projects
- **Part-time job:** production backend services (Spring Boot, PostgreSQL, Redis, Kafka).
- **Internship:** assigned feature/bug work in the internship team's codebase.
- **Final-year project:** intelligent car-part image retrieval system (thesis in progress).

## Main tech stacks
- Backend: Java/Spring Boot, Python/FastAPI, Go; PostgreSQL, Redis, Kafka, Docker.
- Data: Debezium/CDC, dbt, Airflow (learning track).
- CV/ML: Python, CLIP-style/CNN embeddings, FAISS / pgvector.

## Team conventions
- Job: [add branch naming, PR rules, deploy process here when relevant]
- Internship: [add; unknown requests should surface as supervisor questions, not guesses]

## Deployment environment
- Job: [staging → production; add specifics as they become relevant]
- Final-year project: dev machine, GPU optional, free/open tools only.

## Contexts

(Optional per context: a `- Defer to: skill-a, skill-b` line. The dispatcher prefers those skills for matching requests while still applying the context's rules.)

Each `###` heading is a context id usable with `/my-skill:today <id>`. Add, rename, or delete
contexts freely (then run `/my-skill:workflow-adapter`). Rules apply on top of each skill's
own rules while that context is active.

### job
- Paid production system: no deploy, migration, destructive SQL, or config change without an explicit rollback plan and a confirmation step.
- Never paste secrets, internal URLs, or customer data into outputs, docs, or the vault.
- Reviews and tests are required before any "ready to ship" claim.

### internship
- Unknown conventions or requirements become a question for the supervisor, not a guess.
- Keep work scoped to the assigned ticket; draft the supervisor update alongside the work.
- Never reuse job code, configs, or data in internship outputs.

### thesis
- Results need provenance (seed, config, dataset version, commit); mark unreproducible numbers `[REP]`.
- Write outputs to the vault folder `01-Thesis\` per the project CLAUDE.md and log the sync.
- Claims in thesis text must trace to a logged experiment or a cited source.

### learning
- Teach before building; small runnable examples; no production-safety ceremony.

## Current priorities
1. Final-year project: build + evaluate the retrieval pipeline, write the thesis.
2. Job work shipped safely (correctness, reviews, controlled deploys).
3. Internship tasks delivered on time.
4. Data engineering practice in spare hours.

## Completed / paused workflows
- (none yet — move finished roles/projects/interests here with a date, and the skills
  will stop routing to them as active context)

## Maintenance notes
- After changing anything above, say: **"My workflow changed; update the relevant skills."**
  (`continuous-improvement` will propose exact SKILL.md edits and show diffs first.)
- Run `skill-health-check` monthly to check the inventory still matches the profile.
