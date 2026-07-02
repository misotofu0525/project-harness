# Task Contract: [task-name]

<!-- Use this when you want a reusable task brief or an explicit delegation contract. -->

## Goal
- What needs to change:
- What success looks like:

## Context
- Relevant files, systems, or prior decisions:
- What has already been tried:

## Constraints
- Technical constraint:
- Product or UX constraint:
- Safety or compliance constraint:

## Done When
- Concrete completion signal:
- Required verification evidence:

## Delegation
- Allow built-in subagents: `yes | no`
- Good delegation targets:
- Avoid delegation for:
- Wait behavior: `continue locally | wait for delegated work`

## Notes
- Use concrete delegation language when subagents are allowed.
- A good default is: `Allow built-in subagents for read-heavy exploration, independent verification, and low-coupling sidecar work.`
- This template lowers the cost of explicit delegation; it does not imply automatic subagent spawning.
