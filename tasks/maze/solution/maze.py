#!/usr/bin/env python3
"""Shortest path and reachability in a grid maze.

Usage:  python3 maze.py <maze.txt> <out.json>

The maze is a text grid. Passable cells are '.', 'S' (start) and 'E' (end);
every other character (including '#' and spaces) is a wall. Movement is
4-directional (up/down/left/right), one cell per step. Rows may differ in
length; positions past the end of a row are walls.

Output:
    {
      "reachable": <bool>,         # can E be reached from S
      "steps": <int or null>,      # fewest moves S -> E, null if unreachable
      "reachable_cells": <int>     # passable cells reachable from S (including S)
    }
"""
from __future__ import annotations

import json
import sys
from collections import deque

PASSABLE = {".", "S", "E"}


def parse(text: str):
    grid = text.split("\n")
    if grid and grid[-1] == "":
        grid.pop()                     # drop trailing newline's empty row
    start = end = None
    for r, row in enumerate(grid):
        for c, ch in enumerate(row):
            if ch == "S":
                start = (r, c)
            elif ch == "E":
                end = (r, c)
    return grid, start, end


def passable(grid, r, c) -> bool:
    if r < 0 or r >= len(grid):
        return False
    row = grid[r]
    if c < 0 or c >= len(row):
        return False
    return row[c] in PASSABLE


def solve(text: str) -> dict:
    grid, start, end = parse(text)
    if start is None:
        raise ValueError("no start 'S' in maze")

    dist = {start: 0}
    q = deque([start])
    while q:
        r, c = q.popleft()
        for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            nr, nc = r + dr, c + dc
            if (nr, nc) not in dist and passable(grid, nr, nc):
                dist[(nr, nc)] = dist[(r, c)] + 1
                q.append((nr, nc))

    reachable = end is not None and end in dist
    return {
        "reachable": reachable,
        "steps": dist[end] if reachable else None,
        "reachable_cells": len(dist),
    }


def main(argv: list[str]) -> int:
    if len(argv) != 2:
        sys.stderr.write("usage: maze.py <maze.txt> <out.json>\n")
        return 2
    with open(argv[0], encoding="utf-8") as fh:
        result = solve(fh.read())
    with open(argv[1], "w", encoding="utf-8") as fh:
        json.dump(result, fh, indent=2)
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
