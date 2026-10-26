---
name: <skill-name>
description: <One or two sentences - what it does, concrete trigger conditions, and a "Do NOT use" boundary routing the nearest conflicting skill. This is the routing surface; make it specific enough to trigger on its own.>
version: 1.0.0
author: Sothy Eng
---

# <Skill Title>

## Purpose
<What problem it solves - one or two sentences.>

## When to use
- <Concrete trigger: "Kafka consumer lag", "design a new endpoint", ...>
- <Concrete trigger>
- <Concrete trigger>

## When not to use
- <Boundary, routing to the neighboring skill by name: "X → `<skill>`".>

## Context intake
- <What to detect or ask first. Workflow step 1 must read the workflow profile.>

## Workflow
1. Read the my-skill `<docs/workflow-profile.md>`. If it is missing, contradicts this request, or was last updated more than ~3 months ago, confirm or update it with the user before applying any role, project, or stack assumptions.
2. <Step>
3. <Step>  
4. <Steps are ordered; each has an exit or an output.>

## Adaptation rules
- <How behavior shifts for different stacks/teams/project types - keep reusable, never hard-code one person's job.>

## Inputs needed
- <Files/facts required from the user. Distinguish must-have from nice-to-have.>

## Output contract
1. <Deliverable section 1>
2. <Deliverable section 2>
3. <What "done" looks like, stated as checkable conditions.>

## Rules and constraints
- <Hard guardrails: no fabrication, no secrets, etc.>

## Quality checklist
- [ ] <Falsifiable item - technical conditions must hold.>

## Lessons learned

Record improvements after real usage (maintained via `continuous-improvement`). Format:

- `<date>` — `<what happened>` → `<change made to this SKILL.md>`

(empty — entries appear after real usage)

## Examples
1. **Request:** <short worked request>
   **Behavior:** <what the skill delivers, in one or two lines>
2. **Request:** <near-miss request - routes elsewhere>
   **Behavior:** <which skill it routes to and why>
