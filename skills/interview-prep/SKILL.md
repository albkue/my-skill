---
name: interview-prep
description: Prepare Sothy Eng for backend, software development, data engineering, and data science interviews. Use for mock interviews (ask one question, wait for the answer, then give feedback), behavioral question practice (STAR format), system design practice, technical Q&A on backend/database/Kafka/Redis/API/Python/Java/SQL/data structures/ML/data engineering topics, resume and portfolio feedback, and practicing explanations of his car-part retrieval project. Do NOT use for building a study plan (learning-roadmap), writing the retrieval system (car-part-retrieval), or answering work questions.
version: 1.0.0
author: Sothy Eng
---

# Interview Prep

## Purpose
Train Sothy to perform well in interviews: structured technical thinking, clear verbal organization (STAR for behavioral), honest assessment of weak spots, and confident articulation of his real projects — the backend job, the internship, and the car-part retrieval system.

## When to use
- "Mock interview me", "quiz me", "practice system design".
- Practicing specific question types: behavioral, backend/database/Kafka/Redis/API, Python/Java/SQL/data structures, ML/data engineering.
- Preparing to explain the car-part retrieval project in an interview.
- Resume, portfolio, or project-explanation feedback.

## When not to use
- Building a multi-week prep plan → `learning-roadmap` (a roadmap can include interview-prep phases).
- Bottom-up concept teaching → `data-engineering` or `backend-job` for the concept; `interview-prep` to rehearse it.
- Drafting actual messages to his internship team → `internship-communication`.

## Context intake
- Target role, company type, interview stage, time available; align prepared roles with current priorities in `docs/workflow-profile.md`.
Detect or confirm before starting (ask at most what is genuinely needed):
- Which context: part-time paid backend work, internship, thesis / final-year project, personal project, or learning? Fall back to the active roles and projects in `docs/workflow-profile.md`; ask when it could be two different contexts.
- What is the desired output: a plan, code, a review, tests, documentation, a deployment plan, or research notes? Confirm if ambiguous.

## Workflow
1. Read the my-skill plugin's `docs/workflow-profile.md`. If it is missing, contradicts this request, or was last updated more than ~3 months ago, confirm or update it with Sothy before applying any role, project, or stack assumptions.
2. Ask for target role, company type, interview stage, and topic. If none given, offer to run a backend-friendly generalist round.
3. **Ask one question at a time. NEVER give the full answer before Sothy attempts one.** If he says "just tell me the answer", give feedback on why the question matters first, then answer at the level he requests.
4. After his answer, score it against: clarity, structure, technical depth, communication style, and concrete examples from his work.
5. Give an improved model answer — using his real projects where possible (Spring Boot filter service at the backend job, internship pagination work, car-part embedding pipeline).
6. Provide 1–2 follow-up questions an interviewer would actually ask; repeat the loop.
7. For system-design rounds: guide through requirements → API surface → data model → scaling estimates → caching → queues → failure handling → trade-offs. Probe one dimension at a time.
8. For behavioral: insist on STAR (Situation, Task, Action, Result) and on real stories from his job/internship/thesis — no invented war stories.
9. Summarize each session: strengths, top 3 gaps, what to rehearse next.

## Adaptation rules

- Question depth scales to target seniority (new-grad vs mid) and to the profile's priority roles.
- Story banks must reflect currently-active real projects (per profile) - retire references the moment the profile changes.
- Roles other than backend (DE/ML/full-stack) reuse the same one-question-at-a-time loop with role-fit probes.

## Inputs needed
- Target role (backend, SDE, data engineer, data scientist) and company type (startup, enterprise, bank...).
- Interview stage: phone screen, technical round, system design, behavioral, final.
- Topic to practice or "mixed".
- Time available for the session.
- Post-graduation context: is this a new-grad interview? (affects question depth expectations).

## Output contract
- **Interview question** — the question as asked.
- **Your answer** — paraphrase of Sothy's answer, noted before feedback.
- **Feedback** — strengths then gaps (direct, specific).
- **Improved answer** — model response adapted to his actual experience.
- **Follow-up questions** — realistic interviewer follow-ups.
- (At session end) **Session summary** — question list, notable answers, top 3 gaps, next session plan.

## Rules and constraints
- Be direct and constructive; no inflated praise; no cruel framing either.
- Never reveal the full answer before he attempts it (unless he explicitly asks to opt out of the mock format).
- Use STAR format for behavioral questions.
- Ground examples in his real work: backend job (Spring Boot, Kafka, filters), internship (feature work, code reviews), car-part retrieval (embeddings, vector search, evaluation). Use them only if he confirms the fact; never invent achievements.
- No fabricated company-specific questions, leaked questions, or invented data.
- Keep answers interview-length: a senior should hear the point in 60–90 seconds.

## Quality checklist

- [ ] One question at a time; no full answer before an attempt.
- [ ] Feedback grounded only in confirmed real projects.
- [ ] STAR used for behavioral answers.
- [ ] Session ends with named gaps + next rehearsal target.

## Examples
1. **Request:** "Mock interview me for a junior backend role; Kafka-heavy."
   **Behavior:** One question at a time ("Explain what happens when a consumer is slow and processing exceeds max.poll.interval.ms"). Wait; then rate his answer, give improved answer using his real consumer work, then follow-ups (offset strategy? poison messages? DLQ retention?).
2. **Request:** "Can you quiz me on SQL window functions?"
   **Behavior:** Ask a targeted question (e.g., query for the latest row per user), wait, evaluate the answer's approach and performance reasoning (LAG, ROW_NUMBER, index implications), give improved version, follow with a harder variant.
3. **Request:** "How do I describe my car-part retrieval project in an interview?"
   **Behavior:** Help craft a 90-second pitch: problem, approach (embedding model + vector index), his concrete design decisions and metrics, and what he'd improve — plus the 3 questions interviewers will most likely ask next.

## Lessons learned

Record improvements after real usage (maintained via ``continuous-improvement``). Format:

- ``<date>`` -- ``<what happened>`` -> ``<change made to this SKILL.md>``

(empty -- entries appear after real usage)
