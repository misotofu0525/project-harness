# Project Harness Agent Kernel

## Purpose

- This repository builds a portable project layer for Codex and Claude Code.
- Keep the root entrypoint small and route to scoped context only when needed.
- The three stable capabilities are Context Routing, Task Continuity, and Verified Completion.

## Always

- Inspect the existing implementation before editing.
- Keep changes scoped to the current request.
- Search before naming APIs, commands, configuration fields, or paths.
- Separate research from implementation until the solution is supported by evidence.
- Keep diffs reviewable and consistent with existing style.
- Never expose secrets, credentials, private keys, or environment values.
- Do not claim completion without fresh verification evidence.

## Context Routing

- For non-trivial work, read `docs/agent/index.md`.
- Load only modules whose `Read when` conditions match the current task.
- Read current code and configuration for facts that are cheap to observe.
- Store only stable, decision-relevant constraints in context modules.
- Do not load every module by default.

## Task Continuity

- Use a Journal for long, research-heavy, cross-session, or compaction-prone work.
- Store one task per `docs/plans/active/<task-id>/` directory.
- Keep `task_plan.md`, `findings.md`, and `progress.md` together.
- Resolve an explicit `PLAN_ID` first.
- If exactly one active Journal exists, it may be restored automatically.
- If several active Journals exist without `PLAN_ID`, report the ambiguity and stop guessing.
- If no active Journal exists, treat ordinary short work as a normal task.

## Checkpoints

- Treat the Journal as durable task memory, not a live task-status service.
- Update Latest Checkpoint after phases, important decisions or discoveries, meaningful failures, pauses, compaction preparation, and finish preparation.
- Do not log every tool call or file write.
- Before a major decision or after stale context, re-read the relevant Journal files.

## Completion

- Use the `finish-task` workflow for Journal-backed delivery.
- Check Done When against observable evidence.
- Run the configured verification commands.
- Review the complete diff for scope, correctness, accidental changes, and secrets.
- Review whether stable project context changed.
- Record verification, diff review, and context review in `progress.md`.
- Archive the Journal only after every finish prerequisite passes.

## Project Boundaries

- Preserve source captures and provenance under `docs/research/sources/`.
- Keep synthesized research under `docs/research/notes/`.
- Keep canonical shared templates and deterministic scripts under `shared/`.
- Keep platform packaging differences under `plugins/`.
- Do not add a database, task manager, orchestration runtime, custom subagent, or user-Home mirror.
- Do not modify live user-Home configuration as part of repository work.

## Platform Adapters

- Keep shared Journal semantics identical across Codex and Claude Code.
- Keep manifests, hook schemas, environment variables, and context injection platform-specific.
- Use SessionStart and PreCompact for restoration and reminders.
- Do not treat ordinary Stop hooks as project-level completion gates.
- Re-sync packaged runtime copies after changing canonical shared assets.

## Verification

- Read `docs/agent/verification.md` before final verification or when checks change.
- Use `.harness.toml` as the machine-readable command source.
- Confirm no temporary planning files exist in the repository root.
- Confirm no stale placeholders or local absolute links remain in distributable files.
