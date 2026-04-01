# Agent Home Sync

This repository manages a subset of an agent home directory such as `~/.codex`
or `~/.claude` and provides a Python CLI to sync managed content into a target
home without deleting unrelated local state.

## Layout

- `agent_home_sync/`: Runtime package.
- `tests/`: Unit, integration, and smoke test layout.
- `.codex/`: Source-managed agent configuration content.

## Usage

```bash
python3 -m agent_home_sync --dry-run
python3 -m agent_home_sync --tool claude --dry-run
```
