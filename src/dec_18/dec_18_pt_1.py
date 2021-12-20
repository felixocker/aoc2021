#!/usr/bin/env python3
"""aoc21 day 18 pt 1"""

import aocd
import copy
import functools
import json
import math


def snailfish_number_addition(data):
    sfns = [json.loads(line) for line in data.split("\n")]
    sfn_sum = functools.reduce(add, sfns)
    return sfn_sum


def add(sfn_a: list, sfn_b: list) -> list:
    all_clean = False
    sfn_sum = [sfn_a, sfn_b]
    while not all_clean:
        sfn_sum, all_clean = reduce(sfn_sum)
    return sfn_sum


def reduce(sfn_sum: list):
    new_sum = explode(copy.deepcopy(sfn_sum))
    if new_sum != sfn_sum:
        return new_sum, False
    new_sum = split(copy.deepcopy(sfn_sum), False)[0]
    if new_sum != sfn_sum:
        return new_sum, False
    return sfn_sum, True


def explode(sfn_sum: list):
    coords, exploder = get_exploder_coords(sfn_sum, [None, None, None, None], None, 0)
    if exploder:
        sfn_sum[coords[0]][coords[1]][coords[2]][coords[3]] = 0
        for c, coord in enumerate(coords[::-1]):
            partial_coords = coords[:-(c+1)]
            # increase on left side
            if coord == 1 and exploder[0]:
                set_elem_to_side(get_elem_by_coords(sfn_sum, partial_coords), 0, exploder[0], True)
                exploder[0] = None
            # increase on right side
            if coord == 0 and exploder[1]:
                set_elem_to_side(get_elem_by_coords(sfn_sum, partial_coords), 1, exploder[1], True)
                exploder[1] = None
    return sfn_sum


def get_elem_by_coords(sfn: list, coords: list):
    num = sfn
    for c in coords:
        num = num[c]
    return num


def set_elem_to_side(sfn: list, side: int, val: int, initial: bool):
    num_inverted = {0: 1, 1: 0}
    if isinstance(sfn[side], list):
        if initial:
            set_elem_to_side(sfn[side], num_inverted[side], val, False)
        else:
            set_elem_to_side(sfn[side], side, val, False)
    else:
        sfn[side] += val


def get_exploder_coords(sfn_part: list, coords: list, exploder: list, depth: int):
    for c, n in enumerate(sfn_part):
        if not exploder:
            coords[depth] = c
            if isinstance(n, list):
                if depth == 3:
                    exploder = n
                else:
                    coords, exploder = get_exploder_coords(n, copy.copy(coords), exploder, depth+1)
    return coords, exploder


def split(sfn_sum: list, split_status: bool):
    for c, n in enumerate(sfn_sum):
        if not split_status:
            if isinstance(n, int):
                if n > 9:
                    n = [math.floor(n/2), math.ceil(n/2)]
                    split_status = True
            if isinstance(n, list):
                sfn_sum[c], split_status = split(n, split_status)
    return sfn_sum, split_status


def check_magnitude(sfn):
    if isinstance(sfn, list):
        magnitude = 3 * check_magnitude(sfn[0]) + 2 * check_magnitude(sfn[1])
    else:
        magnitude = sfn
    return magnitude


if __name__ == "__main__":
    # test split function
    assert split([10], False)[0] == [[5,5]]
    assert split([11], False)[0] == [[5,6]]
    assert split([[[[0,7],4],[15,[0,13]]],[1,1]], False)[0] == [[[[0,7],4],[[7,8],[0,13]]],[1,1]]
    assert split([[[[0,7],4],[[7,8],[0,13]]],[1,1]], False)[0] == [[[[0,7],4],[[7,8],[0,[6,7]]]],[1,1]]

    # test explode function
    assert explode([[[[[9,8],1],2],3],4]) == [[[[0,9],2],3],4]
    assert explode([7,[6,[5,[4,[3,2]]]]]) == [7,[6,[5,[7,0]]]]
    assert explode([[6,[5,[4,[3,2]]]],1]) == [[6,[5,[7,0]]],3]
    assert explode([[3,[2,[1,[7,3]]]],[6,[5,[4,[3,2]]]]]) == [[3,[2,[8,0]]],[9,[5,[4,[3,2]]]]]
    assert explode([[3, [2, [8, 0]]], [9, [5, [4, [3, 2]]]]]) == [[3,[2,[8,0]]],[9,[5,[7,0]]]]
    assert explode([[[[0, [3, 2]], [3, 3]], [4, 4]], [5, 5]]) == [[[[3, 0], [5, 3]], [4, 4]], [5, 5]]

    # test check_magnitude function
    assert check_magnitude([[1,2],[[3,4],5]]) == 143
    assert check_magnitude([[[[0,7],4],[[7,8],[6,0]]],[8,1]]) == 1384
    assert check_magnitude([[[[1,1],[2,2]],[3,3]],[4,4]]) == 445
    assert check_magnitude([[[[3,0],[5,3]],[4,4]],[5,5]]) == 791
    assert check_magnitude([[[[5,0],[7,4]],[5,5]],[6,6]]) == 1137
    assert check_magnitude([[[[8,7],[7,7]],[[8,6],[7,7]]],[[[0,7],[6,6]],[8,7]]]) == 3488

    # test tiny examples
    data = """[1,1]\n[2,2]\n[3,3]\n[4,4]\n[5,5]"""
    assert snailfish_number_addition(data) == [[[[3, 0], [5, 3]], [4, 4]], [5, 5]]

    data = """[1,1]\n[2,2]\n[3,3]\n[4,4]\n[5,5]\n[6,6]"""
    assert snailfish_number_addition(data) == [[[[5, 0], [7, 4]], [5, 5]], [6, 6]]

    data = """[[[0,[4,5]],[0,0]],[[[4,5],[2,6]],[9,5]]]
        [7,[[[3,7],[4,3]],[[6,3],[8,8]]]]
        [[2,[[0,8],[3,4]]],[[[6,7],1],[7,[1,6]]]]
        [[[[2,4],7],[6,[0,5]]],[[[6,8],[2,8]],[[2,1],[4,5]]]]
        [7,[5,[[3,8],[1,4]]]]
        [[2,[2,2]],[8,[8,1]]]
        [2,9]
        [1,[[[9,3],9],[[9,0],[0,7]]]]
        [[[5,[7,4]],7],1]
        [[[[4,2],2],6],[8,7]]"""
    assert snailfish_number_addition(data) == [[[[8, 7], [7, 7]], [[8, 6], [7, 7]]], [[[0, 7], [6, 6]], [8, 7]]]

    # test example input
    with open("test_input.txt") as f:
        result = check_magnitude(snailfish_number_addition(f.read()))
    assert result == 4140, f"result not as expected: {result}"

    print(check_magnitude(snailfish_number_addition(aocd.get_data(day=18, year=2021))))
