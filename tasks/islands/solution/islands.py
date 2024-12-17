#!/usr/bin/env python3
"""Count connected islands of land in a grid.

Usage:  python3 islands.py <grid.txt> <out.json>

Land cells are '#'; every other character (including spaces) is water. Two land
cells belong to the same island when they are 4-connected (up/down/left/right).
Rows may differ in length; positions past the end of a row are water.

Output:
    {
      "islands": <int>,   # number of connected land components
      "largest": <int>,   # size of the biggest island (0 if there is no land)
      "sizes":   [<int>]  # every island's size, sorted descending
    }
"""
from __future__ import annotations

import json
import sys
from collections import deque


def parse(text: str):
    grid = text.split("\n")
    if grid and grid[-1] == "":
        grid.pop()
    return grid


def is_land(grid, r, c) -> bool:
    if r < 0 or r >= len(grid):
        return False
    row = grid[r]
    if c < 0 or c >= len(row):
        return False
    return row[c] == "#"


def solve(text: str) -> dict:
    grid = parse(text)
    seen = set()
    sizes = []
    for r, row in enumerate(grid):
        for c, ch in enumerate(row):
            if ch != "#" or (r, c) in seen:
                continue
            size = 0
            q = deque([(r, c)])
            seen.add((r, c))
            while q:
                cr, cc = q.popleft()
                size += 1
                for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                    nr, nc = cr + dr, cc + dc
                    if (nr, nc) not in seen and is_land(grid, nr, nc):
                        seen.add((nr, nc))
                        q.append((nr, nc))
            sizes.append(size)
    sizes.sort(reverse=True)
    return {
        "islands": len(sizes),
        "largest": sizes[0] if sizes else 0,
        "sizes": sizes,
    }


def main(argv: list[str]) -> int:
    if len(argv) != 2:
        sys.stderr.write("usage: islands.py <grid.txt> <out.json>\n")
        return 2
    with open(argv[0], encoding="utf-8") as fh:
        result = solve(fh.read())
    with open(argv[1], "w", encoding="utf-8") as fh:
        json.dump(result, fh, indent=2)
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
