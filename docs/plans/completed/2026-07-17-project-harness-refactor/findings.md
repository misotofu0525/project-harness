# Findings: Project Harness Refactor

## Requirements

- Preserve the three-file Journal and per-task isolation.
- Recast planning files as checkpointed Durable Task Memory, not a real-time status machine.
- Resolve active Journals by explicit `PLAN_ID`, unique active directory, ambiguity error, then no-Journal short-task behavior.
- Build a tiny context router before the Journal and an explicit verified finish transaction after it.
- Support Codex and Claude Code through thin platform adapters over shared semantics, templates, and scripts.
- Retire the duplicate task registry, `docs_syncer`, and the managed user-Home mirror.
- Do not alter preserved research source captures or their provenance.

## Initial Repository Facts

- The working tree began clean on `main`, which is three commits ahead of `origin/main`.
- Nine legacy task bundles remain under `docs/plans/active/`; therefore implicit unique-task resolution cannot select this refactor.
- Current project state is split across root `AGENTS.md`, four `handbook/` current docs, `.codex/`, `memory/active-tasks.json`, and `system/codex-home/`.
- The existing global `planning-with-files` skill already uses task-scoped directories and includes a resolver, session recovery, Pre/Stop-style behavior, and operation-level reminders.
- The existing `current-docs-sync` skill has reusable change-surface and minimal-update logic, but assumes the handbook architecture that this task will retire.

## Upstream Comparison

- Current upstream inspected: `OthmanAdi/planning-with-files` v3.5.1 at commit `f90780c92f0506d21c5f6c4865ce95517a8b1964`, dated 2026-07-14.
- Upstream has now absorbed the original isolation concern through slug-mode directories under `.planning/<task-id>/`, explicit `PLAN_ID`, an `.active_plan` pointer, and active-plan-aware hooks.
- Upstream resolution is still broader than this Harness should adopt: `PLAN_ID` -> `.active_plan` -> newest directory by mtime -> legacy root files. The desired Harness intentionally removes the pointer, mtime guessing, and legacy root mode.
- Upstream includes Codex `SessionStart`, `PreCompact`, and `Stop` adapters plus Claude Code hook declarations. It also retains operation-level reminders, legacy per-tool plan injection, and the two-action logging rule.
- Upstream v3 autonomous/gated modes make per-tool injection optional and make hard Stop gating opt-in. Its changelog explicitly records the design lesson that an incomplete plan alone must not block a session.
- Upstream `session-catchup.py` directly parses Codex and Claude transcript stores. This repository should not adopt that implementation because Codex documents `transcript_path` as convenient but not a stable hook interface.
- Upstream also contains attestation, autonomous loops, multi-agent ledgers, active pointers, and broad multi-agent/runtime adapters. Those are useful upstream features but explicit non-goals for this focused Project Harness.
- Upstream is MIT licensed. Any directly adapted implementation or template requires retained MIT attribution; the current plan is to retain a concise attribution notice even where code is newly implemented from the narrower contract.

### Local Value to Preserve

- `docs/plans/active/<task-id>/` and `docs/plans/completed/<task-id>/` encode lifecycle directly and keep durable project history visible.
- The task-scoped bundle is already the repository's canonical practice and does not need `.planning/.active_plan` as a second state source.
- Historical active bundles are not safe to rewrite or archive by inference; several have delivery-only steps left open even though implementation is complete.

### Thin Adaptation to Implement

- Resolve only explicit `PLAN_ID` or a unique active Journal.
- Restore only task id, goal, Latest Checkpoint, next action, and file paths.
- Use `SessionStart` and `PreCompact` without parsing transcripts.
- Keep semantic checkpoints and explicit finish/archive behavior.
- Retain upstream attribution while replacing operation-by-operation logging and Stop gating.

## Official Platform Contracts

- Codex builds the `AGENTS.md` instruction chain once per run and stops adding instruction files at `project_doc_max_bytes` (32 KiB by default). A small root router plus selectively loaded modules is aligned with that contract.
- Codex hooks are discovered from active config layers and enabled plugins. Installed plugins can use the default `hooks/hooks.json`; project-local hooks require project trust.
- Codex `SessionStart` receives `startup`, `resume`, `clear`, or `compact`, and plain stdout becomes developer context. This supports a compact Journal restore without transcript parsing.
- Codex `PreCompact` is turn-scoped and ignores plain stdout. A lightweight reminder must therefore use supported JSON output; it must not block compaction or pretend to perform a semantic checkpoint automatically.
- Codex `Stop` is turn-scoped, receives `stop_hook_active`, and expects JSON. It is not a task-level final-delivery event.
- Codex plugins require `.codex-plugin/plugin.json`, may package skills at plugin root, and automatically discover `hooks/hooks.json`. The manifest need not declare `hooks` when the default path is used.
- Claude Code reads `CLAUDE.md`, not `AGENTS.md`, but officially supports `@AGENTS.md` import. `.claude/rules/` supports `paths` frontmatter so conditional rules load only for matching files.
- Claude Code plugins keep only `plugin.json` under `.claude-plugin/`; `skills/` and `hooks/hooks.json` live at plugin root.
- Claude Code `SessionStart` covers startup/resume/clear/compact and can inject compact context. `PreCompact` and `Stop` are also turn-loop events; Stop runs after the main agent finishes a response and has loop guards.
- Both adapters should therefore share Journal semantics and deterministic scripts while keeping manifest, hook output, environment-variable, and context-injection details platform-specific.

