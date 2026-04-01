from __future__ import annotations

import shutil
import tempfile
from datetime import datetime
from pathlib import Path

from agent_home_sync.models import EXCLUDED_NAMES, LEGACY_SKILL_FILE, SyncPlan
from agent_home_sync.toml_merge import deep_merge, dump_toml, load_toml


def log(message: str) -> None:
    print(message)


def ensure_directory(path: Path, dry_run: bool) -> None:
    if dry_run:
        log(f"Would ensure target root exists: {path}")
        return
    path.mkdir(parents=True, exist_ok=True)


def backup_file(path: Path) -> Path:
    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
    backup_path = path.with_name(f"{path.name}.bak.{timestamp}")
    shutil.copy2(path, backup_path)
    return backup_path


def merge_config(plan: SyncPlan) -> None:
    source_config = plan.source_root / "config.toml"
    target_config = plan.config_target_root / "config.toml"

    if not source_config.is_file():
        return

    merged = deep_merge(load_toml(target_config), load_toml(source_config))
    merged_text = dump_toml(merged)
    current_text = target_config.read_text() if target_config.exists() else None

    if current_text == merged_text:
        log(f"Config already up to date: {target_config}")
        return

    if plan.dry_run:
        log(f"Would merge {source_config} into {target_config}")
        return

    plan.config_target_root.mkdir(parents=True, exist_ok=True)
    if target_config.exists() and plan.backup_config:
        backup_path = backup_file(target_config)
        log(f"Backed up existing config to {backup_path}")

    with tempfile.NamedTemporaryFile(
        mode="w",
        encoding="utf-8",
        dir=plan.config_target_root,
        delete=False,
    ) as handle:
        handle.write(merged_text)
        temp_path = Path(handle.name)

    temp_path.replace(target_config)
    log(f"Merged config into {target_config}")


def copy_file(source: Path, target: Path, dry_run: bool) -> None:
    if dry_run:
        log(f"Would copy {source} -> {target}")
        return

    target.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(source, target)


def sync_directory(source_dir: Path, target_dir: Path, dry_run: bool) -> None:
    if not source_dir.is_dir():
        return

    if dry_run:
        log(f"Would sync {source_dir} -> {target_dir}")
    else:
        log(f"Syncing {source_dir} -> {target_dir}")

    for source_path in sorted(source_dir.rglob("*")):
        relative_path = source_path.relative_to(source_dir)
        if any(part in EXCLUDED_NAMES for part in relative_path.parts):
            continue

        target_path = target_dir / relative_path
        if source_path.is_dir():
            if dry_run and not target_path.exists():
                log(f"Would create {target_path}")
            elif not dry_run:
                target_path.mkdir(parents=True, exist_ok=True)
            continue

        copy_file(source_path, target_path, dry_run=dry_run)


def sync_legacy_skill_dirs(plan: SyncPlan) -> None:
    for child in sorted(plan.source_root.iterdir()):
        if not child.is_dir():
            continue
        if not (child / LEGACY_SKILL_FILE).is_file():
            continue
        sync_directory(child, plan.target_root / "skills" / child.name, plan.dry_run)


def sync_managed_trees(plan: SyncPlan) -> None:
    for tree_name in plan.managed_trees:
        sync_directory(plan.source_root / tree_name, plan.target_root / tree_name, plan.dry_run)
