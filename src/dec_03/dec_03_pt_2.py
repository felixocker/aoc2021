#!/usr/bin/env python3
"""aoc21 day 3 pt 2"""

import copy


def bin_str_to_int(bin_str: str) -> int:
    res = 0
    for c, _ in enumerate(bin_str):
        res += 2**c*int(bin_str[len(bin_str)-1-c])
    return res


def invert_bin_str(bin_str: str) -> str:
    return "".join("0" if i == "1" else "1" for i in bin_str)


def filter_numbers(filename: str) -> list:
    with open(filename, "r") as f:
        lines = f.read().splitlines()
    results = {
        "oxygen": None,
        "co2": None,
    }
    for ratingtype in results:
        nums = copy.copy(lines)
        pos = 0
        while len(nums) > 1:
            nums = filter_by_occurrence(nums, pos, ratingtype)
            pos += 1
        results[ratingtype] = nums[0]
    return list(results.values())


def filter_by_occurrence(nums: list, pos: int, ratingtype: str) -> list:
    ones = sum(int(line[pos]) for line in nums)
    var = "0"
    if ratingtype == "oxygen" and ones >= len(nums)/2 or ratingtype == "co2" and ones < len(nums)/2:
        var = "1"
    return [num for num in nums if num[pos] == var]


def main(filename: str) -> int:
    oxygen_generator_rating, co2_scrubber_rating = filter_numbers(filename)
    life_support_rating = bin_str_to_int(oxygen_generator_rating) * bin_str_to_int(co2_scrubber_rating)
    return life_support_rating


if __name__ == "__main__":
    lsr = main("test_input.txt")
    assert lsr == 230, f"life support rating not calculated correctly: {lsr}"
    print(main("input.txt"))
