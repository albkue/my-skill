# Customizing my_skill for your own workflow

my_skill is built so that adapting it means editing **one small file plus a few descriptions** — never rewriting every skill. This guide covers the safe changes, in order of cost.

## 1. The control surface: `docs/workflow-profile.md`

Every skill reads this file first and asks you to update it if it's missing or stale. Edit these sections:

- **Current roles** — your actual paid/unpaid roles (job titles you hold *now*).
- **Active projects** — what you're building, with a one-line stack note each.
- **Main tech stacks** — languages, frameworks, DBs, infra you actually use.
- **Team conventions** — branch/PR/commit style per team, deployment process.
- **Deployment environment** — where things actually ship.
- **Current priorities** — ranked; skills use this to weight suggestions.
- **Completed / paused workflows** — retired roles/projects with a date. **This section is the migration mechanism**: moving an item here is what tells the skills to stop routing to it.

Update `Last updated: <date>` at the top. Say *"my workflow changed"* afterwards and `continuous-improvement` will propose the matching skill edits (as diffs, before applying anything major).

## 2. Repoint (or remove) the personal context skills

Three skills are personal to the original author and are **not load-bearing**:

| Skill | What it assumes | Your options |
|---|---|---|
| `backend-job` | a paid backend developer job | if you have an equivalent paid role, edit the description to name *your* role; otherwise delete the folder |
| `software-internship` | a developer internship | same — rename to a mentor-for-assigned-work skill or delete |
| `internship-communication` | internship communication | generalize the description to "professional work communication" or delete |

Deleting a context skill is safe: the generic skills (`api-design`, `backend-debugging`, `backend-testing`, `deployment`, etc.) work without it. After removal, restart Claude Code and run the `skill-health-check` to confirm nothing references them. (Skills' "When not to use" sections may cross-reference deleted skills — clean up those lines with a search.)

## 3. Change skill descriptions (routing)

Routing is driven almost entirely by each skill's `description:` frontmatter. To change what triggers a skill:

1. Edit `skills/<name>/SKILL.md` frontmatter `description`.
2. Keep it *specific*: name concrete trigger conditions ("Kafka consumer lag", "deployment rollback plan") and state boundaries ("Do NOT use for X — use Y instead").
3. Keep descriptions unique — two skills must never claim the same trigger zone.
4. Test: ask a few phrasings in a fresh session; if routing misses, add the missed phrasing's keywords.

If your team uses a stack this plugin doesn't mention, **add the stack to your workflow profile first** — many skills adapt to profile stacks automatically via their Adaptation rules — and only edit descriptions if routing still misses.

## 4. Add or remove skills

- **Add:** follow [`CONTRIBUTING.md`](../CONTRIBUTING.md) (folder, frontmatter, required sections, README + CHANGELOG entries).
- **Remove:** delete `skills/<name>/`; grep `skills/`, `commands/`, and `README.md` for references to it and clean those up; add a CHANGELOG "Removed" entry. Never remove without a one-line reason in the changelog.

## 5. Rename a skill safely

1. Move the folder: `git mv skills/old-name skills/new-name`.
2. Update `name:` in its frontmatter to match the folder.
3. Grep the whole plugin for `old-name` and update every cross-reference (other skills' "When not to use", `commands/*.md` dispatchers, README, CHANGELOG).
4. Add a CHANGELOG entry under **Breaking changes** with a migration note ("`old-name` requests now route to `new-name`").
5. Restart and test the old phrasing still routes.

## 6. Project-specific conventions and team coding standards

Two supported places, by domain:

- **Team/general conventions** → `docs/workflow-profile.md` → *Team conventions* (per team: review culture, PR size, formatting, deploy process). Skills consult this instead of hard-coding rules.
- **Stack-specific checklists** → `references/<topic>-checklist.md` (add a file; skills already read this folder on demand). Keep them project-neutral — secrets, internal URLs, and client names never belong in the plugin.

For private per-project rules, prefer the project's own `CLAUDE.md`/agent instructions file over editing the plugin — the plugin should stay portable.

## 7. Skills stay generic — that's the maintenance rule

The long-term health of the plugin depends on one discipline:

- **Everything about *you* lives in the profile and the three personal context skills.**
- **Everything about *craft* lives in the skills** — workflows, checklists, output contracts — written stack-adaptively (see each skill's Adaptation rules).

If you ever catch a skill hard-coding a job title, a company, a dataset, or a specific thesis, move that fact into the profile and reword the skill generically. `continuous-improvement` enforces exactly this when processing feedback ("skills stay single-responsibility; nothing grows broader or role-hard-coded"), and `skill-health-check` flags violations.
