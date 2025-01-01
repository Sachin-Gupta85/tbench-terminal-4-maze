# Connected same-character regions (flood fill)

Implement `/app/region.py`, run as
`python3 /app/region.py <grid.txt> <out.json>`. A stub exists.

Every character in `<grid.txt>` is a cell, **including spaces**. A **region** is
a maximal group of cells that share the same character and are 4-connected (up,
down, left, right — never diagonal). Rows may have different lengths; a cell
exists at `(r, c)` only when `c` is within that row, and connectivity never
crosses a missing cell.

Write `<out.json>`:

```json
{ "regions": 4, "largest": 6, "sizes": [6, 6, 5, 3] }
```

- `regions` — total number of regions.
- `largest` — size of the biggest region (`0` for an empty grid).
- `sizes` — every region's size, sorted **descending**.

Exit 0. `/app/data/sample/` has a worked example.
