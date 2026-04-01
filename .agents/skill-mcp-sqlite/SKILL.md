---
name: mcp-sqlite
description: Use the SQLite MCP server to inspect schemas, run SQL queries, and explore local SQLite databases. Use when the task involves a local `.db` file, lightweight analytics, or validating application state stored in SQLite.
---

# SQLite MCP

Use the SQLite MCP server for local database inspection and queries.

## Workflow

1. Identify the database file being targeted.
2. Inspect available tables and schemas before writing complex SQL.
3. Prefer focused queries with limits.
4. Translate query results into the answer the user actually needs.

## Good Fits

- Explore local app databases.
- Inspect table structures.
- Run analytical or debugging queries.
- Validate rows that explain a bug or test failure.

## Guardrails

- Keep queries small and targeted.
- Confirm the database path if the task could point at multiple files.
- Use explicit filters and limits for large tables.
