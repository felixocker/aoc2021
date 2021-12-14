#!/usr/bin/env python3
"""aoc21 day 14 pt 2"""

from collections import Counter
import copy
import aocd


def main(data, iterations):
    lines = data.split("\n")
    poly = lines[0]
    init_tuples = ["".join((poly[i], poly[i+1])) for i in range(len(poly)-1)]
    occurrences = dict(Counter(init_tuples))
    insert_rules = dict(l.split(" -> ") for l in lines[2:])
    letters_from_insert = "".join(v for v in insert_rules.values())
    insert_rules = {k: ["".join([k[0], v]), "".join([v, k[1]])] for k, v in insert_rules.items()}
    letters = dict(Counter(poly))
    for l in letters_from_insert:
        if l not in letters:
            letters[l] = 0
    for _ in range(iterations):
        old_occurrences = copy.copy(occurrences)
        for k in old_occurrences:
            for v in insert_rules[k]:
                if v not in occurrences:
                    occurrences[v] = old_occurrences[k]
                else:
                    occurrences[v] += old_occurrences[k]
            letters[insert_rules[k][0][1]] += old_occurrences[k]
            occurrences[k] -= old_occurrences[k]
    return sorted(letters.values())[-1] - sorted(letters.values())[0]


if __name__ == "__main__":
    with open("test_input.txt") as f:
        result = main(f.read(), 40)
    assert result == 2188189693529, f"result not as expected: {result}"
    print(main(aocd.get_data(day=14, year=2021), 40))
