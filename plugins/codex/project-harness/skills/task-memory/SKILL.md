---
name: task-memory
description: Create, resolve, checkpoint, or restore an isolated three-file Project Harness Journal. Use for long, research-heavy, cross-session, or compaction-prone tasks, or when a user explicitly requests durable planning files or recovery after clear, resume, or compaction.
---

# Use Durable Task Memory

Resolve `<plugin-root>` as the parent of this Skill's `skills/` directory, identified by its `.codex-plugin/` manifest.

## Start a Journal

Use a stable task id and create one isolated bundle:

```bash
python3 <plugin-root>/lib/create-plan.py <task-id> \
  --project-root <repository> \
  --title "<task title>" \
  --goal "<observable end state>"
```

Do not create a Journal for quick lookups, single-file edits, or other short tasks that do not need durable recovery.

## Resolve and Restore

Resolution order is fixed:

1. explicit `--plan-id` or `PLAN_ID`
2. the only active Journal
3. explicit ambiguity failure when several active Journals exist
4. no Journal when none exists

Never choose by modification time. Inspect or restore with:

```bash
python3 <plugin-root>/lib/restore-plan.py --project-root <repository> --plan-id <task-id>
```

## Checkpoint

Keep `task_plan.md`, `findings.md`, and `progress.md` together. Update `Latest Checkpoint` only after a phase, important decision or discovery, meaningful failure, pause, pre-compaction boundary, or finish preparation. Do not log every tool call and do not add a live task-status field.

Before final delivery, use `finish-task` rather than marking a live status as complete.
