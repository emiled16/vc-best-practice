from __future__ import annotations

import argparse
import sys
from pathlib import Path

from agent_home_sync.fs_sync import ensure_directory, log, merge_config, sync_legacy_skill_dirs, sync_managed_trees
from agent_home_sync.models import DEFAULT_MANAGED_TREES, SyncPlan


def build_parser() -> argparse.ArgumentParser:
    repo_root = Path(__file__).resolve().parent.parent

    parser = argparse.ArgumentParser(
        description=(
            "Sync a managed agent home from this repository into a target home "
            "directory without deleting unrelated target content."
        )
    )
    parser.add_argument(
        "--source",
        type=Path,
        default=repo_root / ".agents",
        help="Source managed home directory. Default: %(default)s",
    )
    parser.add_argument(
        "--target",
        type=Path,
        default=Path.home() / ".agents",
        help="Target home directory for managed trees. Default: %(default)s",
    )
    parser.add_argument(
        "--config-target",
        type=Path,
        default=Path.home() / ".codex",
        help="Target directory for config.toml. Default: %(default)s",
    )
    parser.add_argument(
        "--tool",
        choices=("agents", "claude", "custom"),
        default="agents",
        help=(
            "Convenience target preset. 'agents' uses ~/.agents, 'claude' uses "
            "~/.claude, and 'custom' leaves --target unchanged."
        ),
    )
    parser.add_argument(
        "--managed-tree",
        action="append",
        dest="managed_trees",
        help=(
            "Managed directory relative to the source root. Repeat to add more "
            "trees. Defaults to skills, agents, rules, plugins."
        ),
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Show planned changes without writing.",
    )
    parser.add_argument(
        "--no-config-backup",
        action="store_true",
        help="Do not create a timestamped backup before updating config.toml.",
    )
    return parser


def determine_target_root(tool: str, explicit_target: Path) -> Path:
    default_agents_target = Path.home() / ".agents"
    if tool == "agents":
        return default_agents_target if explicit_target == default_agents_target else explicit_target
    if tool == "claude":
        return Path.home() / ".claude" if explicit_target == default_agents_target else explicit_target
    return explicit_target


def determine_config_target_root(tool: str, explicit_target: Path) -> Path:
    default_codex_target = Path.home() / ".codex"
    if tool == "agents":
        return default_codex_target if explicit_target == default_codex_target else explicit_target
    if tool == "claude":
        return Path.home() / ".claude" if explicit_target == default_codex_target else explicit_target
    return explicit_target


def parse_args(argv: list[str]) -> SyncPlan:
    parser = build_parser()
    args = parser.parse_args(argv)

    source_root = args.source.expanduser().resolve()
    target_root = determine_target_root(args.tool, args.target.expanduser())
    config_target_root = determine_config_target_root(args.tool, args.config_target.expanduser())
    managed_trees = tuple(args.managed_trees or DEFAULT_MANAGED_TREES)

    if not source_root.is_dir():
        parser.error(f"source directory not found: {source_root}")

    return SyncPlan(
        source_root=source_root,
        target_root=target_root,
        config_target_root=config_target_root,
        dry_run=args.dry_run,
        backup_config=not args.no_config_backup,
        managed_trees=managed_trees,
    )


def main(argv: list[str] | None = None) -> int:
    plan = parse_args(argv or sys.argv[1:])
    ensure_directory(plan.target_root, dry_run=plan.dry_run)
    ensure_directory(plan.config_target_root, dry_run=plan.dry_run)
    merge_config(plan)
    sync_legacy_skill_dirs(plan)
    sync_managed_trees(plan)
    log("Sync complete.")
    return 0
