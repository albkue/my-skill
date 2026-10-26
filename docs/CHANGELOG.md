# my-skill changelog

All documented plugin changes. Newest first. Format: version — date — Added / Changed / Removed / Breaking changes / Migration notes.

## [Unreleased]

(none — ready for next change)

## 1.6.0 — 2026-10-26

**Added**
- Cross-agent support: root `AGENTS.md` (AGENTS.md-convention entry point — OpenAI Codex,
  Gemini CLI, Cursor, Zed, OpenCode, others) with the profile-first rule, a
  trigger → skill routing index for all 20 skills, and the improvement-loop rules.
- README "Works with any agent" section; INSTALLATION.md per-agent usage section.

**Fixed**
- AGENTS.md routing index verified against on-disk skills (20/20 targets exist; no dangling references).

### Added
- Credits, license, contribution guide, roadmap, and sharing documentation:
  `docs/CREDITS.md`, `docs/ROADMAP.md`, root `CONTRIBUTING.md` (moved from `docs/`),
  README badges + Author / Credits / Contributing / Roadmap / License sections,
  GitHub links (`github.com/albkue`).

## 1.5.0 — 2026-10-26

**Added**
- `skills/workflow-adapter/SKILL.md` — reconciles drift between `docs/workflow-profile.md` and the user's actual current work; updates the profile only via an approved diff. Command: `/my-skill:workflow-adapter`.
- `skills/applied-ai-delivery/SKILL.md` — takes an ML/CV experiment to a delivered, defensible artifact with evaluation hygiene and provenance tracking (`[REP]` markers). Command: `/my-skill:applied-ai-delivery`.
- `skills/production-delivery/SKILL.md` — idea-to-verified-production orchestrator: phase map, delegated craft skills, user gates at Design/Plan/Ship, +1h/+24h/+48h validation, closure retro.
- `templates/SKILL-template.md` — 12-section scaffold for new skills (referenced by README + CONTRIBUTING).
- `templates/example-template.md` — worked-example capture template for `examples/`.
- Quality-scoring rubric in `skill-health-check`: four sub-criteria (description specificity, workflow measurability, contract testability, adaptation breadth), 0–10 per skill.

**Changed**
- `commands/product-to-production.md` now routes through the `production-delivery` orchestrator instead of an inline lifecycle.
- README gained "What makes my_skill different" positioning section and differentiated use-case examples.
- Plugin manifest version → 1.5.0; description updated with new skills.

## 1.4.0 — 2026-10-26

**Changed**
- **Plugin renamed `thy-skill` → `my-skill`** (manifest `name`, README, all docs, skill workflow step 1, self-referencing skill descriptions).
- Menu command renamed: `commands/thy-skill.md` → `commands/my-skill.md` (same routing behavior).

**Removed** — none (all skills, references, examples unchanged).

**Breaking changes**
- The command namespace changes: `/thy-skill:<command>` no longer resolves after updating. Use `/my-skill:<command>`.

**Migration notes**
- After updating, restart Claude Code and re-run any command with the new namespace (e.g., `/my-skill:my-skill`, `/my-skill:skill-health-check`).
- If you had notes/macros pointing at `/thy-skill:...`, update them to `/my-skill:...`.

## 1.3.0 — 2026-10-26

**Added**
- Skill docs suite: `docs/INSTALLATION.md` (local `--plugin-dir`, plugins-directory, and GitHub-marketplace installs; verification, per-skill smoke tests, update/uninstall, error table).
- `docs/CUSTOMIZATION.md` (repoint the plugin to another user's workflow: profile editing, context-skill repointing/removal, description routing, safe renames, team conventions).
- `docs/CONTRIBUTING.md` (12-section skill standard, naming/description rules, review checklist, local testing procedure).
- `LICENSE` — MIT, copyright 2026 Sothy Eng.
- `.github/PULL_REQUEST_TEMPLATE.md`.

**Changed**
- `README.md` rewritten for sharing: generic intro, three installation methods, marketplace notes, update/uninstall, troubleshooting table, license/author, links to all docs.
- `.claude-plugin/plugin.json` version → 1.3.0.

**Removed** — none.

**Breaking changes** — none.

**Migration notes** — none; all existing skills, commands, and references unchanged.

## 1.2.0 — 2026-10-26
- New skill `continuous-improvement`: feedback → SKILL.md edits loop with before/after diffs, changelog, and lessons tracking.
- New skill `skill-health-check`: read-only inventory audit (overlap, vague triggers, profile mismatch) with ranked merge/split/rename/archive recommendations.
- New `docs/workflow-profile.md`: single source of truth for current roles, projects, stacks, priorities; all skills read it first and ask when stale — plugin degrades gracefully as Sothy's situation changes.
- Restructured all skills to a common adaptive structure: Purpose / When to use / When not to use / Context intake / Workflow / Adaptation rules / Inputs needed / Output contract / Rules and constraints / Quality checklist / Lessons learned / Examples. Existing content preserved; `Required inputs` → `Inputs needed`, `Output format` → `Output contract`.
- Role-tied skills (`backend-job`, `software-internship`, `internship-communication`, `interview-prep`, `thesis-helper`, `car-part-retrieval`) gained graceful-degradation wording: confirm context against the profile, redirect when it changed.
- New commands: `continuous-improvement`, `skill-health-check`.

## 1.1.0 — 2026-10-26
- New skills `observability` (day-2 metrics/alerts/SLOs/runbooks) and `documentation` (code-grounded READMEs/ADRs/API docs).
- New commands `backend-review`, `computer-vision`, `research`, `product-to-production` (full lifecycle orchestrator).
- Post-launch validation checkpoint (+1h/+24h/+48h) added to `backend-deployment`; fix→test/implement handoff added to `backend-debugging` and `backend-code-review`.
- `plugin.json`: removed non-manifest `references` key.

## 1.0.0
- Initial version: 13 skills across the four core contexts (backend job, internship, car-part retrieval thesis/data engineering, plus `api-design`/`learning-roadmap`/`interview-prep`), dispatcher command, references, examples.
