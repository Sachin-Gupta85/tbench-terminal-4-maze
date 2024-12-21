#!/usr/bin/env python3
"""Starter stub for maze — NOT implemented. Write the result to argv[1]."""
import json, sys
def main(argv):
    if len(argv) != 2:
        sys.stderr.write("usage: maze.py <maze.txt> <out.json>\\n"); return 2
    with open(argv[1], "w") as fh: json.dump({"reachable": False, "steps": None, "reachable_cells": 0}, fh)
    return 0
if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
