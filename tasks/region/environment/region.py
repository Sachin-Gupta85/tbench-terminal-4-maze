#!/usr/bin/env python3
"""Starter stub for region — NOT implemented. Write the result to argv[1]."""
import json, sys
def main(argv):
    if len(argv) != 2:
        sys.stderr.write("usage: region.py <grid.txt> <out.json>\n"); return 2
    with open(argv[1], "w") as fh:
        json.dump({"regions": 0, "largest": 0, "sizes": []}, fh)
    return 0
if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