## Migration Map

| Current asset | Target | Treatment |
|---------------|--------|-----------|
| `AGENTS.md` | `AGENTS.md` | Rewrite as a 60-100 line kernel/router. |
| `handbook/PROJECT_CONTEXT.md` | `README.md`, `docs/agent/index.md` | Migrate user-facing and routing facts; retire duplicate current-state handoff. |
| `handbook/ARCHITECTURE.md` | `DESIGN.md`, `docs/agent/architecture.md` | Split conceptual design from scoped stable project context. |
| `handbook/GOLDEN_PRINCIPLES.md` | `DESIGN.md` or kernel invariants | Keep only principles that remain operationally necessary. |
| `handbook/VERIFICATION.md` | `docs/agent/verification.md`, `.harness.toml`, tests | Make verification executable and scoped. |
| `.codex/config.toml`, `.codex/agents/docs_syncer.toml` | none | Remove project-local custom subagent configuration. |
| `memory/active-tasks.json` | Journal checkpoint | Delete duplicate task registry. |
| `system/codex-home/project-scaffolds/` | `shared/templates/` | Migrate only relevant Project Harness templates. |
| `system/codex-home/skills/current-docs-sync/` | `finish-task` Project Context Review | Retain change-surface and minimal-update logic, not the handbook-specific skill. |
| `system/codex-home/AGENTS.md` and README | README migration note | Retire the user-Home mirror without touching live Home files. |
| `docs/research/sources/` | unchanged | Preserve source text and provenance. |
| `docs/research/notes/` and index | unchanged except routing/index references | Preserve durable research synthesis. |
| `docs/plans/` | unchanged lifecycle root | Keep historical Journals and use explicit archive transaction. |

## V1 Interface Contract

### Repository Configuration

`.harness.toml` contains only:

- `version = 1`
- `task_root = "docs/plans"`
- `context_index = "docs/agent/index.md"`
- `[verification].fast` as an array of shell commands
- `[verification].full` as an array of shell commands

No path DSL, status registry, or automatic documentation policy is encoded in configuration.

### Deterministic Scripts

- `resolve-plan.py`: validate an explicit CLI/environment `PLAN_ID`; otherwise select exactly one child under `<task_root>/active`; report ambiguity with task ids; return no selection for zero active tasks. Never use mtime.
- `restore-plan.py`: use the resolver and emit only task id, Goal, Latest Checkpoint fields, next action, and the three Journal paths. It also supports hook stdin so lifecycle adapters do not inspect transcripts.
- `context-impact.py`: inspect changed file paths and suggest which existing context modules may need review. It never writes semantic documentation.
- `verify-task.py`: run configured fast/full verification commands, require the explicit plan when multiple Journals exist, and optionally record exact results in `progress.md`.
- `archive-plan.py`: require checked Done When criteria plus recorded verification, diff review, and Project Context Review before a monotonic move to `completed/`.
- `sync-plugin-runtime.py`: copy canonical templates and deterministic scripts into both self-contained platform packages and make parity testable.

### Script Exit Semantics

- Resolved or intentionally no active Journal: exit 0.
- Invalid or missing explicit `PLAN_ID`, or ambiguous active Journals: exit 2 with an actionable message.
- Failed verification or incomplete finish prerequisites: exit 1 with concrete evidence.
- Existing completed destination or unsafe path containment: fail without moving files.

## Checkpoint and Finish Contract

- `progress.md` begins with `Latest Checkpoint`; it is updated at semantic boundaries only.
- SessionStart restoration never injects the full progress log or findings file.
- PreCompact only reminds; it neither writes a guessed checkpoint nor blocks compaction.
- `Done When` is an explicit checklist in the task plan.
- `progress.md` contains separate finish evidence sections for Verification, Diff Review, and Project Context Review. These are completion records, not live task status.
- Project Context Review accepts `no-impact`, `updated`, or a documented `follow-up`; a missing or pending review blocks archival.
- Archival is the only task lifecycle state change: `active/<task-id>` to `completed/<task-id>`.

## Distribution Contract

- Canonical authored assets live under `shared/`.
- Distributable roots live at `plugins/codex/project-harness/` and `plugins/claude-code/project-harness/`, so each plugin root and manifest name agree.
- A deterministic sync script materializes canonical templates and runtime scripts into each plugin. Tests enforce parity to prevent drift.
- Platform adapters own only manifest schema, hook configuration, hook output shape, and platform-specific installation guidance.
- V1 includes SessionStart and PreCompact hooks and deliberately omits Stop hooks.

## Risks

- Plugin and hook schemas are current-product surfaces and must be verified rather than inferred from saved repository research.
- Existing active bundles may be historically complete but are user-owned records; this task must not silently archive or rewrite them.
- Codex plugin validation may distinguish manifest support from convention-based hook discovery; the adapter must follow validated current behavior.

## Sources

- User-provided design and migration contract in the current task.
- Current repository files and git state.
- `https://github.com/OthmanAdi/planning-with-files` at v3.5.1.
- `https://developers.openai.com/codex/hooks/`.
- `https://developers.openai.com/codex/guides/agents-md/`.
- `https://learn.chatgpt.com/docs/build-plugins`.
- `https://code.claude.com/docs/en/memory`.
- `https://code.claude.com/docs/en/plugins`.
- `https://code.claude.com/docs/en/hooks`.
