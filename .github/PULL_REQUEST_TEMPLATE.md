---
name: pull-request
about: Contribute a change to my_skill
title: "[type] short summary"
labels: ""
---

## What does this PR add or change?

<!-- One short paragraph. Link any related issue. -->

## Which skill is affected?

<!-- skills/<name> — or "none / docs only" -->

## Why is this change useful?

<!-- The repeated gap or real usage evidence that motivates it. -->

## How was it tested?

<!-- e.g. launched with `claude --plugin-dir`, routed request X to skill Y, verified the output contract -->

## Checklist

- [ ] `plugin.json` is valid (and only edited if manifest scope changed)
- [ ] `SKILL.md` has valid YAML frontmatter (`name`, `description`, `version`, `author`)
- [ ] Skill name is unique, lowercase, hyphenated, matches the folder
- [ ] README updated (skill table / structure)
- [ ] `docs/CHANGELOG.md` updated
- [ ] No secrets, internal URLs, or confidential details in any changed file
- [ ] Local test completed (skill triggers, near-miss routing works)

<!-- Every checked box should be verifiable by the reviewer. -->
