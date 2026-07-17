# Task Plan: Project Harness Refactor

## Goal

Refactor this repository into a portable Project Harness for Codex and Claude Code with three stable capabilities: Context Routing, Task Continuity, and Verified Completion.

## Scope

- Preserve task-scoped planning bundles as durable task memory.
- Replace real-time task status and registry concepts with semantic checkpoints and explicit plan resolution.
- Replace the current handbook and managed-home architecture with a tiny kernel, scoped context modules, shared assets, and platform adapters.
- Implement deterministic plan resolution, restoration, verification, context-impact review, and archival.
- Package Codex and Claude Code adapters using their current official plugin formats.
- Preserve research source captures and provenance.

## Constraints

- Do not modify the user Home or install plugins.
- Do not introduce a database, runtime, task manager, orchestration framework, custom subagent, or automatic semantic documentation writer.
- Do not guess the current task by modification time.
- Do not block every turn-ending Stop event merely because an active Journal exists.
- Use Python 3.11+ standard-library `unittest` if no existing test framework is present.
- Keep changes reviewable and prefer moves for durable assets where practical.
- Do not perform broad restructuring until the discovery comparison is recorded in `findings.md`.

## Phases

### Phase 1: Discovery and Current Official Contracts

- [x] Inventory current repository structure, planning implementation, hooks, skills, docs, and task registry.
- [x] Compare the local planning adaptation with current `OthmanAdi/planning-with-files`.
- [x] Verify current Codex and Claude Code plugin, hook, and instruction behavior against official documentation.
- [x] Record retained differences, absorbed upstream behavior, upgrade candidates, licensing, and attribution.
- **Status:** complete

### Phase 2: Target Design and Migration Map

- [x] Freeze the target directory and responsibility map.
- [x] Map current assets to `shared/`, `plugins/`, `docs/agent/`, tests, or retirement.
- [x] Define the first-version `.harness.toml` contract and deterministic script interfaces.
- [x] Define semantic checkpoint and explicit finish transaction behavior.
- **Status:** complete

### Phase 3: Shared Core and Task Continuity

- [x] Add shared templates and deterministic scripts.
- [x] Implement explicit `PLAN_ID`, unique-active auto-resolution, ambiguity failure, and no-active short-task behavior.
- [x] Implement checkpoint restoration, verification, context-impact review, and archival.
- [x] Remove `memory/active-tasks.json` and migrate useful planning assets from `system/codex-home`.
- **Status:** complete

### Phase 4: Context Routing, Completion Skill, and Platform Adapters

- [x] Replace root `AGENTS.md` with a 60-100 line kernel/router.
- [x] Add `docs/agent/index.md` and only the context modules this repository needs.
- [x] Implement `setup-project`, `task-memory`, and `finish-task` skills.
- [x] Add valid Codex and Claude Code plugin manifests and lifecycle hooks.
- [x] Remove `docs_syncer` and replace its useful responsibility with finish-time Project Context Review.
- [x] Rewrite `README.md` and add `DESIGN.md`; retire redundant current-doc architecture.
- **Status:** complete

### Phase 5: Tests, Verification, and Explicit Finish

- [x] Cover the 19 requested structural and behavioral checks.
- [x] Validate both plugin manifests and all skills.
- [x] Run fast and full verification plus `git diff --check`.
- [x] Review the complete diff and resolve context-impact findings.
- [x] Record fresh evidence and archive this bundle through the finish workflow.
- **Status:** complete

## Decisions

| Decision | Rationale |
|----------|-----------|
| Use `2026-07-17-project-harness-refactor` as the explicit `PLAN_ID` | Multiple legacy active bundles exist, so automatic resolution must not guess. |
| Keep this work single-agent | The task contract forbids new custom subagents and does not grant built-in delegation permission. |
| Treat upstream discovery as a gate before migration | The requested design explicitly requires evidence before broad refactoring. |
| Keep `docs/plans/active/` and reject active-pointer/mtime fallback | The repository's task isolation is a valuable local policy; an explicit id or unique active bundle is deterministic. |
| Reuse concepts, not upstream session transcript parsing | Official Codex documentation states that transcript format is not a stable hook interface. |
| Omit a Stop hook in the first release | Both platforms define Stop at turn scope, while task completion is an explicit Journal transaction. |
| Generate self-contained adapter copies from canonical shared assets | Plugins must remain installable while shared templates and deterministic scripts retain one authored source of truth. |
| Nest each distributable as `plugins/<platform>/project-harness/` | The platform directory remains explicit while the actual plugin root matches the `project-harness` manifest name. |
| Require recorded verification, diff review, and context review before archival | Mechanical checks can enforce completion evidence without turning the Journal into a live task state machine. |

## Done When

- [x] The repository describes and implements Project Harness around Context Routing, Task Continuity, and Verified Completion.
- [x] Task Journals are isolated, checkpoint-based, deterministically resolved, and archived only by explicit completion.
- [x] `memory/active-tasks.json`, `docs_syncer`, and the managed user-Home mirror are retired without modifying the live Home.
- [x] Shared templates/scripts and both platform adapters exist, validate, and do not invent a cross-platform runtime.
- [x] README, DESIGN, the tiny AGENTS kernel, and scoped context modules agree with the implemented repository.
- [x] All 19 requested checks pass, along with manifest/skill validation and `git diff --check`.
- [x] The task bundle records passed verification, diff review, and Project Context Review evidence required by the explicit archive transaction.

## Verification

- `python3 -m unittest discover -s tests -v`
- Codex plugin validation using the current `plugin-creator` validator.
- Skill validation using the current `skill-creator` validator.
- Repository fast/full commands from `.harness.toml` and `docs/agent/verification.md`.
- `git diff --check`
- Repository scan for forbidden absolute local links and retired paths/registrations.
