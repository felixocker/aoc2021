#!/usr/bin/env python3
"""aoc21 day 1 pt 1"""


def main(filename: str):
    with open(filename, "r") as f:
        lines = f.readlines()
    larger_than_prior = 0
    for c, line in enumerate(lines[1:]):
        if int(line) > int(lines[c]):
            larger_than_prior += 1
    return larger_than_prior


if __name__ == "__main__":
    test_ltp = main("test_input.txt")
    assert test_ltp == 7, f"counter does not work {test_ltp}"
    print(main("input.txt"))
