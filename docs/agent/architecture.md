# Architecture

## Read when

- changing shared script boundaries or Journal semantics
- changing repository layout or lifecycle flows
- adding a new durable capability

## Stable context

- Project Harness owns project templates, deterministic Journal scripts, two platform adapters, tests, and preserved research.
- `shared/` is the canonical authored source for templates and deterministic scripts.
- Each distributable plugin is self-contained; generated copies must remain byte-identical to canonical shared assets.
- Context Routing, Task Continuity, and Verified Completion are the only top-level capabilities.
- A Journal is resolved by explicit id or unique active directory and archived through one active-to-completed move.
- Hooks restore or remind; they do not infer semantic state or parse transcript internals.
- Platform adapters do not create a cross-platform runtime.

## Update when

- shared/plugin ownership changes
- Journal resolution or archival semantics change
- a new top-level capability or state source is proposed
