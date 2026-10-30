#!/usr/bin/env python3
"""PostToolUse hook: append one line to docs/usage-log.md when a my-skill skill fires.

Reads the hook JSON on stdin. Never fails the session: any error exits 0 silently.
Line format: `<date> — <skill> — <active context>`. continuous-improvement reads this file.
"""
import json
import re
import sys
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

try:
    data = json.load(sys.stdin)
    skill = (data.get("tool_input") or {}).get("skill", "")
    if skill.startswith("my-skill:"):
        ctx = re.search(r"^Current:\s*(\S+)", (ROOT / "docs/active-context.md").read_text(encoding="utf-8"), re.M)
        with open(ROOT / "docs/usage-log.md", "a", encoding="utf-8") as f:
            f.write(f"{date.today()} — {skill.split(':', 1)[1]} — {ctx.group(1) if ctx else 'unset'}\n")
except Exception:
    pass
