#!/usr/bin/env python3
"""Connected same-character regions in a grid (flood fill).

Usage:  python3 region.py <grid.txt> <out.json>

Every character in the grid is a cell, including spaces. A region is a maximal
set of cells that share the same character and are 4-connected
(up/down/left/right). Rows may differ in length; a cell exists at (r, c) only
when c is within that row, and connectivity never crosses a missing cell.

Output:
    {
      "regions": <int>,   # total number of regions
      "largest": <int>,   # size of the biggest region (0 for an empty grid)
      "sizes":   [<int>]  # every region's size, sorted descending
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


def at(grid, r, c):
    if r < 0 or r >= len(grid):
        return None
    row = grid[r]
    if c < 0 or c >= len(row):
        return None
    return row[c]


def solve(text: str) -> dict:
    grid = parse(text)
    seen = set()
    sizes = []
    for r, row in enumerate(grid):
        for c, ch in enumerate(row):
            if (r, c) in seen:
                continue
            size = 0
            q = deque([(r, c)])
            seen.add((r, c))
            while q:
                cr, cc = q.popleft()
                size += 1
                for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                    nr, nc = cr + dr, cc + dc
                    if (nr, nc) not in seen and at(grid, nr, nc) == ch:
                        seen.add((nr, nc))
                        q.append((nr, nc))
            sizes.append(size)
    sizes.sort(reverse=True)
    return {
        "regions": len(sizes),
        "largest": sizes[0] if sizes else 0,
        "sizes": sizes,
    }


def main(argv: list[str]) -> int:
    if len(argv) != 2:
        sys.stderr.write("usage: region.py <grid.txt> <out.json>\n")
        return 2
    with open(argv[0], encoding="utf-8") as fh:
        result = solve(fh.read())
    with open(argv[1], "w", encoding="utf-8") as fh:
        json.dump(result, fh, indent=2)
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
