#!/usr/bin/env python3
"""Total perimeter of the land in a grid.

Usage:  python3 perimeter.py <grid.txt> <out.json>

Land cells are '#'; every other character (including spaces) is water. Each land
cell contributes one unit of perimeter for every one of its four sides
(up/down/left/right) that touches water or the outside of the grid — that is,
4 minus the number of its 4-neighbours that are land. Rows may differ in length;
positions past the end of a row are water.

Output:
    {
      "land_cells": <int>,  # number of '#' cells
      "perimeter":  <int>   # total exposed edge length of all land
    }
"""
from __future__ import annotations

import json
import sys


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
    land = 0
    perimeter = 0
    for r, row in enumerate(grid):
        for c, ch in enumerate(row):
            if ch != "#":
                continue
            land += 1
            for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                if not is_land(grid, r + dr, c + dc):
                    perimeter += 1
    return {"land_cells": land, "perimeter": perimeter}


def main(argv: list[str]) -> int:
    if len(argv) != 2:
        sys.stderr.write("usage: perimeter.py <grid.txt> <out.json>\n")
        return 2
    with open(argv[0], encoding="utf-8") as fh:
        result = solve(fh.read())
    with open(argv[1], "w", encoding="utf-8") as fh:
        json.dump(result, fh, indent=2)
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
