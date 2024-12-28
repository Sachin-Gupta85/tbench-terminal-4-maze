# Total perimeter of the land

Implement `/app/perimeter.py`, run as
`python3 /app/perimeter.py <grid.txt> <out.json>`. A stub exists.

`<grid.txt>` is a text grid. Land cells are `#`; every other character
(including spaces) is water. Each land cell contributes one unit of perimeter
for every one of its four sides that touches water or the outside of the grid —
that is, `4` minus the number of its 4-neighbours that are land. Rows may have
different lengths; any position past the end of a row is water.

Write `<out.json>`:

```json
{ "land_cells": 9, "perimeter": 20 }
```

- `land_cells` — number of `#` cells.
- `perimeter` — total exposed edge length of all land.

Exit 0. `/app/data/sample/` has a worked example.
