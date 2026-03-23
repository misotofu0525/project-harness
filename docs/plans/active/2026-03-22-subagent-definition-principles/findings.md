# Findings & Decisions

## Requirements
- Capture the discussion as a durable document
- Focus on context-management reasoning
- Make it reusable across projects

## Core Findings
- The most important distinction is between using a subagent for one task and defining a reusable custom subagent role.
- Subagents are best understood as context firewalls that isolate noisy, local, tool-heavy, or skill-heavy work from the main thread.
- Custom roles should be rare and justified by repeated cross-project value, stable boundaries, and a reusable context package.
- A practical first-pass filter is to compare subagent收益 against委派/汇总/协调/冲突成本 before using a subagent at all.
