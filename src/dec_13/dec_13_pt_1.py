#!/usr/bin/env python3
"""aoc21 day 13 pt 1"""

import aocd
import numpy as np


def y_fold(arr, y_val):
    new_arr = arr[:y_val, :]
    for y in range(y_val+1, min(2*y_val+1, arr.shape[0])):
        for x in range(0, arr.shape[1]):
            if arr[y][x] == "X":
                new_arr[2*y_val-y][x] = "X"
    return new_arr


def x_fold(arr, x_val):
    new_arr = arr[:, :x_val]
    for x in range(x_val+1, min(2*x_val+1, arr.shape[1])):
        for y in range(0, arr.shape[0]):
            if arr[y][x] == "X":
                new_arr[y][2*x_val-x] = "X"
    return new_arr


def main(data):
    coords = [(int(l.split(",")[0]), int(l.split(",")[1])) for l in data.split("\n\n")[0].split("\n")]
    folds = [f.split("fold along ")[1].split("=") for f in data.split("\n\n")[1].split("\n") if f]
    h_max = max(c[0] for c in coords)+1
    v_max = max(c[1] for c in coords)+1
    arr = np.full((v_max, h_max), " ", dtype=object)
    for c in coords:
        arr[c[1]][c[0]] = "X"
    for f in folds[:1]:
        if f[0] == "x":
            arr = x_fold(arr, int(f[1]))
        elif f[0] == "y":
            arr = y_fold(arr, int(f[1]))
    return (arr == "X").sum()


if __name__ == "__main__":
    with open("test_input.txt") as f:
        result = main(f.read())
    assert result == 17, f"result not as expected: {result}"
    print(main(aocd.get_data(day=13, year=2021)))
