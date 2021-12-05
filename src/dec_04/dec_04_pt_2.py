#!/usr/bin/env python3
"""aoc21 day 3 pt 2"""

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
    rm = []
    num_rows, num_cols = arrays[0].shape
    for arr in arrays:
        arr[arr == num] = None
        if any(all(np.isnan(e) for e in arr[r, :]) for r in range(num_rows)) or\
           any(all(np.isnan(e) for e in arr[:, c]) for c in range(num_cols)):
            if len(arrays) == 1:
                res = np.nansum(arr)
                break
            else:
                rm.append(arr)
    for r in rm:
        # print([a for a in arrays if np.array_equal(a, r, equal_nan=True)])
        arrays = [a for a in arrays if not np.array_equal(a, r, equal_nan=True)]
    return arrays, res


def main(filename: str) -> int:
    nums_drawn, arrays = extract_data(filename)
    n, res = 0, 0
    for n in nums_drawn:
        arrays, res = update_and_check(arrays, n)
        if res:
            break
    return n * res


if __name__ == "__main__":
    score = main("test_input.txt")
    assert score == 1924, f"score was not calculated correctly: {score}"
    print(main("input.txt"))
