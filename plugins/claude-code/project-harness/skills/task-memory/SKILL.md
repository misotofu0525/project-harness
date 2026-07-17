---
name: task-memory
description: Create, resolve, checkpoint, or restore an isolated three-file Project Harness Journal. Use for long, research-heavy, cross-session, or compaction-prone tasks, or when a user explicitly requests durable planning files or recovery after clear, resume, or compaction.
---

# Use Durable Task Memory

Resolve `<plugin-root>` as the parent of this Skill's `skills/` directory, identified by its `.claude-plugin/` manifest.

- Create a Journal with `python3 <plugin-root>/lib/create-plan.py <task-id> --project-root <repository> --title "<title>" --goal "<goal>"`.
- Skip the Journal for simple tasks.
- Resolve explicit `PLAN_ID` first, then a unique active Journal. Fail clearly on ambiguity and never choose by modification time.
- Restore with `python3 <plugin-root>/lib/restore-plan.py --project-root <repository> --plan-id <task-id>`.
- Keep the three Journal files together and update Latest Checkpoint only at semantic boundaries.
- Do not log every tool call or maintain a live task-status field.
- Use `finish-task` for final verification and archival.
