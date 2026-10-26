# Installing my_skill

## Requirements

| Requirement | Details |
|---|---|
| Claude Code | any recent version with plugin support (`/plugin` command available). No minimum known breakage; if `/plugin` doesn't exist, update Claude Code. |
| Git | required for the clone-based installs (any recent version). |
| Node / Python | **not required** — the plugin is pure Markdown (skills, commands, docs). Skills may *suggest* Docker/Postgres/Kafka tools to run code you're working on, but installing the plugin needs nothing. |

No API keys, no network access, no telemetry — the plugin is offline Markdown.

## 1. Clone

```bash
# from GitHub (adjust owner/repo to wherever the plugin is hosted)
git clone https://github.com/albkue/my_skill.git
cd my_skill
```

## 2. Load the plugin

Choose one of:

### Option A — Local development (`--plugin-dir`)

```bash
claude --plugin-dir /path/to/my_skill
```

Use this for testing or hacking; the plugin loads from the raw folder for that session only.

### Option B — Copy into the plugins directory

```bash
# macOS / Linux
mkdir -p ~/.claude/plugins
cp -r /path/to/my_skill ~/.claude/plugins/

# Windows (PowerShell)
New-Item -ItemType Directory -Force "$env:USERPROFILE\.claude\plugins" | Out-Null
Copy-Item -Recurse C:\path\to\my_skill "$env:USERPROFILE\.claude\plugins\my_skill"
```

### Option C — Plugin marketplace (GitHub-based)

Claude Code plugins can be distributed through a **marketplace repo** — a repository containing a marketplace manifest that lists plugins by GitHub repo.

**If you only want to install:** ask the plugin's author for the marketplace name, then in Claude Code:

```
/plugin marketplace add <github-owner>/<marketplace-repo>
/plugin install my-skill@<marketplace-name>
```

**If you are the author setting this up:** create (or reuse) a repo whose root contains `.claude-plugin/marketplace.json` listing your plugin, e.g.:

```json
{
  "name": "sothy-tools",
  "plugins": [
    {
      "name": "my-skill",
      "source": "./my_skill",
      "description": "Personal engineering toolkit: backend, CV, data, research skills"
    }
  ]
}
```

then push and share with `/plugin marketplace add`. Keep the marketplace manifest in a separate repo from the plugin itself if you plan to version them independently.

## Using with other agents (not just Claude Code)

Claude Code discovers this plugin natively via `.claude-plugin/plugin.json`. Every
other modern agent (Codex, Gemini CLI, Cursor, Zed, OpenCode, …) uses the
[`AGENTS.md`](../AGENTS.md) convention instead:

1. Put this repo anywhere on disk (or at a project's root, for per-project use).
2. Open your agent inside or beneath the folder containing `AGENTS.md` — it will
   auto-read the profile-first rule and the trigger → skill routing index.
3. Ask naturally; the agent reads the matched `skills/<skill-name>/SKILL.md` in full.
4. Edit `docs/workflow-profile.md` to make it yours (see `CUSTOMIZATION.md`).

Note: `/my-skill:*` slash commands are Claude Code–only; other agents get the same
behavior by describing the task in natural language (the AGENTS.md index maps the
phrases for them).

## 3. Verify the plugin is loaded

1. Start (or restart) Claude Code.
2. Run `/plugin` — `my-skill` should be listed and enabled.
3. Run `/my-skill:my-skill` — you should get a menu that asks which context you're working in.
4. Run `/plugin install`-free sanity check: ask "what skills do you have?" and confirm `api-design`, `backend-debugging`, etc. appear.

## 4. Test each major skill

After installing, try one cheap request per skill family — all should return the skill's documented output format:

| Test request | Expected |
|---|---|
| "Review this controller" + paste ~20 lines of Java | `backend-code-review` — severity-ranked findings, verdict |
| "Why is my Kafka consumer lagging?" | `backend-debugging` — hypothesis list, cheapest confirmations first |
| "Design an endpoint to upload part images" | `api-design` — contract with auth/validation/error envelope |
| "Write a test for this function" + paste code | `backend-testing` — behavior-named tests, run commands |
| "Plan a deploy of this Spring Boot service" | `backend-deployment` — checklist, rollback plan, post-launch checks |
| "Set up alerts for my API" | `observability` — symptom-based alerts + runbook |
| "Plan a CDC pipeline project" | `data-engineering` — layered architecture, hands-on next step |
| "Outline my methodology chapter" | `thesis-helper` — asks for drafts, `[cite]` placeholders, no fabrication |
| "Review how my_skill handled my last task" | `continuous-improvement` — feedback questions, then proposed edits |

First-run behavior: skills will read `docs/workflow-profile.md` and may ask you to confirm it — that's expected and good; it's how you personalize the plugin (see `docs/CUSTOMIZATION.md`).

## 5. Update the plugin

```bash
cd /path/to/my_skill
git pull
```

Then restart Claude Code. Read `docs/CHANGELOG.md` — especially **Migration notes** — before upgrading across versions. If you installed via a marketplace, `/plugin` also offers update actions per plugin.

## 6. Uninstall or disable

- **Disable temporarily:** `/plugin` → select `my_skill` → disable (folder and settings stay).
- **Remove (Option B install):** delete `~/.claude/plugins/my_skill` (or the copy in `%USERPROFILE%\.claude\plugins\`).
- **Remove (Option A):** stop launching with `--plugin-dir`.
- **Remove (Option C):** `/plugin uninstall my-skill@<marketplace-name>`, and `/plugin marketplace remove` if you no longer want the marketplace.

Your `docs/lessons-learned.md` and `docs/workflow-profile.md` live *inside* the plugin folder — back those up before removal if you've personalized them.

## Common errors and fixes

| Error | Fix |
|---|---|
| `Plugin not found` after copying | folder must contain `.claude-plugin/plugin.json` at its root; verify the path you copied (`~/.claude/plugins/my_skill`, not `~/.claude/plugins/my_skill/my_skill`) |
| Slash commands don't resolve (`/my-skill:...`) | restart Claude Code so commands are registered; confirm the plugin is enabled in `/plugin` |
| `/my_skill:...` (underscore) unknown command | the namespace is the plugin `name` field — `my-skill` with a hyphen |
| `Skill X not found` right after adding | restart the session; verify `skills/X/SKILL.md` exists with valid frontmatter |
| Plugin fails to load with parse error | `plugin.json` is invalid JSON, or a SKILL.md frontmatter is malformed; validate both |
| Skills all ask me about "internship" | personal context skills installed; see `docs/CUSTOMIZATION.md` step 3 |
