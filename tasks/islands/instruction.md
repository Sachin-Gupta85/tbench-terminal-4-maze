# Count islands in a grid

Implement `/app/islands.py`, run as
`python3 /app/islands.py <grid.txt> <out.json>`. A stub exists.

`<grid.txt>` is a text grid. Land cells are `#`; every other character
(including spaces) is water. Two land cells are part of the same **island** when
they are 4-connected (up, down, left, right — never diagonal). Rows may have
different lengths; any position past the end of a row is water.

Write `<out.json>`:

```json
{ "islands": 5, "largest": 2, "sizes": [2, 2, 2, 1, 1] }
```

- `islands` — number of connected land components.
- `largest` — size of the biggest island (`0` if there is no land).
- `sizes` — every island's size, sorted **descending**.

Exit 0. `/app/data/sample/` has a worked example.
