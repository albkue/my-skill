#!/usr/bin/env python3
"""Validate the my-skill plugin. Stdlib only. Exit 1 on any ERROR; WARN never fails.

Usage: python scripts/validate.py
"""
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
errors, warns = [], []
err = lambda m: errors.append(m)
warn = lambda m: warns.append(m)


def frontmatter(path):
    m = re.match(r"---\n(.*?)\n---\n", path.read_text(encoding="utf-8"), re.S)
    if not m:
        return None
    fm = {}
    for line in m.group(1).splitlines():
        k, _, v = line.partition(":")
        fm[k.strip()] = v.strip()
    return fm


# --- manifest
manifest = json.loads((ROOT / ".claude-plugin/plugin.json").read_text(encoding="utf-8"))
version = manifest.get("version", "")
if not re.fullmatch(r"\d+\.\d+\.\d+", version):
    err(f"plugin.json: bad version {version!r}")

# --- skills
skills = {}
for d in sorted((ROOT / "skills").iterdir()):
    f = d / "SKILL.md"
    if not f.exists():
        err(f"{d.name}: missing SKILL.md")
        continue
    fm = frontmatter(f)
    if fm is None:
        err(f"{d.name}: no frontmatter")
        continue
    skills[d.name] = fm
    for key in ("name", "description", "version", "author"):
        if not fm.get(key):
            err(f"{d.name}: frontmatter missing {key}")
    if fm.get("name") != d.name:
        err(f"{d.name}: name {fm.get('name')!r} != folder")
    desc = fm.get("description", "")
    if len(desc) > 1024:
        err(f"{d.name}: description {len(desc)} chars > 1024 limit")
    if "Do NOT use" not in desc:
        err(f"{d.name}: description lacks a 'Do NOT use' boundary")
    for ref in re.findall(r"\(([a-z][a-z0-9-]+(?: / [a-z][a-z0-9-]+)*)\)", desc):
        for name in ref.split(" / "):
            if not (ROOT / "skills" / name).exists():
                warn(f"{d.name}: description routes to unknown skill {name!r}")
    body = f.read_text(encoding="utf-8")
    if "workflow-profile" not in body:
        err(f"{d.name}: never reads docs/workflow-profile.md")
    for section in ("## Workflow",):
        if section not in body:
            err(f"{d.name}: missing section {section!r}")

# --- unique descriptions
seen = {}
for n, fm in skills.items():
    first = fm.get("description", "").split(".")[0].lower()
    if first in seen:
        err(f"{n}: description opener duplicates {seen[first]}")
    seen[first] = n

# --- commands
cmd_targets = set()
for f in sorted((ROOT / "commands").glob("*.md")):
    fm = frontmatter(f)
    if not fm or not fm.get("description"):
        err(f"commands/{f.name}: missing description")
    for target in re.findall(r"skills/([a-z0-9-]+)/SKILL\.md", f.read_text(encoding="utf-8")):
        cmd_targets.add(target)
        if target not in skills:
            err(f"commands/{f.name}: routes to missing skill {target}")
# skills are directly invocable as /my-skill:<name>; commands are optional wrappers

# --- active context + hook
for p in ("docs/active-context.md", "hooks/hooks.json", "scripts/log_skill.py", "commands/today.md", "commands/setup.md"):
    if not (ROOT / p).exists():
        err(f"missing {p}")
ctx = re.search(r"^Current:\s*(\S+)", (ROOT / "docs/active-context.md").read_text(encoding="utf-8"), re.M)
profile = (ROOT / "docs/workflow-profile.md").read_text(encoding="utf-8")
block = re.search(r"^## Contexts\n(.*?)(?=^## )", profile, re.M | re.S)
ids = set(re.findall(r"^### (\S+)", block.group(1), re.M)) if block else set()
if not ids:
    err("workflow-profile.md: no '## Contexts' section with '### <id>' entries")
