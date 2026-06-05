#!/usr/bin/env python3
"""Minify JSON and pack.mcmeta files under a directory tree (in place)."""

import json
import sys
from pathlib import Path


def is_json_pack_file(path: Path) -> bool:
    return path.suffix == ".json" or path.name.endswith(".mcmeta")


def minify_file(path: Path) -> None:
    data = json.loads(path.read_text(encoding="utf-8"))
    path.write_text(
        json.dumps(data, separators=(",", ":"), ensure_ascii=False) + "\n",
        encoding="utf-8",
    )


def main() -> None:
    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} <directory>", file=sys.stderr)
        sys.exit(1)

    root = Path(sys.argv[1])
    if not root.is_dir():
        print(f"Not a directory: {root}", file=sys.stderr)
        sys.exit(1)

    paths = sorted(
        path
        for path in root.rglob("*")
        if path.is_file() and is_json_pack_file(path)
    )
    for path in paths:
        minify_file(path)

    print(f"Minified {len(paths)} file(s) under {root}")


if __name__ == "__main__":
    main()
