#!/usr/bin/env python3
"""aoc21 day 9 pt 2"""

from io import StringIO
import math
import numpy as np
import aocd


def extend_basin(floor_map, basin: set, outer: set):
    surroundings = set()
    for (v, h) in outer:
        if v > 0:
            if floor_map[v][h] < floor_map[v - 1][h] < 9:
                surroundings.add((v-1, h))
        if v < floor_map.shape[0] - 1:
            if floor_map[v][h] < floor_map[v + 1][h] < 9:
                surroundings.add((v+1, h))
        if h > 0:
            if floor_map[v][h] < floor_map[v][h - 1] < 9:
                surroundings.add((v, h-1))
        if h < floor_map.shape[1] - 1:
            if floor_map[v][h] < floor_map[v][h + 1] < 9:
                surroundings.add((v, h+1))
    basin.update(outer)
    new_outer = basin.union(surroundings).difference(basin)
    if new_outer:
        extend_basin(floor_map, basin, new_outer)


def main(data) -> int:
    low_points: list = []
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
            low_points.append((v, h))
    basins = [{lp} for lp in low_points]
    for basin in basins:
        extend_basin(floor_map, basin, basin)
    return math.prod(sorted([len(basin) for basin in basins], reverse=True)[:3])


if __name__ == "__main__":
    with open("test_input.txt") as f:
        result = main(f)
    assert result == 1134, f"result not as expected: {result}"
    print(main(StringIO(aocd.get_data(day=9, year=2021))))
