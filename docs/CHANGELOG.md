# my-skill changelog

All documented plugin changes. Newest first. Format: version — date — Added / Changed / Removed / Breaking changes / Migration notes.

## [Unreleased]

(none — ready for next change)

## 1.10.0 — 2026-10-30

**Added**
- Transition playbook in `workflow-adapter`: on a job/role change it builds a capability map for the new role, matches each capability to an existing my-skill skill, an installed non-my-skill skill, or a gap, and produces ONE approval-gated proposal (profile diff, new context with rules, `Defer to` list, at most 2-3 new skills drafted from the template only for real gaps, demote/retire candidates from the usage log).
- Optional `- Defer to: <skills>` line per context in the profile; the `/my-skill` dispatcher (Step 3b) routes matching requests to those installed skills while still applying the context's rules.
- `evals/transitions.json` — 4 role-change scenarios (internship to data engineer, data analyst move, thesis done, stack change) with expected profile changes, reuse, new skills, and retirements; validated for structure and skill names.

**Changed**
- `workflow-adapter` may now create NEW skill folders during an approved transition (it still never edits existing skills; that stays with `continuous-improvement`).
- Validator checks the playbook exists and the scenario file is well-formed.

**Migration notes**
- No action needed. Say "my job changed to X" and `workflow-adapter` runs the playbook. The scenarios are for manual live testing; nothing runs them automatically.

## 1.9.0 — 2026-10-30

**Added**
- `/my-skill:setup` — interviews a new user and generates their `docs/workflow-profile.md` (roles, projects, contexts, per-context safety rules).
- `docs/workflow-profile.example.md` — neutral template for anyone adopting the plugin.
- "Contexts" section in the workflow profile: contexts and their rules are now data, so users define their own.

**Changed**
- `/my-skill:today` accepts any context id defined in the profile (was a fixed list of four); per-context rules moved from `active-context.md` into the profile.
- 15 skills' context-intake line and the `/my-skill` dispatcher menu read contexts from the profile instead of naming job/internship/thesis.
- Validator checks `Current` against the profile's defined context ids.

**Migration notes**
- Existing profile keeps working; its four contexts (`job`, `internship`, `thesis`, `learning`) carried over unchanged.
- Persona skills (`backend-job`, `software-internship`, `car-part-retrieval`, etc.) still name the original author's situation; see `docs/CUSTOMIZATION.md` section 2.

## 1.8.0 — 2026-10-30

**Added**
- `docs/active-context.md` + `/my-skill:today <job|internship|thesis|learning>` — one switch for the day's context. Skills read it right after the workflow profile, skip the "job or internship?" question when it is set (within a day), and apply per-context rules (job: rollback plan and confirmation before prod changes; internship: supervisor questions, no job code; thesis: provenance and vault sync).
- `hooks/hooks.json` + `scripts/log_skill.py` — PostToolUse hook on the Skill tool appends `date — skill — context` to `docs/usage-log.md` (git-ignored, local). `continuous-improvement` and `skill-health-check` read it to find unused and over-used skills with data.
- Validator checks for the active-context file, hook wiring, and that `backend-job` / `software-internship` consult it.

**Changed**
- 15 skills' context-intake line, `backend-job`, `software-internship`, `applied-ai-delivery`, `production-delivery`, `workflow-adapter`, `my-skill` dispatcher and `AGENTS.md` routing rule now consult the active context before asking.

**Migration notes**
- Run `/my-skill:today <context>` at the start of a work block. Left `unset` or stale, behavior is identical to 1.7.0.
- The hook needs Python on PATH. If it is missing the hook fails silently; skills are unaffected.

## 1.7.0 — 2026-10-30

**Added**
- `scripts/validate.py` — stdlib-only plugin validator: frontmatter (name == folder, 1024-char description limit, "Do NOT use" boundary), profile-first rule, command targets, AGENTS.md routing coverage and version sync, CHANGELOG/manifest version sync, relative links, eval coverage.
- `evals/triggers.json` — 3 "should trigger" + 2 "should not trigger (routes to X)" prompts for every skill (100 prompts), validated for coverage and valid routing targets.
- `.github/workflows/validate.yml` — runs the validator on push and PR.

**Changed**
- PR template and CONTRIBUTING now require `python scripts/validate.py` to pass and new skills to add eval prompts.
- ROADMAP: automated validation and eval set moved from Later to done.

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
