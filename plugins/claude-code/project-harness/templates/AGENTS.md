# Project Agent Kernel

## Always

- Inspect the existing implementation before editing.
- Keep changes scoped to the current request.
- Do not invent commands, paths, APIs, or project facts.
- Do not expose secrets or credentials.
- Do not claim completion without fresh verification evidence.

## Context Routing

- For non-trivial work, read `docs/agent/index.md`.
- Load only modules whose `Read when` conditions match the task.
- Prefer current code and configuration for facts that are cheap to observe.
- Keep durable context modules limited to stable constraints and decision-relevant facts.

## Task Continuity

- Use a task Journal for long, research-heavy, cross-session, or compaction-prone work.
- Store each Journal under `docs/plans/active/<task-id>/` with `task_plan.md`, `findings.md`, and `progress.md`.
- Resolve an explicit `PLAN_ID` first; otherwise use the Journal only when exactly one active task exists.
- If multiple active Journals exist and no `PLAN_ID` is set, stop and identify the ambiguity.
- Update the Latest Checkpoint at semantic boundaries, not after every tool call.

## Completion

- Before final delivery, use the `finish-task` workflow for Journal-backed work.
- Check Done When, run configured verification, review the diff, and review project-context impact.
- Archive a Journal only after the completion checks have recorded evidence.
