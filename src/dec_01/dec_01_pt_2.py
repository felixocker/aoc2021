#!/usr/bin/env python3
"""aoc21 day 1 pt 2"""


def main(filename: str):
    with open(filename, "r") as f:
        lines = f.readlines()
    larger_than_prior = 0
    for c, _ in enumerate(lines[1:-2]):
        sum_current = sum([int(e) for e in lines[c+1:c+4]])
        sum_prior = sum([int(e) for e in lines[c:c+3]])
        if sum_current > sum_prior:
            larger_than_prior += 1
    return larger_than_prior


if __name__ == "__main__":
    test_ltp = main("test_input.txt")
    assert test_ltp == 5, f"counter does not work {test_ltp}"
    print(main("input.txt"))
