#!/usr/bin/env python3
"""aoc21 day 6 pt 2"""

import copy


def main(filename: str, days: int) -> int:
    fish_groups = [0]*9
    with open(filename) as f:
        ages = f.read()[:-1].split(",")
    for a in ages:
        fish_groups[int(a)] += 1
    for _ in range(days):
        fish_groups_old = copy.copy(fish_groups)
        for i in range(0, 8):
            fish_groups[i] = fish_groups_old[i+1]
        fish_groups[8] = fish_groups_old[0]
        fish_groups[6] += fish_groups_old[0]
    return sum(fish_groups)


if __name__ == "__main__":
    fish = main("test_input.txt", 18)
    assert fish == 26, f"number of lantern fish was not calculated correctly: {fish}"
    fish = main("test_input.txt", 80)
    assert fish == 5934, f"number of lantern fish was not calculated correctly: {fish}"
    fish = main("test_input.txt", 256)
    assert fish == 26984457539, f"number of lantern fish was not calculated correctly: {fish}"
    print(main("input.txt", 256))
