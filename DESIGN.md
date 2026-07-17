# Project Harness Design

Project Harness is a portable project layer, not an agent runtime. It connects three stable capabilities around the existing coding-agent loop.

## Context Routing

The root instruction file is a small kernel. It points non-trivial tasks to `docs/agent/index.md`, whose entries state when a scoped context module is relevant. Modules store only stable, decision-relevant facts that are expensive or risky to rediscover.

This avoids turning permanent instructions into a copy of the repository tree, package manifest, branch state, or API inventory.

## Task Continuity

Each durable task owns one Journal directory with plan, findings, and progress files. The plan defines the goal, scope, constraints, phases, decisions, Done When, and verification. Findings preserve decision-changing evidence. Progress keeps the Latest Checkpoint and finish evidence.

Resolution is deliberately strict:

1. explicit `PLAN_ID` or `--plan-id`;
2. exactly one Journal under `active/`;
3. ambiguity error for several Journals;
4. no Journal for zero active tasks.

SessionStart restores a compact projection, not the complete files. PreCompact reminds without guessing or writing semantic state. Checkpoints occur at semantic boundaries rather than after operations.

## Verified Completion

An agent's belief that implementation is done is only the start of the finish transaction. The transaction checks Done When, executes `.harness.toml` verification, reviews the complete diff, reviews stable context impact, records evidence, and moves the Journal to `completed/`.

The move is monotonic and is the only lifecycle state transition:

```text
docs/plans/active/<task-id>
→ docs/plans/completed/<task-id>
```

No live `running`, `waiting`, or `complete` field needs synchronization with a platform session.

## Runtime loop

```text
Route context
→ Restore Journal
→ Act
→ Observe environment feedback
→ Checkpoint at a semantic boundary
→ Explicitly verify and finish
```

## Shared core and adapters

Canonical templates and deterministic Python scripts live under `shared/`. A sync script materializes them into self-contained Codex and Claude Code plugin packages. Tests reject drift between canonical and packaged copies.

Adapters own only platform contracts: manifest location, hook schema, plugin-root environment variables, and context-output behavior. V1 uses SessionStart and PreCompact and omits Stop hooks.

## Deliberate exclusions

Project Harness does not provide a database, vector memory, task manager, multi-agent orchestration framework, autonomous loop, automatic semantic documentation writer, custom subagent, user-Home mirror, or cross-platform runtime.
