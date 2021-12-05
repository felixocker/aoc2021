#!/usr/bin/env python3
"""aoc21 day 3 pt 1"""

import numpy as np
from io import StringIO


def extract_data(filename: str):
    # TODO: refactor
    with open(filename, "r") as f:
        lines = f.read().splitlines()
    nums_drawn = [int(n) for n in lines[0].split(",")]
    arrays: list = []
    arr_str = ""
    for c, line in enumerate(lines[2:]):
        arr_str += line
        if line == "" or c == len(lines)-3:
            sio = StringIO(arr_str)
            arr = np.loadtxt(sio)
            arrays.append(arr)
            arr_str = ""
        else:
            arr_str += "\n"
    return nums_drawn, arrays


def update_and_check(arrays: list, num):
    res = None
    num_rows, num_cols = arrays[0].shape
    for arr in arrays:
        arr[arr == num] = None
        if any(all(np.isnan(e) for e in arr[r, :]) for r in range(num_rows)) or\
           any(all(np.isnan(e) for e in arr[:, c]) for c in range(num_cols)):
            res = np.nansum(arr)
            break
    return res


def main(filename: str) -> int:
    nums_drawn, arrays = extract_data(filename)
    n, res = 0, 0
    for n in nums_drawn:
        res = update_and_check(arrays, n)
        if res:
            break
    return n * res


if __name__ == "__main__":
    score = main("test_input.txt")
    assert score == 4512, f"score was not calculated correctly: {score}"
    print(main("input.txt"))
