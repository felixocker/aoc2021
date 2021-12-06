#!/usr/bin/env python3
"""aoc21 day 5 pt 2"""

import numpy as np


def parse_input(filename: str):
    with open(filename) as f:
        coords = [(li.split(" -> ")[0].split(","), li.split(" -> ")[1].split(",")) for li in f.read().splitlines()]
    int_coords = [((int(c[0][0]), int(c[0][1])), (int(c[1][0]), int(c[1][1]))) for c in coords]
    reduced_coords = [((c[0][0], c[0][1]), (c[1][0], c[1][1])) for c in int_coords if c[0][0] == c[1][0] or
                      c[0][1] == c[1][1] or abs(c[0][0]-c[1][0]) == abs(c[0][1]-c[1][1])]
    x_max = max([c[0][0] for c in reduced_coords] + [c[1][0] for c in reduced_coords]) + 1
    y_max = max([c[0][1] for c in reduced_coords] + [c[1][1] for c in reduced_coords]) + 1
    return reduced_coords, (x_max, y_max)


def create_map(x_len, y_len, data: list):
    arr = np.full((y_len, x_len), 0)
    for c in data:
        if c[0][0] == c[1][0]:
            for y in range(min(c[0][1], c[1][1]), max(c[0][1], c[1][1])+1):
                arr[y][c[0][0]] += 1
        elif c[0][1] == c[1][1]:
            for x in range(min(c[0][0], c[1][0]), max(c[0][0], c[1][0])+1):
                arr[c[0][1]][x] += 1
        else:
            delta = range(abs(c[0][0] - c[1][0]) + 1)
            x_direction, y_direction = 1, 1
            if c[0][0] > c[1][0]:
                x_direction = -1
            if c[0][1] > c[1][1]:
                y_direction = -1
            for d in delta:
                arr[c[0][1] + y_direction * d][c[0][0] + x_direction * d] += 1
    return arr


def main(filename: str):
    coords, shape = parse_input(filename)
    vent_map = create_map(*shape, coords)
    return (vent_map >= 2).sum()


if __name__ == "__main__":
    critical = main("test_input.txt")
    assert critical == 12, f"number of critical points was not calculated correctly: {critical}"
    print(main("input.txt"))
