---
name: internship-communication
description: Help Sothy Eng communicate professionally during the Software Developer internship. Use when drafting standup updates, status reports, blocker explanations, clarification requests to the supervisor, code-review request messages, professional emails/messages to the internship team, or internship PR descriptions' human-facing note. Do NOT use for actual implementation work (software-internship), backend-job communication, or interview answers (interview-prep).
version: 1.0.0
author: Sothy Eng
---

# Internship Communication

## Purpose
Draft and polish professional written communication for the internship: short, clear, respectful messages that keep the team informed and make Sothy look reliable.

## When to use
- Asking the supervisor for clarification on a task or requirement.
- Reporting progress ("done", "in progress") in standups or written updates.
- Explaining a blocker or a delay honestly and proactively.
- Requesting code review, or replying to review comments.
- Any professional message, email, or Slack/Teams note to the internship team.
- The human-facing part of PR descriptions for internship work.

## When not to use
- Implementation, debugging, or code changes themselves → `software-internship`.
- Backend part-time job communications → keep out of this skill; treat as `software-internship` style work only if the user confirms it's internship-related, otherwise decline and clarify.
- Theses or academic writing → `thesis-helper`.
- Interview STAR answers → `interview-prep`.

## Context intake
- Audience, channel, and whether the internship context still applies (check `docs/workflow-profile.md`); if it changed, this becomes general professional-work communication and says so.
Detect or confirm before starting (ask at most what is genuinely needed):
- Which context: part-time paid backend work, internship, thesis / final-year project, personal project, or learning? Fall back to the active roles and projects in `docs/workflow-profile.md`; ask when it could be two different contexts.
- What is the desired output: a plan, code, a review, tests, documentation, a deployment plan, or research notes? Confirm if ambiguous.

## Workflow
1. Read the my-skill plugin's `docs/workflow-profile.md`. If it is missing, contradicts this request, or was last updated more than ~3 months ago, confirm or update it with Sothy before applying any role, project, or stack assumptions.
2. Ask for audience, situation, desired outcome, and tone if not provided.
3. Gather the facts; separate facts from interpretation — never invent either.
4. Draft a concise professional message: main point first, facts next, ask/update last.
5. Offer a shorter alternative (many standups need one-liners).
6. Highlight any questions Sothy should be asking but isn't.

## Adaptation rules

- Tone/length altitude adjusts to audience seniority and channel norms; many teams want 2-3 line updates.
- After the internship ends: same drafting discipline for any future workplace communication - the no-invented-facts rule never relaxes.

## Inputs needed
- Audience (supervisor, team lead, whole team) and channel (standup, email, chat, PR comment).
- Situation and facts: what happened, what's done, what's next, when.
- Desired outcome (approval, unblocking, information, review).
- Tone preference and any length constraint (many teams want 2–3 line updates).
- Deadlines or dates involved.

## Output contract
- **Draft message** — complete, ready to send, with subject line for emails.
- **Shorter version** — condensed alternative.
- **Key questions to ask** — anything missing or worth clarifying from the other side.

## Rules and constraints
- Clear, respectful professional English; avoid filler and excessive hedging.
- Keep messages concise — seniors read fast.
- **Do not invent facts about Sothy's work, his team, deadlines, or artifacts.** If a key fact is unknown, leave a clearly marked placeholder like `[what you actually did today]` and say why.
- No blame language when explaining blockers; state the blocker, impact, what was tried, and the proposed path.
- Never include secrets, credentials, or confidential details from either workplace in drafts.
- If the communication could be for the backend part-time job instead, ask which context before drafting.

## Quality checklist

- [ ] No invented facts; unknowns are clearly marked placeholders.
- [ ] Main point first; a shorter alternative provided.
- [ ] Questions Sothy should ask surfaced.
- [ ] No secrets or confidential info in the draft.

## Examples
1. **Request:** "Standup update — I'm stuck on the DB config for the feature."
   **Behavior:** Ask what exactly is stuck and for how long. Draft a 3-line standup update (progress, blocker, attempted steps + proposed ask), a one-liner version, plus the question he should pose to the supervisor (e.g., who owns that config).
2. **Request:** "I'm a day late on my task. How do I tell my lead?"
   **Behavior:** Draft an honest, short, proactive email: current state, exact remaining work, revised ETA, no excuses. Shorter chat version. Key questions: whether to split remaining work or scope down.

## Lessons learned

Record improvements after real usage (maintained via ``continuous-improvement``). Format:

- ``<date>`` -- ``<what happened>`` -> ``<change made to this SKILL.md>``

(empty -- entries appear after real usage)
