# Solve a grid maze

Write `/app/maze.py`, run as `python3 /app/maze.py <maze.txt> <out.json>`.

`<maze.txt>` is a text grid. Passable cells are `.`, `S` (the start) and `E`
(the end). Every other character — including `#` and spaces — is a wall. You may
move one cell at a time in four directions (up, down, left, right); you cannot
move diagonally or off the grid. Rows may have different lengths; any position
past the end of a row is a wall.

Compute, by breadth-first search from `S`:

```json
{
  "reachable": true,
  "steps": 8,
  "reachable_cells": 18
}
```

- `reachable` — can `E` be reached from `S`? (`true`/`false`)
- `steps` — the fewest moves from `S` to `E`; `null` if `E` is unreachable.
- `reachable_cells` — how many passable cells are reachable from `S`, counting
  `S` itself.

You can assume exactly one `S`. `E` may or may not be reachable (and the suite
includes unreachable mazes). Exit 0 on success. `/app/data/sample/` has a worked
example.
