---
name: car-part-retrieval
description: Support Sothy Eng's final-year project - an intelligent car-part image retrieval system. Use for project scope/user stories/architecture, car-part image datasets (collection, cleaning, labeling, splitting), image embeddings (classical CV, CNN/metric.learning, multimodal CLIP-style), vector databases and similarity search, model selection/fine-tuning/evaluation, search API and indexing pipeline, admin functionality, and technical documentation or diagrams for the system. Do NOT use for thesis chapters and academic writing (thesis-helper), backend-job work, or interview prep - but evaluation results from this project can be routed to interview-prep as material.
version: 1.0.0
author: Sothy Eng
---

# Car-Part Retrieval

## Purpose
End-to-end assistant for the final-year project: turn "search for a car part by image" into a concrete, buildable, evaluable system — data pipeline, embedding model, vector index, search API, and evaluation — sized for a final-year project, not a research lab.

## When to use
- Scoping the project: user stories, requirements, MVP definition, architecture.
- Working on datasets: sourcing, scraping, cleaning, labeling, splitting, metadata design.
- Choosing or fine-tuning embedding models; comparing classical CV vs. deep embeddings vs. multimodal (text-to-image) retrieval.
- Building the retrieval layer: vector DB selection, indexing strategies, ranking and re-ranking.
- Building the search API, ingestion/indexing pipeline, and admin functionality.
- Designing experiments and the evaluation harness (Precision@K, Recall@K, mAP, MRR, latency, index size).
- System diagrams and technical (non-thesis-format) documentation.

## When not to use
- Thesis chapters, abstracts, academic tone, literature review structure → `thesis-helper` (but technical content can be drafted here and handed over).
- Data engineering topics beyond this project's direct need (warehouse modeling, CDC learning) → `data-engineering`.
- Backend-job work → `backend-job`.
- Mock interview questions about this project → `interview-prep`.

## Context intake
- Confirm the project is still the car-part image retrieval thesis (check `docs/workflow-profile.md`); if the thesis shipped or the domain changed, reframe to the current project stage.
Detect or confirm before starting (ask at most what is genuinely needed):
- Which context: part-time paid backend work, internship, thesis / final-year project, personal project, or learning? Fall back to the active roles and projects in `docs/workflow-profile.md`; ask when it could be two different contexts.
- What is the desired output: a plan, code, a review, tests, documentation, a deployment plan, or research notes? Confirm if ambiguous.

## Workflow
1. Read the my-skill plugin's `docs/workflow-profile.md`. If it is missing, contradicts this request, or was last updated more than ~3 months ago, confirm or update it with Sothy before applying any role, project, or stack assumptions.
2. Ask for the current stage, available data, tech stack, target categories, and evaluation requirements if missing.
3. Frame the system as layers — data, model (embedding), retrieval (index/search), API, evaluation — and identify which layer the current request belongs to.
4. Recommend a practical architecture first (simple baseline that works end-to-end), then the scaled/improved version if the request asks for more.
5. For datasets: define folder structure, metadata schema (part category, part name, make/model fitment, source, license), label taxonomy, train/val/test split (splitting by part type and by image source to avoid leakage), and quality checks.
6. For retrieval: compare embedding options in a small table (model, embedding dim, training data, fit for car parts, cost) and vector DB/indexing options (FAISS HNSW/IVF, hnswlib, pgvector, Qdrant, Milvus), state when re-ranking (classical CV features, metadata filtering, fitment rules) helps.
7. For evaluation: define the ground-truth protocol (query image → relevant part IDs), metrics (Precision@K, Recall@K, mAP, MRR, latency p50/p95, index build time/size), and a reusable experiment config with seeds for reproducibility.
8. Deliver implementation guidance in small testable steps — always something Sothy can run the same day.
9. When useful for thesis later, structure outputs so results/figures can be reused by `thesis-helper`.

## Adaptation rules

- The layering (data -> embedding -> index -> API -> evaluation) is domain-agnostic: keep it and re-derive dataset/metrics per domain if the project scope changes.
- Post-graduation: the same skill serves personal products built on the system or learning experiments; route thesis-only content to `thesis-helper` once the profile updates.
- Free/open tools and GPU-optional paths remain the default unless the profile says otherwise.

## Inputs needed
- Current project stage (idea / data collection / model / retrieval / API / evaluation / writing).
- Available data: what exists, format, size, licensing status.
- Stack: languages, frameworks, GPU availability, vector DB preference if any.
- Target car-part categories (engine parts? body panels? filter types? granularity?).
- Evaluation requirements: university expectations, deliverable list, deadline.

## Output contract
- **Current stage assessment** — where the project stands, what's ready, what's missing.
- **Recommended architecture** — diagram (Mermaid or ASCII) of the layer relevant to the request.
- **Concrete next steps** — ordered, small, end with something runnable.
- **Code, schema, or experiment design** — as requested.
- **Evaluation plan** — metrics, protocol, expected-effort/expected-result table.
- **Risks and limitations** — data license issues, class imbalance, domain gap, GPU constraints, scope creep.

## Rules and constraints
- Do not assume Sothy already has a labeled dataset; always start from what actually exists.
- Prefer reproducible experiments and clear baselines: benchmark a classical baseline (e.g., ResNet features + cosine, or OpenCV/SIFT+FLANN) before fine-tuning anything.
- Explicitly separate the three retrieval regimes — classical image retrieval, deep embedding retrieval, multimodal/text-to-image retrieval — and don't blur them.
- Keep the system practical for a final-year project: free/open tools, dataset sizes from a few thousand images unless stated otherwise, GPU-optional paths.
- Respect licensing: flag scraped or partly-licensed data sources as needing verification; never fabricate dataset sources.
- Do not fabricate experimental results; when Sothy shares numbers, restate them exactly before interpreting.

## Quality checklist

- [ ] A plain baseline exists/is planned before any fine-tuning.
- [ ] Train/val/test split designed to avoid leakage.
- [ ] Metrics have a stated ground-truth protocol and seeded config.
- [ ] Output ends with something runnable today.
- [ ] All quoted numbers come from Sothy, restated exactly.

## Examples
1. **Request:** "Design an image embedding and vector search pipeline for retrieving car parts from an uploaded photo."
   **Behavior:** Assess stage; propose architecture diagram (upload → preprocess → embedding model → vector DB (HNSW) → top-K + optional re-rank → results); recommend starting with pretrained ResNet/CLIP embeddings + FAISS baseline, pgvector if Postgres-only; define indexing pipeline, metadata schema, and Precision@K/MRR/latency evaluation; list next runnable steps.
2. **Request:** "My labels are messy — parts have many spellings and nested categories."
   **Behavior:** Propose a canonical label taxonomy (category → subcategory → part name), a normalization mapping, dedup/consistency checks, split strategy avoiding leakage of near-duplicate part photos, and quality metrics (label audit sample, inter-checklist). Output format applied.

## Lessons learned

Record improvements after real usage (maintained via ``continuous-improvement``). Format:

- ``<date>`` -- ``<what happened>`` -> ``<change made to this SKILL.md>``

(empty -- entries appear after real usage)
