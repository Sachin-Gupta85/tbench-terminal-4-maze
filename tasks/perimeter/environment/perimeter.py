#!/usr/bin/env python3
"""Starter stub for perimeter — NOT implemented. Write the result to argv[1]."""
import json, sys
def main(argv):
    if len(argv) != 2:
        sys.stderr.write("usage: perimeter.py <grid.txt> <out.json>\n"); return 2
    with open(argv[1], "w") as fh:
        json.dump({"land_cells": 0, "perimeter": 0}, fh)
    return 0
if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
