#!/usr/bin/env python3
"""aoc21 day 14 pt 1"""

from collections import Counter
import aocd


def main(data, iterations):
    lines = data.split("\n")
    poly = lines[0]
    insert_rules = dict(l.split(" -> ") for l in lines[2:])
    for _ in range(iterations):
        new_poly = ""
        for c, e in enumerate(poly):
            new_poly += e
            if c < len(poly)-1:
                new_poly += insert_rules["".join([e, poly[c+1]])]
        poly = new_poly
    occurrences = Counter(poly)
    return sorted(occurrences.values())[-1] - sorted(occurrences.values())[0]


if __name__ == "__main__":
    with open("test_input.txt") as f:
        result = main(f.read(), 10)
    assert result == 1588, f"result not as expected: {result}"
    print(main(aocd.get_data(day=14, year=2021), 10))
