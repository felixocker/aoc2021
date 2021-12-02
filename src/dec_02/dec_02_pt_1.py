#!/usr/bin/env python3
"""aoc21 day 2 pt 1"""


def main(filename: str):
    x, depth = 0, 0
    with open(filename, "r") as f:
        for line in f.readlines():
            if "forward" in line:
                x += int(line.split(" ")[-1])
            elif "down" in line:
                depth += int(line.split(" ")[-1])
            elif "up" in line:
                depth -= int(line.split(" ")[-1])
    return x*depth


if __name__ == "__main__":
    pos = main("test_input.txt")
    assert pos == 150, f"pos was not calculated correctly: {pos}"
    print(main("input.txt"))
