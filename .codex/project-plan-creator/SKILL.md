---
name: project-plan-creator
description: Create and update versioned software project plans in Markdown. Use when a user asks to create a new implementation plan, revise an existing plan, or structure work into milestones, tasks, dependencies, and execution checklists.
---

# Project Plan Creator

Create clear, versioned implementation plans for software projects.
Treat plans as immutable snapshots: when scope changes, create a new version instead of editing history.

## Output Files

Create both files at the project root:

1. `plans/plan_vX.Y.md`
2. `checklists/plan_vX.Y_checklist.md`

Use the same version in both filenames.

## Rules

- Break work into milestones (or epics) and concrete tasks.
- Give each task a stable ID (for example `T1`, `T2`).
- Include dependencies between tasks using those IDs.
- Do not include time or effort estimates.
- Keep revision history in the plan file so each version explains what changed and why.

## Workflow

1. Capture context and goals.
2. Define milestones and task breakdown.
3. Add dependencies for every task.
4. Create or update the `Revisions` section:
   - For `v1.0`, state `Initial version`.
   - For later versions, list changes compared to the previous version and the rationale.
5. Generate the matching checklist file with one checkbox per task.

## Plan Template

```markdown
# Plan vX.Y

## Context
Briefly describe the problem, goals, and constraints.

## Milestones

### M1: Milestone Name

#### Task T1: Task Title
- Description: What must be done and the expected outcome.
- Files involved: Relevant files, modules, or systems.
- Dependencies: None | T2, T3

#### Task T2: Task Title
- Description: ...
- Files involved: ...
- Dependencies: T1

## Revisions
- vX.Y: Initial version.
```

## Checklist Template

```markdown
# Checklist for Plan vX.Y

## Milestone M1: Milestone Name
- [ ] T1: Task Title
- [ ] T2: Task Title
```

## Quality Bar

Before finalizing, verify:

- Filenames and versions match.
- Every task appears in the checklist.
- Dependencies reference valid task IDs.
- No task includes time estimates.
- The plan is specific enough for another engineer to execute without guessing.
