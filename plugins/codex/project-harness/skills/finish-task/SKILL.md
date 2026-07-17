---
name: finish-task
description: Execute the explicit Project Harness completion transaction for a Journal-backed task. Use when implementation appears done and the task must check Done When, run configured verification, review the git diff, review stable project-context impact, record evidence, archive the Journal, and report residual risks.
---

# Finish a Journal-Backed Task

Resolve `<plugin-root>` as the parent of this Skill's `skills/` directory, identified by its `.codex-plugin/` manifest.

1. Resolve the intended Journal explicitly when more than one active task exists:

   ```bash
   python3 <plugin-root>/lib/resolve-plan.py --project-root <repository> --plan-id <task-id>
   ```

2. Read `task_plan.md` and check every Done When criterion against current evidence. Do not mark an unchecked criterion merely because implementation stopped.
3. Run the context-impact checker and inspect its suggestions:

   ```bash
   python3 <plugin-root>/lib/context-impact.py --project-root <repository>
   ```

4. Review the complete git diff. Record `Diff Review` as `passed` only after checking scope, correctness, accidental changes, and secrets.
5. Complete `Project Context Review` in `progress.md`:
   - `no-impact` when stable project knowledge did not change;
   - `updated` after updating the relevant existing `docs/agent/` module;
   - `follow-up` only with a concrete note explaining the unresolved documentation work.
6. Run and record fresh project verification:

   ```bash
   python3 <plugin-root>/lib/verify-task.py \
     --project-root <repository> \
     --plan-id <task-id> \
     --mode full \
     --record
   ```

7. If verification fails, keep the Journal active, record the failure at the next semantic checkpoint, and fix or report the blocker.
8. Mark Done When checkboxes only after their evidence exists. Then archive:

   ```bash
   python3 <plugin-root>/lib/archive-plan.py \
     --project-root <repository> \
     --plan-id <task-id>
   ```

9. Report the outcome, exact verification run, context-review result, archive path, and residual risks. Never claim completion if archival prerequisites failed.
