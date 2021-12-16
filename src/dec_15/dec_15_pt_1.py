#!/usr/bin/env python3
"""aoc21 day 15 pt 1"""

import aocd
import numpy as np


def find_neighbours(coords: tuple, value_map: np.array):
    neighbours = [(coords[0]-1, coords[1]), (coords[0]+1, coords[1]), (coords[0], coords[1]-1), (coords[0], coords[1]+1)]
    return {n for n in neighbours if not np.isnan(value_map[n[0]][n[1]])}


def dijkstra(padded_map, start, end):
    nodes = [(i, j) for i in range(1, padded_map.shape[0]-1) for j in range(1, padded_map.shape[1]-1)]
    distances = {n: float('inf') for n in nodes}
    priors = {n: None for n in nodes}
    distances[start] = 0
    while end in nodes:
        closest = sorted(nodes, key=lambda x: distances[x])[0]
        nodes.remove(closest)
        for neighbour in find_neighbours(closest, padded_map):
            if neighbour in nodes:
                update_distance(closest, neighbour, distances, priors, padded_map)
    return distances[end]


def update_distance(closest, neighbour, distances, priors, padded_map):
    alternative = distances[closest] + padded_map[neighbour[0]][neighbour[1]]
    if alternative < distances[neighbour]:
        distances[neighbour] = alternative
        priors[neighbour] = closest


def main(data):
    risk_data = [[float(c) for c in l] for l in data.split("\n")]
    risk_map = np.array(risk_data, dtype=float)
    padded_map = np.pad(risk_map, 1, 'constant', constant_values=np.nan)
    endpoint = (padded_map.shape[0]-2, padded_map.shape[1]-2)
    return dijkstra(padded_map, (1, 1), endpoint)


if __name__ == "__main__":
    with open("test_input.txt") as f:
        result = main(f.read())
    assert result == 40, f"result not as expected: {result}"
    print(main(aocd.get_data(day=15, year=2021)))
