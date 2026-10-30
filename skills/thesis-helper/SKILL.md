---
name: thesis-helper
description: Help Sothy Eng plan, structure, and improve his final-year thesis on intelligent car-part image retrieval. Use for research questions/objectives/scope, methodology and timeline planning, literature review organization, system architecture and diagrams, experiment design and result presentation, thesis chapters (abstract/introduction/methodology/results/conclusion), improving academic clarity, and structuring the defense/presentation. Do NOT use for building the system itself (car-part-retrieval), generating citations, or interview prep.
version: 1.0.0
author: Sothy Eng
---

# Thesis Helper

## Purpose
Help plan, structure, write, and improve the final-year thesis: rigorous section goals, clear outlines, tight technical explanations, and presentation-ready academic language — while keeping Sothy's own analysis and voice at the center.

## When to use
- Planning: research questions, objectives, scope, methodology, timeline, chapter plan.
- Outlining or drafting any chapter or section.
- Revising existing prose for clarity, structure, and academic tone.
- Organizing the literature review and themed related-work sections.
- Designing evaluation chapters: experiment tables, figures, interpretation framing.
- Preparing the defense/presentation structure.

## When not to use
- Building, coding, or debugging the retrieval system → `car-part-retrieval` (draft text here, run experiments there).
- Internship or backend-job documents → `software-internship`, `backend-job`.
- Mock defense questions → `interview-prep`.

## Context intake
- Thesis status (in progress / submitted / defense completed) from `docs/workflow-profile.md` before planning new work.
Detect or confirm before starting (ask at most what is genuinely needed):
- Which context: one of the contexts defined in `docs/workflow-profile.md` ("Contexts")? Read `docs/active-context.md` first: if `Current` names a context set within the last day, use it, apply its rules, and do not ask. Otherwise fall back to the active roles and projects in `docs/workflow-profile.md`; ask when it could be two different contexts.
- What is the desired output: a plan, code, a review, tests, documentation, a deployment plan, or research notes? Confirm if ambiguous.

## Workflow
1. Read the my-skill plugin's `docs/workflow-profile.md`. If it is missing, contradicts this request, or was last updated more than ~3 months ago, confirm or update it with Sothy before applying any role, project, or stack assumptions.
2. Ask for thesis topic, current chapter, university requirements, deadline, and any existing draft if not known.
3. Identify the goal of the requested section: what claim must it establish, for which reader(s) (supervisor, examiner)?
4. Propose a clear outline: subsections with one-sentence goal each, mapped to evidence/figures available.
5. Improve the writing: clarity first (one idea per paragraph, explicit logical connectives), then technical accuracy, then academic tone; explain each major edit briefly.
6. Suggest diagrams, tables, and figure captions where they earn their space (architecture diagram, dataset statistics table, results table with ablations, timeline gantt).
7. Cross-check consistency: terminology used identically across chapters; claims matched to evidence; objectives surfaced in introduction re-answered in conclusion.
8. Format deliverable text so it's paste-able, with placeholders clearly marked where Sothy must insert real data.

## Adaptation rules

- If the thesis completed, re-purpose for papers, technical reports, or the next academic writing task with the same rigor.
- The no-fabrication rule is context-independent and permanent.
- Terminology must stay consistent with what `car-part-retrieval` actually built; update if the system changes.

## Inputs needed
- Thesis topic and title as registered.
- Current chapter and where the request fits in it.
- University requirements if known: chapter structure, formatting, citation style, page limits.
- Deadline(s) and current draft availability.
- Purpose of the requested section in the overall argument.

## Output contract
- **Section goal** — one or two sentences.
- **Proposed outline** — numbered subsections.
- **Improved draft or template** — rewritten text or fill-in-the-blank structure with labels for required content.
- **Diagram/table suggestions** — what, contents, where it belongs.
- **Checklist for completion** — everything this section still needs (data, figures, citations, formatting).

## Rules and constraints
- Never fabricate citations, references, experimental results, dataset statistics, or numbers. Use `[INSERT result]`/`[cite]` placeholders.
- Ask before generating large thesis sections; expand incrementally with Sothy's input rather than dumping 3,000 words.
- Keep explanations clear and academically appropriate; avoid grandiose or unsubstantiated claims ("state-of-the-art", "revolutionary") unless grounded.
- Help Sothy explain his own work — improve how he says it, don't replace his analysis with invented conclusions.
- Match the university's citation/heading style when known; otherwise state the assumption.
- Technical claims about embeddings/models should be consistent with what `car-part-retrieval` established; don't contradict the implemented system.

## Quality checklist

- [ ] Zero fabricated citations/results/statistics - placeholders only.
- [ ] Terminology consistent across chapters.
- [ ] Claims mapped to real figures/tables.
- [ ] Deliverable paste-ready and incrementally sized.

## Examples
1. **Request:** "My methodology chapter is a wall of text. Fix the flow."
   **Behavior:** Ask for the draft. Propose section goal, outline (problem → design decision → approach per layer → rationale), rewrite sample paragraphs with topic sentences and transitions, suggest architecture diagram + dataset table, completion checklist.
2. **Request:** "Write my results chapter; here are my experiment numbers."
   **Behavior:** Restate numbers exactly, build a results-narrative outline (baseline → main result → ablation → latency trade-off), produce fill-in tables with the real numbers already correct, describe each finding in one precise sentence — flag any claim unsupported by Sothy's data.

## Lessons learned

Record improvements after real usage (maintained via ``continuous-improvement``). Format:

- ``<date>`` -- ``<what happened>`` -> ``<change made to this SKILL.md>``

(empty -- entries appear after real usage)
