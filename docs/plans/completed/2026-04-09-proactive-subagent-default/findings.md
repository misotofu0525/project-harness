# Findings: Reframe proactive subagent usage under current Codex constraints

## Confirmed facts
- Project-local `.codex/config.toml` currently contains only:
  - `[agents]`
  - `max_threads = 4`
  - `max_depth = 1`
- The managed and live global `AGENTS.md` files currently say to use subagents when they help, but they do not encode an explicit default delegation contract for common task shapes.
- The project `AGENTS.md` says to prefer built-in roles and keep only `docs_syncer` as the custom role surface.
- The current research note still leans toward "`spawn subagent` should be relatively common" as a qualitative recommendation.

## Official verification
- Date verified: 2026-04-09
- Source: OpenAI Developers, "Subagents"
- Current official statement: Codex does not spawn subagents automatically and should only use subagents when the user explicitly asks for subagents or parallel agent work.
- Practical implication: repository guidance cannot reliably make Codex auto-delegate in the absence of an explicit delegation request.

## Working diagnosis
- The current repo guidance has a strong theory for why subagents are useful, but it stops at principle level.
- The repo does not currently provide a lightweight task contract or trigger language that helps users or parent agents convert an ordinary task into an explicit delegation request.
- Because the product itself requires explicit triggering, the gap is partly product-level and partly workflow-level.

## Likely remediation shape
- Update the policy language so it distinguishes:
  - product limitation: no automatic spawn
  - workflow objective: reduce friction to explicit delegation
- Add a reusable delegation contract or prompt pattern that makes "please parallelize when useful" part of the normal task framing.
- Keep custom roles minimal; solve this mostly with policy, scaffolds, and examples rather than new repo-local agent definitions.

## Implemented remediation
- Updated the managed and live global `AGENTS.md` files so the stable cross-project rule now says:
  - current Codex behavior requires explicit delegation triggers
  - when delegation would help but permission is missing, ask for a short opt-in instead of silently staying single-threaded
  - an explicit task contract can serve as that permission boundary
- Updated the repository `AGENTS.md` with the same repo-level operating model and a recommended `Delegation:` field.
- Added a shared `task-contract.template.md` scaffold to both the managed and live project-scaffold directories.
- Updated the shared scaffold bootstrap docs and project `AGENTS` template so future repos inherit this pattern.
- Updated current docs, research notes, and cross-session task memory to reflect the new model.

## Verification evidence
- `diff -u system/codex-home/AGENTS.md ~/.codex/AGENTS.md` -> clean
- `diff -ru system/codex-home/project-scaffolds ~/.codex/project-scaffolds` -> clean
- `rg -n -P '^((?!rg -n).)*(\\[project-name\\]|\\[path-or-none\\]|\\[task-name\\]|\\[TODO:)' AGENTS.md handbook .codex docs memory system/codex-home --glob '!system/codex-home/project-scaffolds/**'` -> no matches
- `find . -maxdepth 1 -type f | sort` -> root stays thin
