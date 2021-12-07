#!/usr/bin/env python3
"""aoc21 day 7 pt 1"""

import statistics
import aocd


def main(positions: str):
    positions = [int(i) for i in positions.split(",")]
    best_pos = int(statistics.median(positions))
    return sum(abs(p-best_pos) for p in positions)


if __name__ == "__main__":
    result = main("16,1,2,0,4,2,7,1,2,14")
    assert result == 37, f"result not as expected: {result}"
    print(main(aocd.get_data(day=7, year=2021)))
