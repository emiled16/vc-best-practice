from __future__ import annotations

import json
import re
import tomllib
from pathlib import Path
from typing import Any


def load_toml(path: Path) -> dict[str, Any]:
    if not path.exists():
        return {}
    return tomllib.loads(path.read_text())


def deep_merge(base: dict[str, Any], incoming: dict[str, Any]) -> dict[str, Any]:
    merged = dict(base)
    for key, value in incoming.items():
        current = merged.get(key)
        if isinstance(current, dict) and isinstance(value, dict):
            merged[key] = deep_merge(current, value)
        else:
            merged[key] = value
    return merged


def format_toml_key(key: str) -> str:
    if re.fullmatch(r"[A-Za-z0-9_-]+", key):
        return key
    return json.dumps(key)


def format_toml_value(value: Any) -> str:
    if isinstance(value, bool):
        return "true" if value else "false"
    if isinstance(value, int):
        return str(value)
    if isinstance(value, float):
        return repr(value)
    if isinstance(value, str):
        return json.dumps(value)
    if isinstance(value, list):
        return "[" + ", ".join(format_toml_value(item) for item in value) + "]"
    raise TypeError(f"unsupported TOML value: {value!r}")


def emit_toml_table(lines: list[str], prefix: list[str], mapping: dict[str, Any]) -> None:
    scalar_items = [(key, value) for key, value in mapping.items() if not isinstance(value, dict)]
    nested_items = [(key, value) for key, value in mapping.items() if isinstance(value, dict)]

    if prefix and scalar_items:
        lines.append("[" + ".".join(format_toml_key(part) for part in prefix) + "]")
        for key, value in scalar_items:
            lines.append(f"{format_toml_key(key)} = {format_toml_value(value)}")

    for index, (key, value) in enumerate(nested_items):
        if lines and lines[-1] != "":
            lines.append("")
        emit_toml_table(lines, [*prefix, key], value)
        if index != len(nested_items) - 1 and lines and lines[-1] != "":
            lines.append("")


def dump_toml(data: dict[str, Any]) -> str:
    lines: list[str] = []
    scalar_items = [(key, value) for key, value in data.items() if not isinstance(value, dict)]
    table_items = [(key, value) for key, value in data.items() if isinstance(value, dict)]

    for key, value in scalar_items:
        lines.append(f"{format_toml_key(key)} = {format_toml_value(value)}")

    if scalar_items and table_items:
        lines.append("")

    for index, (key, value) in enumerate(table_items):
        emit_toml_table(lines, [key], value)
        if index != len(table_items) - 1 and lines and lines[-1] != "":
            lines.append("")

    return "\n".join(lines).rstrip() + "\n"
