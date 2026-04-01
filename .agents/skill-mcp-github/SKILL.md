---
name: mcp-github
description: Use the GitHub MCP server for repository inspection, file reads, issue and pull request work, Actions-aware investigation, and other GitHub API tasks. Use when the task should be performed through GitHub capabilities rather than local git alone.
---

# GitHub MCP

Use the GitHub MCP server for GitHub-native operations.

## Workflow

1. Confirm the target owner, repo, and branch or PR when relevant.
2. Prefer read operations first: inspect files, issues, PRs, workflows, and metadata.
3. Use write actions only when the user explicitly wants GitHub state changed.
4. Keep repository scope narrow to avoid unnecessary calls.

## Good Fits

- Read files from a remote repo.
- Inspect issues, PRs, reviews, or workflow state.
- Compare branches or commits.
- Work with GitHub objects that do not exist locally.

## Guardrails

- Treat write operations as higher risk than read operations.
- Use least-privilege PAT scopes.
- If `GITHUB_TOOLSETS` is restricted, stay within the enabled capability set.
