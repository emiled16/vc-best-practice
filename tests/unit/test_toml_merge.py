from __future__ import annotations

from agent_home_sync.toml_merge import deep_merge


def test_deep_merge_overrides_managed_keys_but_keeps_unrelated_keys() -> None:
    target = {
        "model": "gpt-5.4",
        "plugins": {"github@openai-curated": {"enabled": True}},
        "projects": {"/tmp/project": {"trust_level": "trusted"}},
    }
    source = {
        "mcp_servers": {
            "context7": {
                "command": "npx",
                "args": ["-y", "@upstash/context7-mcp"],
            }
        },
        "plugins": {"github@openai-curated": {"enabled": False}},
    }

    merged = deep_merge(target, source)

    assert merged["projects"] == {"/tmp/project": {"trust_level": "trusted"}}
    assert merged["plugins"] == {"github@openai-curated": {"enabled": False}}
    assert merged["mcp_servers"]["context7"]["command"] == "npx"
