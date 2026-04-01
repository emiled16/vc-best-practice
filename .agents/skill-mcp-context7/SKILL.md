---
name: mcp-context7
description: Use Context7 MCP for up-to-date framework and library documentation, API references, migration guidance, and code examples. Use when a task depends on current docs instead of model memory, especially for package usage, version-specific behavior, or recent API changes.
---

# Context7 MCP

Use the Context7 MCP server when the task depends on current library documentation.

## Workflow

1. Identify the library, framework, or package name.
2. Resolve the correct documentation target if the client exposes multiple options.
3. Query for the narrow question instead of asking for broad dumps.
4. Base the answer on the returned docs and examples, not memory.

## Good Fits

- Verify current API signatures.
- Check version-specific behavior or migrations.
- Pull minimal examples for implementation.
- Confirm configuration flags or defaults.

## Guardrails

- Prefer official documentation over secondary summaries.
- Ask focused questions so the tool returns high-signal excerpts.
- Mention the package and version when the user provides one.
