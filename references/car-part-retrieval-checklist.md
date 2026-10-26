# Car-Part Retrieval Checklist

Execution checklist for the intelligent car-part image retrieval final-year project (`car-part-retrieval`, `thesis-helper`). Work through the section for the current stage; earlier stages must be genuinely done before later claims are safe.

## Dataset checklist
- [ ] Source identified for each batch of images with license/usage status recorded.
- [ ] Target categories and granularity defined (e.g., brakes vs. callipers vs. pads) before scaling collection.
- [ ] Per-image minimum quality bar: resolution, in-focus, part visible, background complexity noted.
- [ ] Duplicates and near-duplicates removed (hash + perceptual check).
- [ ] Corrupt/blank images filtered; count of removals recorded.
- [ ] Folder structure agreed: `raw/ → cleaned/ → split/{train,val,test}/<category>/`.
- [ ] Metadata file exists (`metadata.csv`): image path, category, subcategory, part name, source, license, collection date.
- [ ] Class balance inspected; imbalance documented, not silently ignored.

## Labeling checklist
- [ ] Canonical label taxonomy defined: category → subcategory → part name (one spellings list, synonyms mapped).
- [ ] Labeling guideline written (2 pages is enough): what counts as this category, ambiguous examples adjudicated.
- [ ] Label normalization script exists and is re-runnable (no hand-editing of files).
- [ ] Sample of labels audited for accuracy; audit results recorded.
- [ ] Multi-label decisions decided (part functions as both "part" and "for car model X"?) and consistently applied.
- [ ] Labels versioned (v1, v2...) so experiments can state which labels they used.

## Embedding checklist
- [ ] Classical baseline implemented first (e.g., pretrained ResNet/CLIP features + cosine) — before any fine-tuning.
- [ ] Preprocessing pipeline fixed and versioned (resize, crop, normalization) — same everywhere.
- [ ] Embedding dimension, model, and version recorded per experiment.
- [ ] Fine-tuning (if used) justified by baseline gap; train/val curves logged, no silent overfit.
- [ ] Embeddings reproducible: seed set, batch order documented, config saved with the run.
- [ ] Embedding storage chosen (npz/parquet) with a proper versioned location.

## Vector search checklist
- [ ] Index type justified (HNSW vs. IVF vs. flat) against dataset size and latency budget.
- [ ] Distance metric matches training objective (cosine vs. L2) — verified, not assumed.
- [ ] Index build parameters and query parameters (ef, nprobe...) recorded.
- [ ] Vector store decision made deliberately (FAISS file, pgvector, Qdrant, Milvus) with reasoning.
- [ ] Metadata filtering path works (filter by category before/after similarity).
- [ ] Index update/append strategy defined (rebuild cadence vs. incremental insert).
- [ ] Latency measured p50/p95 at expected concurrency.

## Evaluation checklist
- [ ] Ground truth defined: what makes a result relevant (same part ID? same category? same fitment?).
- [ ] Split strategy prevents leakage (splits separated by part identity and/or image source, not random per-image).
- [ ] Metrics chosen: Precision@K, Recall@K, mAP, MRR (+ latency, index size, memory).
- [ ] Evaluation script re-runnable from one config; results written to a results file with config hash.
- [ ] Every experiment row: model version, data version, seed, metric values, notes.
- [ ] Ablation performed or planned (e.g., with/without re-ranking; with/without fine-tuning).
- [ ] Failure cases qualitatively reviewed (K worst queries) and noted for the thesis.

## API checklist
- [ ] Search endpoint contract defined (image in → ranked results with score, category, image URL).
- [ ] Upload validation: format, size, max dimensions; errors meaningful.
- [ ] Results include enough metadata for the consumer UI to render decisions.
- [ ] Latency budget stated per hop (preprocess / embed / search) and instrumented.
- [ ] Demo/admin functionality: re-index trigger, per-category stats, sample queries.
- [ ] API documented (OpenAPI), reproducible locally via Docker Compose.

## Thesis experiment checklist
- [ ] Research questions mapped to specific experiments/repos (RQ1 ← experiments X).
- [ ] Baselines named and honestly compared (classical CV, pretrained CNN, fine-tuned, multimodal if in scope).
- [ ] All figures generated from scripts, saved as vector format (PDF/SVG) where possible, and reproducible.
- [ ] Results tables match raw results files exactly — no hand-copied numbers.
- [ ] Limitations written from real observations (dataset size, domain gap, mislabeled cases), not defensively guessed.
- [ ] Seeds/configs disclosed in the methodology chapter for reproducibility claims.
