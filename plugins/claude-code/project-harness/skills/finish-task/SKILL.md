---
name: finish-task
description: Execute the explicit Project Harness completion transaction for a Journal-backed task. Use when implementation appears done and the task must check Done When, run configured verification, review the git diff, review stable project-context impact, record evidence, archive the Journal, and report residual risks.
---

# Finish a Journal-Backed Task

Resolve `<plugin-root>` as the parent of this Skill's `skills/` directory, identified by its `.claude-plugin/` manifest.

1. Resolve the intended Journal explicitly when active tasks are ambiguous.
2. Check every Done When item against evidence.
3. Run `context-impact.py`, review the full git diff, and record Diff Review plus Project Context Review in `progress.md`.
4. Use `no-impact`, `updated`, or a concrete `follow-up` for Project Context Review.
5. Run `python3 <plugin-root>/lib/verify-task.py --project-root <repository> --plan-id <task-id> --mode full --record`.
6. Keep the Journal active if verification or any completion prerequisite fails.
7. Mark evidenced Done When boxes, then run `python3 <plugin-root>/lib/archive-plan.py --project-root <repository> --plan-id <task-id>`.
8. Report exact verification, context review, archive path, and residual risks.
