# 🧭 tbench-terminal-4-maze — grid & graph tasks

> A collection of **Terminal-Bench 3**-style grid/graph tasks for coding agents: parse a character grid and emit a structured JSON answer, graded by exact comparison on unseen grids.

![Python](https://img.shields.io/badge/Python-3.10%2B-blue)
![Format](https://img.shields.io/badge/format-Terminal--Bench%203-6f42c1)
![Tasks](https://img.shields.io/badge/tasks-4-informational)
![Deps](https://img.shields.io/badge/dependencies-none-brightgreen)

Compact algorithmic tasks over a text grid — BFS, connected components, flood
fill, edge counting — where the care points are ragged rows, treating every
non-marker glyph (including spaces) as background, and **deterministic output**.

---

## 📦 Tasks

| Task | Problem |
|---|---|
| [`maze`](tasks/maze) | BFS shortest path `S`→`E`, reachability, component size |
| [`islands`](tasks/islands) | count 4-connected `#` islands + their sizes |
| [`region`](tasks/region) | maximal connected same-character regions (flood fill) |
| [`perimeter`](tasks/perimeter) | total exposed edge length of all `#` land |

## ✅ Verify every task (no dependencies)

```bash
python3 run_checks.py
```

```
islands     Oracle=1  Nop=0  ✅
maze        Oracle=1  Nop=0  ✅
perimeter   Oracle=1  Nop=0  ✅
region      Oracle=1  Nop=0  ✅
ALL 4 TASKS GOOD ✅
```

Each task has `instruction.md`, `task.toml`, `environment/` (stub + `data/sample/`),
`solution/` (reference), and `tests/` (hidden grader + held-out grids).

## 📎 Note

Terminal-Bench 3 **task-authoring** structure with a lightweight local runner,
published as **portfolio examples of agent-task design**.

## 📝 License

MIT — see [LICENSE](LICENSE).
