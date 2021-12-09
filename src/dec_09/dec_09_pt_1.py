#!/usr/bin/env python3
"""aoc21 day 9 pt 1"""

from io import StringIO
import numpy as np
import aocd


def main(data) -> int:
    risk_level_sum: int = 0
    map_data = [[int(c) for c in l if c != "\n"] for l in data]
    floor_map = np.array(map_data)
    for v in range(floor_map.shape[0]):
        for h in range(floor_map.shape[1]):
            if v > 0:
                if floor_map[v][h] >= floor_map[v-1][h]:
                    continue
            if v < floor_map.shape[0] - 1:
                if floor_map[v][h] >= floor_map[v+1][h]:
                    continue
            if h > 0:
                if floor_map[v][h] >= floor_map[v][h-1]:
                    continue
            if h < floor_map.shape[1] - 1:
                if floor_map[v][h] >= floor_map[v][h+1]:
                    continue
            risk_level_sum += floor_map[v][h]+1
    return risk_level_sum


if __name__ == "__main__":
    with open("test_input.txt") as f:
        result = main(f)
    assert result == 15, f"result not as expected: {result}"
    print(main(StringIO(aocd.get_data(day=9, year=2021))))
