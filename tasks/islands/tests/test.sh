#!/bin/bash
set -uo pipefail
mkdir -p /logs/verifier
TASK_BIN=/app/islands.py python3 -m unittest discover -s /tests -v
rc=$?
[ "$rc" -eq 0 ] && echo -n 1 > /logs/verifier/reward.txt || echo -n 0 > /logs/verifier/reward.txt
exit 0
