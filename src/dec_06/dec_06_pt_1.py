#!/usr/bin/env python3
"""aoc21 day 6 pt 1"""

from dataclasses import dataclass


@dataclass
class Fish:
    internal_timer: int = 8

    def spawn_new(self):
        self.internal_timer = 6
        return Fish()

    def age(self):
        if self.internal_timer == 0:
            return self.spawn_new()
        self.internal_timer -= 1


def main(filename: str, days: int) -> int:
    with open(filename) as f:
        ages = f.read()[:-1].split(",")
    fish_population = [Fish(internal_timer=int(a)) for a in ages]
    for _ in range(days):
        new_fish = [f.age() for f in fish_population]
        fish_population.extend(f for f in new_fish if f)
    return len(fish_population)


if __name__ == "__main__":
    fish = main("test_input.txt", 18)
    assert fish == 26, f"number of lantern fish was not calculated correctly: {fish}"
    fish = main("test_input.txt", 80)
    assert fish == 5934, f"number of lantern fish was not calculated correctly: {fish}"
    print(main("input.txt", 80))
