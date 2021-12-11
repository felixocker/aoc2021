#!/usr/bin/env python3
"""aoc21 day 11 pt 2"""

from io import StringIO
import aocd
import numpy as np


def reset_pad(arr, val) -> None:
    arr[0] = arr[-1] = arr[:, 0] = arr[:, -1] = val


def increase_surroundings(arr, coords: tuple) -> None:
    for a in -1, 0, 1:
        for b in -1, 0, 1:
            arr[coords[0]+a][coords[1]+b] += 1


def main(data) -> int:
    octupus_data = [[float(c) for c in l if c != "\n"] for l in data]
    octopus_map = np.array(octupus_data)
    map_w_pad = np.pad(octopus_map, 1, 'constant', constant_values=np.nan)
    step = 0
    while True:
        step += 1
        map_w_pad += 1
        if 10 in map_w_pad:
            while (map_w_pad > 9).any():
                flashing_octs = np.transpose((map_w_pad > 9).nonzero())
                map_w_pad[map_w_pad > 9] = np.nan
                for oct in flashing_octs:
                    increase_surroundings(map_w_pad, oct)
            if (np.isnan(map_w_pad)).all():
                return step
            map_w_pad[np.isnan(map_w_pad)] = 0
            reset_pad(map_w_pad, np.nan)


if __name__ == "__main__":
    with open("test_input.txt") as f:
        result = main(data=f)
    assert result == 195, f"result not as expected: {result}"
    print(main(StringIO(aocd.get_data(day=11, year=2021))))