if not ctx or ctx.group(1) not in ids | {"unset"}:
    err(f"active-context.md: Current {ctx and ctx.group(1)!r} is not unset or a defined context {sorted(ids)}")
if not (ROOT / "docs/workflow-profile.example.md").exists():
    err("missing docs/workflow-profile.example.md")
hooks = json.loads((ROOT / "hooks/hooks.json").read_text(encoding="utf-8"))
if "PostToolUse" not in hooks.get("hooks", {}):
    err("hooks.json: PostToolUse hook missing")
for n in ("backend-job", "software-internship"):
    if "active-context" not in (ROOT / "skills" / n / "SKILL.md").read_text(encoding="utf-8"):
        err(f"{n}: does not consult docs/active-context.md")

# --- transition scenarios
if "Transition playbook" not in (ROOT / "skills/workflow-adapter/SKILL.md").read_text(encoding="utf-8"):
    err("workflow-adapter: Transition playbook section missing")
tpath = ROOT / "evals/transitions.json"
if not tpath.exists():
    err("evals/transitions.json missing")
else:
    scenarios = json.loads(tpath.read_text(encoding="utf-8"))
    if len(scenarios) < 4:
        err("evals/transitions.json: need >=4 scenarios")
    for sc in scenarios:
        for key in ("say", "profile", "reuse_my_skill", "reuse_installed", "new_skills", "retire_candidates"):
            if key not in sc:
                err(f"transitions: {sc.get('say', '?')!r} missing {key}")
        for name in sc.get("reuse_my_skill", []) + sc.get("retire_candidates", []):
            if name not in skills:
                err(f"transitions: unknown my-skill skill {name!r}")

# --- AGENTS.md routing + version
agents = (ROOT / "AGENTS.md").read_text(encoding="utf-8")
for n in skills:
    if f"`{n}`" not in agents:
        err(f"AGENTS.md: skill {n} missing from routing index")
m = re.search(r"Version:\s*([\d.]+)", agents)
if not m or m.group(1) != version:
    err(f"AGENTS.md version {m and m.group(1)} != plugin.json {version}")
count = re.search(r"all (\d+) skills", agents)
if count and int(count.group(1)) != len(skills):
    err(f"AGENTS.md says {count.group(1)} skills, found {len(skills)}")

# --- changelog
top = re.search(r"^## (\d+\.\d+\.\d+)", (ROOT / "docs/CHANGELOG.md").read_text(encoding="utf-8"), re.M)
if not top or top.group(1) != version:
    err(f"CHANGELOG top entry {top and top.group(1)} != plugin.json {version}")

# --- relative links
for f in [ROOT / "README.md", ROOT / "AGENTS.md", ROOT / "CONTRIBUTING.md", *(ROOT / "docs").glob("*.md")]:
    for target in re.findall(r"\]\(([^)#\s]+)(?:#[^)]*)?\)", f.read_text(encoding="utf-8")):
        if re.match(r"[a-z]+:", target):
            continue
        if not (f.parent / target).resolve().exists():
            err(f"{f.relative_to(ROOT)}: broken link {target}")

# --- trigger evals
evals_path = ROOT / "evals/triggers.json"
if not evals_path.exists():
    err("evals/triggers.json missing")
else:
    evals = json.loads(evals_path.read_text(encoding="utf-8"))
    for n in skills:
        e = evals.get(n, {})
        if len(e.get("should", [])) < 3:
            err(f"evals: {n} needs >=3 'should' prompts")
        if len(e.get("should_not", [])) < 2:
            err(f"evals: {n} needs >=2 'should_not' prompts")
        for item in e.get("should_not", []):
            if item.get("route") not in skills:
                err(f"evals: {n} should_not routes to unknown skill {item.get('route')!r}")
    for n in evals:
        if n not in skills:
            err(f"evals: unknown skill {n}")

for w in warns:
    print("WARN ", w)
for e in errors:
    print("ERROR", e)
print(f"\n{len(skills)} skills, {len(errors)} errors, {len(warns)} warnings")
sys.exit(1 if errors else 0)
