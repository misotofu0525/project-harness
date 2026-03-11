# Findings & Decisions

## Requirements
- Review `https://github.com/runesleo/claude-code-workflow`.
- Combine that review with:
- the saved article `how-to-be-a-world-class-agentic-engineer.md`
- the saved paper `2512.05470-everything-is-context.md`
- Produce a synthesized view oriented toward improving Codex usage.

## Research Findings
- The earlier article emphasizes minimal stacks, context control, separated research/implementation, explicit completion contracts, and iterative rules/skills cleanup.
- The paper emphasizes treating context as governed infrastructure with persistent `history`, `memory`, `scratchpad`, metadata, lineage, and an explicit constructor/updater/evaluator pipeline.
- Current task needs comparison across three layers: tactical workflow, persistent context architecture, and Codex-specific feasibility.
- `claude-code-workflow` is explicitly designed as a three-layer context system:
- Layer 0 always-loaded rules
- Layer 1 on-demand docs
- Layer 2 hot working-state memory
- The repo strongly emphasizes `verification before completion`, `auto-save/memory flush`, `SSOT`, and model/task routing.
- The repo is not just a single `CLAUDE.md`; it is a structured workflow package containing rules, docs, skills, agents, commands, and memory templates.
- The top-level `CLAUDE.md` acts as a router/index rather than a giant instruction dump. This aligns with the article's advice to keep the root file as a context directory.
- `rules/behaviors.md` encodes hard routing and operating constraints: deployment rules, debugging protocol, quality control triggers, memory-search triggers, and atomic commit expectations.
- The repo assumes Anthropic/Claude-specific capabilities such as `memory_add`, `memory_search`, model tiers like Sonnet/Opus/Haiku, and a `CLAUDE.md` global home config layout.
- `rules/skill-triggers.md` turns skills into event-driven policies:
- bug/error -> `systematic-debugging`
- before completion -> `verification-before-completion`
- exit signal -> `session-end + memory-flush`
- complex >5-file task -> suggest `planning-with-files`
- `rules/memory-flush.md` treats persistence as automatic, not user-triggered. This is a strong operationalization of "don't lose context on exit".
- `docs/agents.md` defines a hub-and-spoke multi-model workflow with Claude as coordinator and Codex as verifier/reviewer for selected tasks.
- The repo constrains external model writes through an interface contract (`PROJECT_CONTEXT.md` handoff block only), which is a concrete governance mechanism rather than a soft preference.
- `skills/verification-before-completion/SKILL.md` is the repo's strongest rule: no claim without fresh verification evidence in the current message.
- `skills/systematic-debugging/SKILL.md` encodes a deterministic debugging flow: recall -> root cause -> pattern -> hypothesis -> implementation.
- `skills/session-end/SKILL.md` closes the loop by updating hot memory (`today.md`), goals/projects status, task registry, handoff block, and optionally committing.
- `commands/review.md` shows the pattern is not just memory-heavy; it also packages review preparation into reusable command workflows.
- The memory templates are intentionally lightweight:
- `today.md` = daily working memory / handoff log
- `projects.md` = cross-project summary index
- `goals.md` = tactical + strategic goal stack
- `active-tasks.json` = cross-session in-flight registry
- Compared with the paper, the repo has clear `hot data` and task-state layers, but it does not yet present a full `history / memory / scratchpad / evaluator` architecture with lineage and replay semantics.
- The repo is closer to a pragmatic operating workflow than to a full context platform. That is a strength for usability, but also its architectural limit.
- A unified synthesis document was created to reorganize all experiences by dimensions instead of by source.
- The best overall synthesis is:
- article -> tactical rules for keeping a single task clean
- repo -> operational workflow for repeatability
- paper -> architectural model for persistent, governed context systems
- The strongest transferable pattern set across all three sources is:
- root file as router
- layered context loading
- explicit task contracts
- hard verification gate
- lightweight hot-state persistence
- strict write boundaries
- eventual move toward governed `history/memory/scratchpad`

## Technical Decisions
| Decision | Rationale |
|----------|-----------|
| Store cross-source synthesis in markdown files first | Keeps the research auditable and resumable |
| Treat the GitHub repo as a workflow pattern library, not as truth | Need to test ideas against article and paper, not just summarize repo marketing |
| Inspect actual repo files after README | Need to verify which ideas are really encoded in rules vs only advertised |
| Focus comparison on transferability to Codex | Many repo mechanisms are clearly Claude-specific, so value depends on what survives translation |

## Issues Encountered
| Issue | Resolution |
|-------|------------|
| No prior session catchup output was returned | Proceeded with fresh planning files |

## Resources
- Article summary file: `/Users/misotofu/Documents/workspace/context-engineering/docs/research/sources/how-to-be-a-world-class-agentic-engineer.md`
- Paper full text: `/Users/misotofu/Documents/workspace/context-engineering/docs/research/sources/2512.05470-everything-is-context.md`
- Paper Chinese summary: `/Users/misotofu/Documents/workspace/context-engineering/docs/research/notes/2512.05470-summary.zh.md`
- Target repo: `https://github.com/runesleo/claude-code-workflow`
- Repo local snapshot: `/tmp/ccw.MHvfKr`
- Repo README: `https://raw.githubusercontent.com/runesleo/claude-code-workflow/HEAD/README.md`
- Repo CLAUDE.md: `https://raw.githubusercontent.com/runesleo/claude-code-workflow/HEAD/CLAUDE.md`
- Repo behaviors: `https://raw.githubusercontent.com/runesleo/claude-code-workflow/HEAD/rules/behaviors.md`
- Repo skill triggers: `/tmp/ccw.MHvfKr/rules/skill-triggers.md`
- Repo memory flush: `/tmp/ccw.MHvfKr/rules/memory-flush.md`
- Repo agents doc: `/tmp/ccw.MHvfKr/docs/agents.md`
- Repo task routing doc: `/tmp/ccw.MHvfKr/docs/task-routing.md`
- Repo verification skill: `/tmp/ccw.MHvfKr/skills/verification-before-completion/SKILL.md`
- Repo debugging skill: `/tmp/ccw.MHvfKr/skills/systematic-debugging/SKILL.md`
- Repo session-end skill: `/tmp/ccw.MHvfKr/skills/session-end/SKILL.md`
- Repo review command: `/tmp/ccw.MHvfKr/commands/review.md`
- Unified synthesis doc: `/Users/misotofu/Documents/workspace/context-engineering/docs/research/notes/context-engineering-experience-map.zh.md`

## Visual/Browser Findings
- None yet.

---
*Update this file after every 2 view/browser/search operations*
