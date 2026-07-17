# Project Harness

> A portable project layer for Codex and Claude Code.

Project Harness installs a small, reviewable layer into a real code repository. It does not replace the coding agent or create a new runtime. It connects three capabilities that are otherwise easy to implement inconsistently.

## The three capabilities

### Context Routing

A tiny root `AGENTS.md` acts as a kernel and router. `docs/agent/index.md` lists scoped project-context modules and the conditions for reading them. Modules contain stable constraints, invariants, and authoritative sources that cannot be inferred cheaply from code.

### Task Continuity

Long tasks use a three-file Journal:

```text
docs/plans/active/<task-id>/
├── task_plan.md
├── findings.md
└── progress.md
```

Each task has its own directory. Resolution is deterministic: explicit `PLAN_ID`, then exactly one active Journal, then a clear ambiguity error. No registry, active pointer, or modification-time guess is involved.

`progress.md` begins with a compact Latest Checkpoint. SessionStart restores the task id, goal, checkpoint, next action, and Journal paths. PreCompact emits a lightweight reminder. Neither hook parses private transcript formats.

### Verified Completion

Completion is an explicit transaction:

```text
check Done When
→ run project verification
→ review the diff
→ review stable context impact
→ record evidence
→ move active/<task-id> to completed/<task-id>
```

Ordinary Stop hooks are not completion gates because both Codex and Claude Code expose them at turn scope.

## When to use a Journal

Use one for work that is long, research-heavy, spans sessions, is likely to compact, or has important failed approaches and evidence worth preserving.

Skip it for quick questions, simple lookups, and small edits that can be completed safely in one short session. Installing Project Harness does not create a Journal automatically.

## Installed project layer

The setup workflow creates or merges only the files a project needs:

```text
target-project/
├── AGENTS.md
├── CLAUDE.md
├── .harness.toml
└── docs/
    ├── agent/
    │   ├── index.md
    │   └── verification.md
    └── plans/
        ├── active/
        └── completed/
```

Additional context modules are added only when stable project knowledge justifies them. Claude path-specific rules are optional and must include `paths` frontmatter.

## Repository layout

- `shared/templates/`: canonical project and Journal templates.
- `shared/scripts/`: deterministic setup, resolution, restoration, verification, impact, and archive logic.
- `plugins/codex/project-harness/`: self-contained Codex plugin package.
- `plugins/claude-code/project-harness/`: self-contained Claude Code plugin package.
- `tests/`: behavioral, structural, and distribution-contract tests.
- `docs/research/`: preserved research sources and durable notes.
- `docs/plans/`: active and completed task Journals.

Canonical shared assets are mechanically synchronized into both plugin packages. This keeps each plugin installable without creating a new cross-platform runtime.

## Codex

The Codex adapter uses `.codex-plugin/plugin.json`, three skills, and the default `hooks/hooks.json` lifecycle path. SessionStart plain output restores compact developer context. PreCompact returns supported JSON rather than plain text, which Codex ignores for that event.

Validate it with the current `plugin-creator` validator before distribution. Plugin hooks still require the normal Codex trust review when installed.

## Claude Code

The Claude Code adapter uses `.claude-plugin/plugin.json`, plugin-root skills, and `hooks/hooks.json`. Installed projects use a thin `CLAUDE.md` with `@AGENTS.md`; optional `.claude/rules/` files remain path-scoped.

For local development, load the adapter with:

```bash
claude --plugin-dir ./plugins/claude-code/project-harness
```

## Configuration

`.harness.toml` intentionally has a small surface:

```toml
version = 1
task_root = "docs/plans"
context_index = "docs/agent/index.md"

[verification]
fast = ["project-fast-check"]
full = ["project-lint", "project-test"]
```

Setup must replace example commands with verified project commands. There is no workflow DSL.

## Migration from the earlier repository design

This repository previously treated handbook currentness, a JSON task registry, a custom `docs_syncer`, and a versioned user-Home mirror as separate workflow surfaces. Project Harness retires those duplicate sources:

- stable project knowledge moves to scoped `docs/agent/` modules;
- task state lives only in task Journals;
- context impact becomes a finish-time review;
- shared assets live under `shared/` and platform packages under `plugins/`;
- live user-Home configuration is outside repository ownership.

The canonical GitHub repository is `misotofu0525/project-harness`; local checkouts should use `https://github.com/misotofu0525/project-harness.git` for `origin`.

## Attribution

The three-file working-memory approach was informed by [OthmanAdi/planning-with-files](https://github.com/OthmanAdi/planning-with-files). Project Harness retains the locally valuable task-scoped directory design while intentionally narrowing plan resolution, recovery, and completion behavior. See `THIRD_PARTY_NOTICES.md` for MIT attribution.
