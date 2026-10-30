# my_skill

![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)
![Built for Claude Code](https://img.shields.io/badge/Built%20for-Claude%20Code-blueviolet)
![Status](https://img.shields.io/badge/status-active-brightgreen)

**my_skill** is a self-improving personal engineering workflow plugin for Claude Code: backend development, data engineering, applied ML/computer vision, research, and idea-to-production delivery.

It was built as Sothy Eng's personal toolkit, but it is structured to be **shareable and adaptable**: every skill reads `docs/workflow-profile.md` first, so a new user can take over the plugin by editing one file instead of seventeen.

## What makes my_skill different

Most marketplace plugins solve one craft well, once, for anyone. my_skill is built for one engineer's *changing* reality and gets sharper over time:

1. **Profile-first** — every skill reads `docs/workflow-profile.md` before starting, so work is framed for the right audience and stack, and aging out of a role degrades gracefully instead of breaking routing. `workflow-adapter` makes profile updates a first-class flow: state the change, see the drift, approve the diff.
2. **Improvement from real work, gated by you** — `continuous-improvement` turns post-task feedback into SKILL.md diffs (routing fixes, workflow steps, output contracts) with a changelog and lessons ledger. `skill-health-check` audits freshness and overlap against the profile. Nothing edits itself autonomously.
3. **Idea to verified production** — `production-delivery` + `backend-deployment` + `observability` give you acceptance criteria → slices → tests/review → deploy → +1h/+24h/+48h validation → runbooks, not just a deploy checklist.
4. **Applied AI with integrity rails** — baseline-first experiments, leakage-safe splits, seeded configs, and provenance on every quoted number (`applied-ai-delivery`, `car-part-retrieval`); academic writing treats fabrication as a hard error (`thesis-helper`).

## Who it is for

- Backend developers who want structured (not generic) assistance: reviews with verdicts, root-cause debugging, safe deployments.
- Applied ML / computer-vision students building retrieval or ML systems with real evaluation discipline.
- Students and early-career engineers juggling **multiple work contexts** (job + internship + coursework) where mixing advice between contexts is a real risk.
- Anyone who wants their assistant to **adapt over time** instead of hard-coding one snapshot of their career.

**Design note:** two context skills (`backend-job`, `software-internship`) are personal to the original author and kept deliberately separate — different teams, different codebases, different conventions. If you install this plugin, see [Customization](docs/CUSTOMIZATION.md) to repoint those skills to *your* contexts.

## What problems it solves

- **Right-framed answers:** context detection first (job / internship / thesis / personal / learning, plus desired output type), so advice is framed for the right audience.
- **Rigor by default:** hypothesis-driven debugging, blocking-vs-nice-to-have review verdicts, expand-contract migrations, seeded evaluation metrics, no fabricated citations or results.
- **Safe shipping:** pre-deployment checklists, rollback plans, post-launch validation checkpoints, symptom-based alerting.
- **A plugin that improves itself:** post-task retros and feedback turn into concrete SKILL.md edits, with changelog and lessons tracking.

## Folder structure

```
my_skill/
├── .claude-plugin/plugin.json   # manifest: name, version, skills/commands paths
├── README.md                    # this file
├── LICENSE                      # MIT
├── CONTRIBUTING.md              # how to contribute a skill
├── commands/                    # slash commands (manual entry points / dispatchers)
├── skills/<skill-name>/SKILL.md # one skill per folder
├── hooks/hooks.json            # PostToolUse hook: logs which skills fire to docs/usage-log.md
├── scripts/validate.py          # plugin validator (run before every commit; CI runs it too)
├── evals/transitions.json      # role-change scenarios for testing workflow-adapter
├── evals/triggers.json         # should / should-not trigger prompts per skill
├── templates/                   # SKILL.md scaffold + worked-example template (copy, don't edit in place)
├── docs/
│   ├── INSTALLATION.md          # detailed install/update/uninstall instructions
│   ├── CUSTOMIZATION.md         # adapt the plugin to your own workflow
│   ├── CREDITS.md               # author, built-with, thanks
│   ├── ROADMAP.md               # next / later / ideas
│   ├── CHANGELOG.md             # documented plugin changes (newest first)
│   ├── active-context.md        # today's context (job/internship/thesis/learning), set by /my-skill:today
│   ├── workflow-profile.md      # roles/projects/stacks/priorities — read by every skill first
│   └── lessons-learned.md       # real-usage lessons feed (maintained by continuous-improvement)
├── references/                  # production checklists, question bank (not auto-loaded)
├── examples/                    # worked example requests (not auto-loaded)
└── .github/PULL_REQUEST_TEMPLATE.md
```

`references/` and `examples/` are intentionally not plugin-manifest keys — skills read those files on demand; unknown manifest keys are unreliable across Claude Code versions.

## Skill catalog

| Skill | What it does |
|---|---|
| `api-design` | Designs clean, consistent, production-ready REST APIs and service contracts. |
| `backend-code-review` | Reviews PRs and backend code like a senior engineer, with blocking vs. nice-to-have issues and a verdict. |
| `backend-debugging` | Systematic root-cause diagnosis of backend errors, latency, Kafka/Redis/DB issues. |
| `backend-testing` | Creates practical unit, integration, API, database, and contract tests. |
| `backend-deployment` | Plans safe deployments: checklists, migrations, rollback, +1h/+24h/+48h validation. |
| `backend-job` | Senior backend engineering assistant for paid backend work (Spring Boot/FastAPI/Go, PostgreSQL, Redis, Kafka). |
| `software-internship` | Practical dev mentor for implementing assigned features, fixing bugs, and preparing PRs as an intern. |
| `internship-communication` | Drafts professional messages, standups, blocker reports, and status updates. |
| `car-part-retrieval` | Computer-vision retrieval systems: datasets, embeddings, vector search, evaluation, architecture. |
| `thesis-helper` | Academic writing and thesis structure with a strict no-fabrication rule. |
| `data-engineering` | Teaches and builds data pipelines: ETL/ELT, Kafka/CDC, dbt/Airflow, end-to-end projects. |
| `observability` | Day-2 monitoring: metrics, dashboards, alerts, SLOs, health checks, runbooks. |
| `documentation` | Code-grounded docs: READMEs, setup guides, ADRs, API docs, runbooks. |
| `learning-roadmap` | Realistic weekly study plans and small project milestones. |
| `interview-prep` | Mock interviews and direct feedback for backend, SDE, DE, and DS roles. |
| `workflow-adapter` | Detects profile-vs-reality drift (role/project/stack changes) and updates `docs/workflow-profile.md` with an approved diff. |
| `applied-ai-delivery` | Takes an ML/CV experiment to a delivered, defensible artifact: packaging, evaluation report, handover with provenance. |
| `production-delivery` | Orchestrates one deliverable from idea to verified production: phase gates, delegated craft skills, +1h/+24h/+48h validation, closure retro. |
| `continuous-improvement` | Plugin self-improvement loop: retros, feedback into SKILL.md edits, changelog, lessons. |
| `skill-health-check` | Read-only inventory audit: freshness, overlap, vague triggers, ranked recommendations. |

## Works with any agent, not just Claude Code

The skills are plain markdown — the only agent-specific part is *discovery*. So the plugin ships a universal entry point:

- **[`AGENTS.md`](AGENTS.md)** (root): read automatically by agents following the [AGENTS.md convention](https://agents.md) — OpenAI Codex, Gemini CLI, Cursor, Zed, OpenCode, and others. It contains the profile-first rule, a trigger → skill routing index for all 20 skills, and the improvement-loop rules.
- **Claude Code**: native discovery via `.claude-plugin/plugin.json` + `skills/*/SKILL.md` frontmatter and `/my-skill:*` commands.
- **Any other agent** (or no agent): the files are self-contained — point your agent at the catalog table in this README and let it read the matching `skills/<name>/SKILL.md`.

| Agent | How it uses my_skill |
|---|---|
| Claude Code | Native skills + `/my-skill:` commands |
| Codex / Gemini CLI / Cursor / Zed / OpenCode | Auto-reads `AGENTS.md`, loads `skills/<name>/SKILL.md` on demand |
| Any other tool | Paste the request + the relevant SKILL.md content into the prompt |

## Installation

Three ways to install. Full details (requirements, verification, troubleshooting, uninstall) in [`docs/INSTALLATION.md`](docs/INSTALLATION.md).

### Method 1 — Local development install (`--plugin-dir`)

Best for trying or hacking on the plugin without committing.

```bash
claude --plugin-dir /path/to/my_skill
```

That session loads the plugin directly from the folder. Changes to skills are picked up by restarting Claude Code.

### Method 2 — Copy into the plugins directory

```bash
# clone anywhere, then copy the whole folder into your plugins directory:
git clone https://github.com/albkue/my_skill.git
# then copy / move the my_skill folder into:
#   ~/.claude/plugins/my_skill        (macOS / Linux)
#   %USERPROFILE%\.claude\plugins\my_skill   (Windows)
```

Restart Claude Code, run `/plugin`, and confirm `my_skill` is listed and enabled.

### Method 3 — Install via a plugin marketplace (GitHub)

Publish or consume through a marketplace repo: the marketplace file lists plugins by GitHub repo; users add the marketplace and install with `/plugin install my-skill@<marketplace-name>`. Setup for authors is in [`docs/INSTALLATION.md`](docs/INSTALLATION.md).

### Updating after pulling changes

```bash
cd /path/to/my_skill
git pull          # or download the new zip and replace the folder
```

Then restart Claude Code (or `/plugin` → disable/enable the plugin). New skills are discovered on the next session start. Check `docs/CHANGELOG.md` for what changed and read any **Migration notes** before upgrading minor/major versions.

## Usage

Slash commands are the manual entry points. The plugin namespace is **`my_skill`** as displayed to humans, but the *functional* namespace is the plugin name in `.claude-plugin/plugin.json` — currently `my-skill` (hyphen). `/my_skill:...` with an underscore will **not** resolve; use `/my-skill:...`.

| Command | Routes to | Use it for |
|---|---|---|
| `/my-skill:my-skill` | menu + router | Any request; asks for context and picks the right skill |
| `/my-skill:backend-review` | `backend-code-review` | "Review this PR / diff / controller" |
| `/my-skill:computer-vision` | `car-part-retrieval` | Datasets, embeddings, vector search, evaluation |
| `/my-skill:research` | `thesis-helper` | Thesis planning, chapters, literature review, defense |
| `/my-skill:product-to-production` | `production-delivery` | Full lifecycle orchestrator: design → plan → build → ship → validate → retro, with phase gates |
| `/my-skill:applied-ai-delivery` | `applied-ai-delivery` | "Package the model", "make the demo real", evaluation reports with provenance |
| `/my-skill:workflow-adapter` | `workflow-adapter` | "My workflow changed", "update my workflow profile" — drift reconciliation |
| `/my-skill:continuous-improvement` | `continuous-improvement` | "Review my last task", "improve skill X", "my workflow changed", monthly report |
| `/my-skill:skill-health-check` | `skill-health-check` | Inventory audit with ranked recommendations |

### Example commands

```
/my-skill:my-skill
/my-skill:my-skill Review this Spring Boot Kafka consumer for retry and idempotency handling (backend job)
/my-skill:backend-review <paste diff or file paths>
/my-skill:computer-vision Compare CLIP vs. ResNet embeddings for image retrieval
/my-skill:research Outline my methodology chapter
/my-skill:product-to-production Review the whole retrieval system end to end before the defense
```

### Example natural-language requests

Just talk normally — descriptions decide which skill activates:

```
Review my PostgreSQL query that's causing timeouts          → backend-job / backend-debugging
Does this API design handle pagination and errors right?    → api-design
Write tests for this Spring service                          → backend-testing
How do I ask my supervisor about unclear acceptance criteria?→ internship-communication
Compare CLIP vs. ResNet embeddings for car-part retrieval    → car-part-retrieval
Build me a small CDC pipeline with Debezium                  → data-engineering
Is my service ready to be on-call?                           → observability
Review how my plugin handled my last task                    → continuous-improvement
```

### Example use cases: why my_skill is different

1. **"My internship ended mid-project."**
   `workflow-adapter` updates the profile (moves the role to *Completed / paused* with a date); `continuous-improvement` proposes redirect diffs for `software-internship` and `internship-communication`; you approve; nothing is deleted, everything is repointed. Marketplace equivalent: nothing.

2. **"Ship the image-search API before my defense."**
   `production-delivery` sequences acceptance criteria → sliced plan → `backend-testing` → `backend-code-review` → `backend-deployment` → +1h/+24h/+48h post-launch validation → closure retro — all stack- and profile-aware. Marketplace equivalent: a static checklist.

3. **"Review how you handled my last review task."**
   `continuous-improvement` compares the original request with the final output, asks 2–4 short feedback questions, and shows a before/after diff before touching any SKILL.md. Marketplace equivalent: autonomous prompt-optimization tools that don't show their work.

4. **"Are those accuracy numbers real?"**
   Provenance rules across `applied-ai-delivery` / `car-part-retrieval` / `thesis-helper` make every quoted metric traceable to its source run — fabrication is a hard error, not a style choice. Marketplace equivalent: none.

### How skills trigger automatically

Claude Code matches your request against each skill's `description` frontmatter. This plugin's descriptions include explicit **trigger conditions** and "when NOT to use" boundaries, so routing stays predictable. If two skills could apply, the plugin asks one clarifying question (e.g., *"Is this for your paid backend job or your internship?"*) rather than guessing. If routing ever feels wrong, that's a description bug — report it and `continuous-improvement` will fix the description, not the workflow.

## Customizing for another user

See [`docs/CUSTOMIZATION.md`](docs/CUSTOMIZATION.md). Short version:

1. Edit `docs/workflow-profile.md` — roles, projects, stacks, priorities. This is the control surface.
2. Keep the generic skills (`api-design`, `backend-testing`, `deploy`…) as-is.
3. Repoint personal skills (`backend-job`, `software-internship`) to your own contexts or delete them — they are your author's, not load-bearing.
4. Never hard-code a person's job titles into generic skills; use the profile instead.

## Adding a new skill

Follow [`CONTRIBUTING.md`](CONTRIBUTING.md): copy `templates/SKILL-template.md` into `skills/<skill-name>/SKILL.md`, lowercase-hyphenated unique name, specific description, required sections (Purpose, When to use, Context intake, Workflow, Adaptation rules, Inputs needed, Output contract, Quality checklist, Rules and constraints, Lessons learned, Examples), README + CHANGELOG entries, then a local test with `claude --plugin-dir .`.

## Troubleshooting

| Symptom | Cause | Fix |
|---|---|---|
| `/my-skill:...` commands don't appear | plugin not loaded | run `/plugin` and enable; verify folder is under the plugins dir (or launched with `--plugin-dir`) |
| Commands only resolve as `my-skill:...`, not `my_skill:...` | plugin name contains a hyphen | use `/my-skill:<command>` — the namespace must match the plugin `name` in `plugin.json` |
| A skill didn't trigger | description not matched by your phrasing | invoke it explicitly via `/my-skill:my-skill`, then tell `continuous-improvement` so the description can be fixed |
| Skills ask about "my internship" though you don't have one | personal context skills still installed | remove `backend-job`/`software-internship`/`internship-communication` folders, or update `docs/workflow-profile.md` |
| New skill not found after adding | session cached | restart Claude Code |
| `Parse error` on plugin load | invalid `plugin.json` or frontmatter | validate JSON; check every SKILL.md has `---` frontmatter with `name` + `description` |

## Author

Created and maintained by **Sothy Eng**.
GitHub: https://github.com/albkue

## Credits

Full [Credits →](docs/CREDITS.md) — author, built-with info, and thanks.

## Contributing

Contributions welcome — see [`CONTRIBUTING.md`](CONTRIBUTING.md) for the skill standard, local testing, and the PR checklist.

## Roadmap

Where the plugin is heading: [`docs/ROADMAP.md`](docs/ROADMAP.md) — *Next / Later / Ideas*.

## License

This project is licensed under the [MIT License](LICENSE). See `LICENSE` for details.
