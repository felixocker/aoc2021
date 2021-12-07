#!/usr/bin/env python3
"""aoc21 day 7 pt 2"""

import statistics
import aocd


def gauss_sum(n: int) -> int:
    return n*(n+1)//2


def main(positions: str):
    positions = [int(i) for i in positions.split(",")]
    best_pos = round(statistics.mean(positions))
    return sum(gauss_sum(abs(p-best_pos)) for p in positions)


if __name__ == "__main__":
    result = main("16,1,2,0,4,2,7,1,2,14")
    assert result == 168, f"result not as expected: {result}"
    print(main(aocd.get_data(day=7, year=2021)))
