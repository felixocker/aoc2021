#!/usr/bin/env python3
"""aoc21 day 8 pt 2"""

import aocd


def init_digit_dict(digit_strs: list) -> dict:
    digit_dict: dict = {}
    for s in digit_strs:
        for length, digit in [(2, 1), (3, 7), (4, 4), (7, 8)]:
            if len(s) == length:
                digit_dict[digit] = "".join(sorted(s))
    for s in digit_strs:
        if len(s) == 6:
            if set(s) > set(digit_dict[4]):
                digit_dict[9] = "".join(sorted(s))
            elif set(s) > set(digit_dict[1]):
                digit_dict[0] = "".join(sorted(s))
            else:
                digit_dict[6] = "".join(sorted(s))
    for s in digit_strs:
        if len(s) == 5:
            if set(s) > set(digit_dict[1]):
                digit_dict[3] = "".join(sorted(s))
            elif set(s) < set(digit_dict[9]):
                digit_dict[5] = "".join(sorted(s))
            else:
                digit_dict[2] = "".join(sorted(s))
    return {v: k for k, v in digit_dict.items()}


def main(data):
    signals = [l.split(" | ") for l in data.split("\n") if l[:-1]]
    counter = 0
    for s in signals:
        num: list = []
        dt = init_digit_dict(s[0].split())
        for n in s[1].split():
            num.append(dt["".join(sorted(n))])
        counter += int("".join(str(i) for i in num))
    return counter


if __name__ == "__main__":
    with open("test_input.txt") as f:
        result = main(f.read())
    assert result == 61229, f"result not as expected: {result}"
    print(main(aocd.get_data(day=8, year=2021)))
