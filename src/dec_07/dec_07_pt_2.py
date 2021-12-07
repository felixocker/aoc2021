#!/usr/bin/env python3
"""aoc21 day 7 pt 2"""

import aocd


def gauss_sum(n: int) -> int:
    return n*(n+1)//2


def main(positions: str):
    positions = [int(i) for i in positions.split(",")]
    fuel_costs: dict = {}
    for pos in range(min(positions), max(positions)+1):
        fuel_costs[pos] = sum(gauss_sum(abs(p-pos)) for p in positions)
    best_pos = min(fuel_costs, key=fuel_costs.get)
    return fuel_costs[best_pos]


if __name__ == "__main__":
    result = main("16,1,2,0,4,2,7,1,2,14")
    assert result == 168, f"result not as expected: {result}"
    print(main(aocd.get_data(day=7, year=2021)))
