from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path


DEFAULT_MANAGED_TREES = ("skills", "agents", "rules", "plugins")
LEGACY_SKILL_FILE = "SKILL.md"
EXCLUDED_NAMES = {".DS_Store"}


@dataclass(frozen=True)
class SyncPlan:
    source_root: Path
    target_root: Path
    config_target_root: Path
    dry_run: bool
    backup_config: bool
    managed_trees: tuple[str, ...]
