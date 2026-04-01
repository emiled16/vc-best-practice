---
name: project-progress-tracker
description: Track execution progress for a planned software project using append-only logs, decision records, bug records, and checklist updates. Use when implementing work from an existing project plan.
---

# Project Progress Tracker

Track progress in a way that is auditable, easy to resume, and aligned with the active plan version.

## Output Files

Maintain these files in the project root:

1. `memory/progress.md`
2. `memory/key-decisions.md`
3. `memory/bugs.md`
4. `checklists/plan_vX.Y_checklist.md` (for the active plan version)

## Rules

- Treat all `memory/*.md` files as append-only logs.
- Never rewrite history; add correction entries instead.
- Always include the active plan version (`vX.Y`) in progress entries.
- Keep checklist status synchronized with completed work.
- Use task IDs from the plan (for example `T1`, `T2`) whenever available.

## Workflow

1. Identify the active plan version (`plans/plan_vX.Y.md`).
2. Add a `START` entry in `memory/progress.md` before beginning a task.
3. Add a matching `DONE`, `BLOCKED`, or `CANCELLED` entry when task state changes.
4. Update `checklists/plan_vX.Y_checklist.md`:
   - Mark completed tasks as checked.
   - Leave in-progress tasks unchecked.
5. Record notable architecture/product decisions in `memory/key-decisions.md`.
6. Record defects and their current status in `memory/bugs.md`.

## `memory/progress.md` Format

Use this log line format:

`[YYYY-MM-DD HH:MM:SS] [plan vX.Y] [STATUS] <Task ID>: <Short message>`

Allowed statuses: `START`, `DONE`, `BLOCKED`, `UNBLOCKED`, `CANCELLED`, `CORRECTION`.

Example:

```text
# Plan v1.0
[2026-04-01 09:00:00] [plan v1.0] [START] T1: Implement ingestion adapter
[2026-04-01 09:35:00] [plan v1.0] [BLOCKED] T1: Missing API credentials
[2026-04-01 09:50:00] [plan v1.0] [UNBLOCKED] T1: Credentials added to local env
[2026-04-01 10:20:00] [plan v1.0] [DONE] T1: Ingestion adapter merged locally
```

When plan version changes, start a new section:

```text
---
# Plan v1.1
[2026-04-02 11:00:00] [plan v1.1] [START] T1: Replace adapter retry policy
```

## `memory/key-decisions.md` Format

Record one section per decision:

```markdown
## [YYYY-MM-DD] D-001: Decision Title
- Plan: vX.Y
- Context: What problem triggered the decision.
- Options considered:
  - Option A
  - Option B
- Decision: Chosen option.
- Rationale: Why this option was selected.
- Consequences: Tradeoffs, follow-up actions, or risks.
```

## `memory/bugs.md` Format

Record one section per bug:

```markdown
## [YYYY-MM-DD] B-001: Short bug title
- Plan: vX.Y
- Status: Open | In progress | Fixed | Won't fix
- Severity: Low | Medium | High | Critical
- Description: What is failing.
- Reproduction: Minimal steps.
- Root cause: Known cause, or `Unknown`.
- Fix: Implemented fix or next action.
- Verification: How the fix was validated.
```

## Quality Bar

Before finishing a work session, verify:

- Every started task has a later status update.
- Checklist checkboxes reflect actual completion state.
- Each major decision is logged with rationale.
- Each encountered bug is logged with status.
- New entries use the current plan version.
