"""Read-only structural check of a pinned upstream ECC checkout.

This script does not execute or import code from ECC and requires no API key.
"""

import json
from pathlib import Path
import re
import subprocess
import sys

UPSTREAM_REPOSITORY = "https://github.com/affaan-m/ECC"
UPSTREAM_SHA = "90606c8315ee09cafc303515c5f33024db6b9882"


def verify(root: Path) -> dict[str, str]:
    root = root.resolve(strict=True)
    actual_sha = subprocess.check_output(
        ["git", "-C", str(root), "rev-parse", "HEAD"],
        text=True,
        stderr=subprocess.DEVNULL,
        timeout=15,
    ).strip()
    if actual_sha != UPSTREAM_SHA:
        raise ValueError(f"ECC source SHA mismatch: {actual_sha}")

    manifest_path = root / ".codex-plugin" / "plugin.json"
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    if manifest.get("name") != "ecc":
        raise ValueError("Unexpected Codex plugin name")
    if manifest.get("repository", "").rstrip("/").lower() != UPSTREAM_REPOSITORY.lower():
        raise ValueError("Unexpected upstream repository identity")
    if manifest.get("license") != "MIT":
        raise ValueError("Unexpected plugin license")
    version = manifest.get("version")
    if not isinstance(version, str) or not re.fullmatch(r"\d+\.\d+\.\d+", version):
        raise ValueError("Missing or invalid ECC version")

    for key, directory in (("skills", True), ("mcpServers", False), ("hooks", False)):
        relative = manifest.get(key)
        if not isinstance(relative, str) or not relative.startswith("./"):
            raise ValueError(f"Unsafe or missing {key} path")
        target = (root / relative).resolve()
        if not target.is_relative_to(root):
            raise ValueError(f"Path escapes checkout: {key}")
        if directory and not target.is_dir():
            raise ValueError(f"Missing skill directory: {key}")
        if not directory and not target.is_file():
            raise ValueError(f"Missing manifest asset: {key}")

    license_path = root / "LICENSE"
    license_text = license_path.read_text(encoding="utf-8")
    if not license_text.startswith("MIT License") or "Copyright" not in license_text:
        raise ValueError("Missing MIT license and copyright notice")

    skill_count = sum(1 for item in (root / "skills").iterdir() if item.is_dir())
    if skill_count < 1:
        raise ValueError("No skill directories found")
    return {"sha": actual_sha, "version": version, "skills_directories": str(skill_count)}


if __name__ == "__main__":
    if len(sys.argv) != 2:
        raise SystemExit("Usage: python scripts/check_upstream_ecc.py <path-to-upstream-checkout>")
    try:
        result = verify(Path(sys.argv[1]))
    except (OSError, ValueError, KeyError, json.JSONDecodeError, subprocess.SubprocessError) as exc:
        print(f"ECC source structural check FAILED: {exc}", file=sys.stderr)
        raise SystemExit(1) from exc
    print("ECC source structural check PASSED: " + json.dumps(result, sort_keys=True))
    print("Note: This does NOT install/run ECC, Codex, hooks, or AI agents.")
