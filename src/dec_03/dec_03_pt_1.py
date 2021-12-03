#!/usr/bin/env python3
"""aoc21 day 3 pt 1"""


def bin_str_to_int(bin_str: str) -> int:
    res = 0
    for c, _ in enumerate(bin_str):
        res += 2**c*int(bin_str[len(bin_str)-1-c])
    return res


def invert_bin_str(bin_str: str) -> str:
    return "".join("0" if i == "1" else "1" for i in bin_str)


def count_bit_occurrences(filename: str) -> str:
    with open(filename, "r") as f:
        lines = f.read().splitlines()
    res = ""
    for pos, _ in enumerate(lines[0]):
        ones = sum(int(line[pos]) for line in lines)
        if ones > len(lines)/2:
            res += "1"
        elif ones < len(lines)/2:
            res += "0"
        else:
            print("bits are equally common")
            exit(1)
    return res


def main(filename: str) -> int:
    gamma_rate = count_bit_occurrences(filename)
    epsilon_rate = invert_bin_str(gamma_rate)
    power_consumption = bin_str_to_int(gamma_rate) * bin_str_to_int(epsilon_rate)
    return power_consumption


if __name__ == "__main__":
    pc = main("test_input.txt")
    assert pc == 198, f"power consumption was not calculated correctly: {pc}"
    print(main("input.txt"))
