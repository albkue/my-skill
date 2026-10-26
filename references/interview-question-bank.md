# Interview Question Bank

Question bank for `interview-prep` (and `learning-roadmap` planning). Organized by area with a "what a good answer should show" note per question, not canned answers. Difficulty: ★ basic, ★★ solid understanding, ★★★ senior-ish depth. Role tags: [BE] backend/new-grad, [DE] data engineering, [DS] data science/ML.

## Backend questions
- ★ Explain the HTTP request lifecycle through a modern web server/framework. — *shows baseline mental model.*
- ★★ Difference between processes and threads; how does a language/runtime you know handle concurrency? — *shows runtime literacy [BE].*
- ★★ What happens, end to end, when you type a URL and press Enter? — *classic; tests layered knowledge.*
- ★★ Explain idempotency in HTTP; how would you make a payment endpoint idempotent? — *shows API-service experience.*
- ★★★ How would you design rate limiting for a multi-tenant API? Compare token bucket vs. leaky bucket vs. fixed windows. — *distributed systems and trade-off thinking.*
- ★★★ How do you keep a long-running transaction safe while still calling an external service? — *real incident-grade reasoning.*
- ★★ What's the difference between optimistic and pessimistic locking? When would each break? — *concurrency pragmatics.*

## API questions
- ★ REST vs. RPC-style APIs; when is each the right choice? — *design fundamentals.*
- ★★ Design an endpoint for a file upload with virus scanning; where does it get slow, and how do you handle it? — *async patterns, polling, S3-style artifact flows.*
- ★★ How would you version an API that has angry enterprise consumers? — *deprecation communication besides technical mechanism.*
- ★★★ How would you design paginated endpoints for very large result sets without offset pagination? — *cursor/pagination depth.*

## Database questions
- ★ Normalization basics: 1NF–3NF in your own words. — *theory literacy.*
- ★★ When/why might you denormalize? Risks and mitigations. — *trade-off growing.*
- ★★ Index types (b-tree, hash, composite); how do you decide what to index? — *read-the-query-plan thinking.*
- ★★ Explain why `SELECT *` plus a JSON column in a hot path degrades performance. — *index/TOAST/cache awareness.*
- ★★★ How does MVCC work in Postgres? What problem does it solve and create? — *deep internals [BE].*
- ★★★ Star schema vs. snowflake schema; when is each appropriate? — *warehouse modeling [DE].*
- ★★ What is `SELECT ... FOR UPDATE` used for, and what can go badly wrong with it? — *locking in practice.*
- ★★★ Write SQL: the latest order per customer, with performance reasoning. — *window functions execution.*

## Kafka questions
- ★ Explain topics, partitions, keys, offsets in one pass. — *fundamentals.*
- ★★ What actually happens when a consumer falls behind and exceeds `max.poll.interval.ms`? — *lived experience [BE].*
- ★★ Delivery semantics: at-most-once vs. at-least-once vs. exactly-once; which is realistic in practice? — *semantics maturity.*
- ★★ How do you handle a poison-pill message? — *operational maturity.*
- ★★★ Explain consumer group rebalancing; what operational pain does it cause and how would you reduce it? — *production experience.*
- ★★★ What breaks if the consumer commits offsets before processing the message? Or vice versa? — *offset correctness.*

## Redis questions
- ★ What data structures does Redis offer and name a realistic use for each. — *breadth.*
- ★★ Cache invalidation strategies: TTL vs. write-through vs. event-driven; trade-offs of each. — *pattern literacy.*
- ★★ What is a cache stampede and two ways to prevent it? — *operational awareness.*
- ★★★ Explain Redis persistence options (RDB vs. AOF) and when each fails. — *recovery thinking.*

## System design questions
- ★★ Design a URL shortener. — *classic start: hashing, collisions, redirects, analytics.*
- ★★ Design an image upload/CDN service. — *storage, CDN, presigned URLs, eviction.*
- ★★★ Design a search-by-image service (relevant to the car-part retrieval project). — *embedding service, vector index, metadata store, cache, latency budget.*
- ★★★ Design a notification service with at-least-once delivery and per-user rate limits. — *queues, dedupe, fan-out, idempotency.*
- ★★★ Design a data pipeline processing 5M events/day from app users into a dashboard. — *[DE] batch vs. streaming choice, storage, freshness, quality checks.*
- Tips: always start with requirements clarification, non-functional targets (latency/consistency), API surface, data model, then scale/caching/queues/trade-offs. Interviewers vote on reasoning, not buzzwords.

## Data engineering questions
- ★ ETL vs. ELT; why has ELT become common with modern warehouses? — *paradigm literacy [DE].*
- ★★ Batch vs. streaming: criteria for choosing which. — *decision maturity.*
- ★★ What is CDC and when is it the right ingestion strategy? — *Debezium/Logical WAL literacy.*
- ★★ What is idempotency in a data pipeline and why does it matter more there than in APIs? — *retries/backfills.*
- ★★ Schema evolution: how do you add a required field without breaking consumers? — *versioned contracts, additive changes.*
- ★★★ How would you handle late-arriving data in an app that computes daily aggregates? — *watermarks, reprocessing windows [DE].*
- ★★★ Explain an Airflow DAG architecture you'd build for 20 interconnected data jobs. — *sensors, task groups, retry policy.*

## Machine learning / data science questions
- ★ Precision vs. recall in one concrete example each. — *fundamentals [DS].*
- ★★ What is Precision@K / mAP / MRR, and where do they make sense? — *retrieval-project fluency.*
- ★★ Explain contrastive learning at a high level; why is CLIP suited to text-to-image search? — *embedding literacy.*
- ★★ How do you split an image dataset for retrieval evaluation to avoid leakage? — *his thesis project directly.*
- ★★★ How do you detect and handle data drift in a deployed image search system? — *monitoring maturity.*

## Behavioral questions
Use STAR (Situation, Task, Action, Result); ground answers in real events from the backend job, internship, car-part retrieval project, and university team context — never invented stories.
- ★ Tell me about yourself / a project you're proud of.
- ★ Why this company / this role?
- ★★ Tell me about a time you disagreed with a teammate's technical decision.
- ★★ Describe a hard bug you found and fixed. — *car-part retrieval, backend-job, or internship candidates welcome.*
- ★★ Tell me about a time you missed a deadline.
- ★★ How do you decide what to learn next given limited time? — *honest roadmap story: backend job + internship + thesis simultaneously.*
- ★★★ Tell me about a mistake that had real consequences and what you changed afterward.
