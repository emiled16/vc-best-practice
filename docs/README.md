# Agent Home Sync

This repository manages a subset of an agent home directory such as `~/.agents`
or `~/.claude` and provides a Python CLI to sync managed content into a target
home without deleting unrelated local state. The managed trees sync into the
agent home, while `config.toml` is merged into `~/.codex` by default.

## Layout

- `agent_home_sync/`: Runtime package.
- `tests/`: Unit, integration, and smoke test layout.
- `.agents/`: Source-managed agent configuration content.

## Usage

```bash
python3 -m agent_home_sync.cli --dry-run
python3 -m agent_home_sync.cli --tool claude --dry-run
python3 -m agent_home_sync.cli --config-target ~/.codex --dry-run
```
