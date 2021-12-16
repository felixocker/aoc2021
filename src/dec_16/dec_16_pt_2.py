#!/usr/bin/env python3
"""aoc21 day 16 pt 2"""

import aocd
from functools import reduce
import operator


def main(data):
    bin_data = add_leading_zeros(data)
    top = init_packet(bin_data)
    return top.evaluate()


def add_leading_zeros(hex_num):
    bin_num = hex_to_bin(hex_num)
    shortened_len = len(bin_num)
    full_len = len(hex_to_bin("F"*len(hex_num)))
    return "0"*(full_len - shortened_len) + bin_num


def init_packet(bin_data):
    packet_version = bin_to_dec(bin_data[0:3])
    packet_type = bin_to_dec(bin_data[3:6])
    if packet_type == 4:
        p = Literal(bin_data, packet_version, packet_type)
    else:
        p = Operator(bin_data, packet_version, packet_type)
    return p


class Operator:
    def __init__(self, p_string, p_version, p_type):
        self.p_string = p_string
        self.p_version = p_version
        self.p_type = p_type
        self.len_id = p_string[6]
        self.sub_packets: list = []
        self.rest: str = ""
        self.length_of_ps: int = 0
        self.number_of_ps: int = 0
        if self.len_id == "0":
            self.length_of_ps = bin_to_dec(p_string[7:22])
            self.rest = p_string[22:22+self.length_of_ps]
            self._read_packages_by_length()
            self.rest = p_string[22+self.length_of_ps:]
        elif self.len_id == "1":
            self.number_of_ps = bin_to_dec(p_string[7:18])
            self.rest = p_string[18:]
            self._read_packages_by_number()
        self.function_dict = {
            0: sum,
            1: self.__prod,
            2: min,
            3: max,
            5: self.__greater,
            6: self.__less,
            7: self.__equal,
        }

    @staticmethod
    def __prod(operands: list):
        return reduce(operator.mul, operands, 1)

    @staticmethod
    def __greater(operands: list):
        assert len(operands) == 2, "greater than comparison only works for lists of length two"
        return 1 * (operands[0] > operands[1])

    @staticmethod
    def __less(operands: list):
        assert len(operands) == 2, "less than comparison only works for lists of length two"
        return 1 * (operands[0] < operands[1])

    @staticmethod
    def __equal(operands: list):
        assert len(operands) == 2, "equal to comparison only works for lists of length two"
        return 1 * (operands[0] == operands[1])

    def _read_packages_by_length(self):
        while self.rest:
            self.sub_packets.append(init_packet(self.rest))
            self.rest = self.sub_packets[-1].rest

    def _read_packages_by_number(self):
        while len(self.sub_packets) < self.number_of_ps:
            self.sub_packets.append(init_packet(self.rest))
            self.rest = self.sub_packets[-1].rest

    def get_version_sum(self):
        return sum(p.get_version_sum() for p in self.sub_packets) + self.p_version

    def evaluate(self):
        try:
            fun = self.function_dict[self.p_type]
        except KeyError:
            raise KeyError(f"no function defined for self.p_type")
        return fun([sp.evaluate() for sp in self.sub_packets])


class Literal:
    def __init__(self, p_string, p_version, p_type):
        self.p_string = p_string
        self.p_version = p_version
        self.p_type = p_type
        self.bin_number: str = ""
        self.rest: str = p_string[6:]
        self._init_numbers()
        self.dec_number = bin_to_dec(self.bin_number)

    def _init_numbers(self):
        while self.rest[0] != "0":
            self.bin_number += self.rest[1:5]
            self.rest = self.rest[5:]
        self.bin_number += self.rest[1:5]
        self.rest = self.rest[5:]

    def get_version_sum(self):
        return self.p_version

    def evaluate(self):
        return self.dec_number


def hex_to_bin(hexv):
    return bin(int(hexv, 16))[2:]


def bin_to_dec(binv):
    return int(binv, 2)


if __name__ == "__main__":
    assert main("C200B40A82") == 3, f"expression evaluation not as expected"
    assert main("04005AC33890") == 54, f"expression evaluation not as expected"
    assert main("880086C3E88112") == 7, f"expression evaluation not as expected"
    assert main("CE00C43D881120") == 9, f"expression evaluation not as expected"
    assert main("D8005AC2A8F0") == 1, f"expression evaluation not as expected"
    assert main("F600BC2D8F") == 0, f"expression evaluation not as expected"
    assert main("9C005AC2F8F0") == 0, f"expression evaluation not as expected"
    assert main("9C0141080250320F1802104A08") == 1, f"expression evaluation not as expected"
    print(main(aocd.get_data(day=16, year=2021)))
