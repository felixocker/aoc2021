#!/usr/bin/env python3
"""aoc21 day 8 pt 1"""

import aocd


def main(data):
    number_lengths = {1: 2, 4: 4, 7: 3, 8: 7}
    signals = [l.split(" | ") for l in data.split("\n") if l[:-1]]
    counter = 0
    for s in signals:
        lengths = [len(n) for n in s[1].split()]
        counter += sum(1 for l in lengths if l in number_lengths.values())
    return counter


if __name__ == "__main__":
    with open("test_input.txt") as f:
        result = main(f.read())
    assert result == 26, f"result not as expected: {result}"
    print(main(aocd.get_data(day=8, year=2021)))
