---
name: mcp-postgres
description: Use the Postgres MCP server for schema inspection and read-only SQL queries against PostgreSQL databases. Use when the task requires understanding tables, relationships, or querying live Postgres data safely from MCP.
---

# Postgres MCP

Use the Postgres MCP server for database inspection and read-only querying.

## Workflow

1. Identify the target database and the tables relevant to the request.
2. Inspect schema information before writing non-trivial SQL.
3. Prefer small, explicit `SELECT` queries.
4. Summarize results in business or engineering terms after querying.

## Good Fits

- Discover tables and columns.
- Validate assumptions against live data.
- Check counts, joins, or filtered slices.
- Investigate data quality problems without changing data.

## Guardrails

- Assume the server is read-only and design queries accordingly.
- Avoid `SELECT *` on large tables unless the result is explicitly limited.
- Use bounded queries with `LIMIT` where practical.
