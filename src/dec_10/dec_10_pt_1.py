#!/usr/bin/env python3
"""aoc21 day 10 pt 1"""

from io import StringIO
import aocd


def calc_score(invalid_chars: list) -> int:
    scores = {")": 3, "]": 57, "}": 1197, ">": 25137}
    return sum(scores[c] for c in invalid_chars)


def main(data):
    valid = {")": "(", "]": "[", "}": "{", ">": "<"}
    lines = [l[:-1] for l in data]
    invalid_chars = []
    for line in lines:
        stack = []
        for c in line:
            if c in valid.values():
                stack.append(c)
            elif stack[-1] == valid[c]:
                stack.pop()
            else:
                invalid_chars.append(c)
                stack.pop()
    return calc_score(invalid_chars)


if __name__ == "__main__":
    with open("test_input.txt") as f:
        result = main(f)
    assert result == 26397, f"result not as expected: {result}"
    print(main(StringIO(aocd.get_data(day=10, year=2021))))
