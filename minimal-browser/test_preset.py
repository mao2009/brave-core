#!/usr/bin/env python3
"""Sanity tests for the experimental minimal GN configuration."""
from pathlib import Path
import re
import unittest

PRESET = Path(__file__).with_name("args.gn")
REQUIRED = {
    "is_brave_origin_branded": "true",
    "enable_brave_rewards": "false",
    "enable_brave_wallet": "false",
    "enable_ai_chat": "false",
    "enable_brave_vpn_v1": "false",
    "enable_brave_vpn_v2": "false",
}

def parse_gn_args(source: str) -> dict[str, str]:
    result = {}
    for raw in source.splitlines():
        line = raw.split("#", 1)[0].strip()
        if not line:
            continue
        match = re.fullmatch(r"([A-Za-z_][A-Za-z_0-9]*)\s*=\s*(true|false|\d+|\"[^\"]*\")", line)
        if match is None:
            raise ValueError(f"Unexpected GN argument syntax: {raw!r}")
        key, value = match.groups()
        if key in result:
            raise ValueError(f"Duplicate GN argument: {key}")
        result[key] = value
    return result

class MinimalPresetTests(unittest.TestCase):
    def test_feature_flags(self):
        actual = parse_gn_args(PRESET.read_text(encoding="utf-8"))
        for key, expected in REQUIRED.items():
            with self.subTest(key=key):
                self.assertEqual(actual.get(key), expected)

    def test_fail_closed_on_duplicates(self):
        with self.assertRaises(ValueError):
            parse_gn_args("enable_ai_chat = false\nenable_ai_chat = true")

    def test_fail_closed_on_unknown_syntax(self):
        with self.assertRaises(ValueError):
            parse_gn_args("enable_ai_chat = true || false")

if __name__ == "__main__":
    unittest.main()
