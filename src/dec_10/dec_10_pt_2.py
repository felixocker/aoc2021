#!/usr/bin/env python3
"""aoc21 day 10 pt 2"""

from io import StringIO
import aocd


def calc_middle_score(completions: list) -> int:
    assert len(completions) % 2 == 1, "number of completion strings is not odd"
    return sorted(calc_individual_score(completion) for completion in completions)[(len(completions)-1)//2]


def calc_individual_score(completion) -> int:
    scores = {")": 1, "]": 2, "}": 3, ">": 4}
    score = 0
    for c in completion:
        score *= 5
        score += scores[c]
    return score


def get_stack(line: str, valid: dict):
    stack = []
    for c in line:
        if c in valid.values():
            stack.append(c)
        elif stack[-1] == valid[c]:
            stack.pop()
        else:
            stack = None
            break
    return stack


def main(data):
    valid = {")": "(", "]": "[", "}": "{", ">": "<"}
    lookup = {v: k for k, v in valid.items()}
    lines = [l[:-1] for l in data]
    completions: list = []
    for line in lines:
        remaining_stack = get_stack(line, valid)
        if remaining_stack:
            completions.append("".join(lookup[c] for c in reversed(remaining_stack)))
    return calc_middle_score(completions)


if __name__ == "__main__":
    with open("test_input.txt") as f:
        result = main(f)
    assert result == 288957, f"result not as expected: {result}"
    print(main(StringIO(aocd.get_data(day=10, year=2021))))
