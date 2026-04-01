# MCP Setup Notes

This repository's MCP server configuration lives in `.agents/config.toml`.

## Required Environment Variables

These variables are required by the current config in this repo.

| MCP server | Required env vars | Optional env vars | Notes |
| --- | --- | --- | --- |
| `context7` | `CONTEXT7_API_KEY` | None | Used by `@upstash/context7-mcp` for current library and framework docs. |
| `github` | `GITHUB_PERSONAL_ACCESS_TOKEN` | `GITHUB_TOOLSETS` | `GITHUB_TOOLSETS` lets you restrict or expand enabled GitHub toolsets. |
| `postgres` | `POSTGRES_MCP_URL` | None | Should be a PostgreSQL connection URL, for example `postgresql://user:pass@host:5432/dbname`. |
| `kubernetes` | None | `KUBECONFIG` | No env var is required by the current config. If you do not want to use the default kube context resolution, set `KUBECONFIG` to a kubeconfig file. |
| `docker` | None | `DOCKER_CONFIG` | Uses Docker's MCP gateway via `docker mcp gateway run`. Docker Desktop or the Docker MCP Toolkit must be installed and running, and any desired upstream MCP servers should be enabled in Docker first. |
| `notion` | `NOTION_TOKEN` | `OPENAPI_MCP_HEADERS`, `AUTH_TOKEN` | `NOTION_TOKEN` is the recommended auth method for the local Notion MCP server. `OPENAPI_MCP_HEADERS` is the advanced alternative. `AUTH_TOKEN` only matters if you run Notion MCP in HTTP transport mode. |
| `sqlite` | `SQLITE_MCP_PATH` | None | Should be an absolute path to the SQLite database file you want the server to open. |

## Example Shell Setup

```bash
export CONTEXT7_API_KEY="..."
export GITHUB_PERSONAL_ACCESS_TOKEN="..."
export GITHUB_TOOLSETS="default,actions"
export POSTGRES_MCP_URL="postgresql://user:pass@localhost:5432/app"
export KUBECONFIG="$HOME/.kube/config"
export DOCKER_CONFIG="$HOME/.docker"
export NOTION_TOKEN="ntn_..."
export SQLITE_MCP_PATH="/absolute/path/to/app.db"
```

## Notes

- `github`, `docker`, `notion`, and `kubernetes` can expose powerful write operations depending on how you configure credentials and toolsets.
- `docker` in this repo is a gateway entrypoint, not a single Docker-specific tool binary. The tools available through it depend on what you have enabled in Docker MCP Toolkit.
- `postgres` and `sqlite` are database-specific. Point them at a dedicated development or read-only data source unless you explicitly want broader access.
- If an MCP server fails to start, check that the env var is set in the shell before launching Codex.
