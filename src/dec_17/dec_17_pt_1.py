#!/usr/bin/env python3
"""aoc21 day 17 pt 1"""

import aocd
import copy
import math


def main(data):
    x_target = [int(x) for x in data.split(": ")[1].split(", ")[0][2:].split("..")]
    y_target = [int(y) for y in data.split(": ")[1].split(", ")[1][2:].split("..")]
    assert all([x > 0 for x in x_target]), f"target not to right of start"
    assert all([y < 0 for y in y_target]), f"target not below start"
    print(x_target, y_target)
    highest = 0
    for x_vel in range(0, x_target[1]):
        for y_vel in range(0, 1000):
            coords = (0, 0)
            velocity = (copy.copy(x_vel), copy.copy(y_vel))
            while coords[0] <= x_target[1] and coords[1] >= y_target[0]:
                if x_target[0] <= coords[0] <= x_target[1] and y_target[0] <= coords[1] <= y_target[1]:
                    if y_vel > highest:
                        highest = y_vel
                        break
                coords, velocity = update_status(coords, velocity)
    print(highest)
    return gauss_sum(highest)


def update_status(coords: tuple, velocity: tuple) -> tuple:
    new_coords = (coords[0]+velocity[0], coords[1]+velocity[1])
    if velocity[0] != 0:
        x_velocity = math.copysign(abs(velocity[0])-1, velocity[0])
    else:
        x_velocity = 0
    y_velocity = velocity[1] - 1
    new_velocity = (x_velocity, y_velocity)
    return new_coords, new_velocity


def gauss_sum(n: int) -> int:
    return n * (n + 1) // 2


if __name__ == "__main__":
    result = main("target area: x=20..30, y=-10..-5")
    print(result)
    assert result == 45, f"result not as expected: {result}"
    print(main(aocd.get_data(day=17, year=2021)))
