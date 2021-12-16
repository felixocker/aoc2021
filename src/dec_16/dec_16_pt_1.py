#!/usr/bin/env python3
"""aoc21 day 16 pt 1"""

import aocd


def main(data):
    bin_data = add_leading_zeros(data)
    top = init_packet(bin_data)
    return top.get_version_sum()


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


def hex_to_bin(hexv):
    return bin(int(hexv, 16))[2:]


def bin_to_dec(binv):
    return int(binv, 2)


if __name__ == "__main__":
    assert main("D2FE28") == 6, f"version sum not as expected"
    assert main("8A004A801A8002F478") == 16, f"version sum not as expected"
    assert main("620080001611562C8802118E34") == 12, f"version sum not as expected"
    assert main("C0015000016115A2E0802F182340") == 23, f"version sum not as expected"
    assert main("A0016C880162017C3686B18A3D4780") == 31, f"version sum not as expected"
    print(main(aocd.get_data(day=16, year=2021)))
