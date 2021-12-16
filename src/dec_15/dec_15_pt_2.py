#!/usr/bin/env python3
"""aoc21 day 15 pt 2"""

import aocd
import heapq
import itertools
import numpy as np


def find_neighbours(coords: tuple, value_map: np.array):
    neighbours = [(coords[0]-1, coords[1]), (coords[0]+1, coords[1]), (coords[0], coords[1]-1), (coords[0], coords[1]+1)]
    return {n for n in neighbours if not np.isnan(value_map[n[0]][n[1]])}


def dijkstra(padded_map, start, end):
    nodes = [(i, j) for i in range(1, padded_map.shape[0]-1) for j in range(1, padded_map.shape[1]-1)]
    distances = {n: float('inf') for n in nodes}
    priors = {n: None for n in nodes}
    distances[start] = 0
    node_heap = []
    entry_finder = {}
    counter = itertools.count()
    for n in nodes:
        add_node_to_heap(node_heap, n, counter, entry_finder, priority=distances[n])
    while end in entry_finder:
        closest = pop_node_from_heap(node_heap, entry_finder)
        for neighbour in find_neighbours(closest, padded_map):
            if neighbour in entry_finder:
                update_distance(closest, neighbour, distances, priors, padded_map, node_heap, counter, entry_finder)
    return distances[end]


def add_node_to_heap(my_heap, node, counter, entry_finder, priority=0):
    if node in entry_finder:
        remove_node_from_heap(node, entry_finder)
    count = next(counter)
    entry = [priority, count, node]
    entry_finder[node] = entry
    heapq.heappush(my_heap, entry)


def remove_node_from_heap(node, entry_finder):
    entry = entry_finder.pop(node)
    entry[-1] = (None, None)


def pop_node_from_heap(my_heap, entry_finder):
    while my_heap:
        priority, count, node = heapq.heappop(my_heap)
        if node != (None, None):
            del entry_finder[node]
            return node
    raise KeyError("cannot pop from an empty priority queue")


def update_distance(closest, neighbour, distances, priors, padded_map, node_heap, counter, entry_finder):
    alternative = distances[closest] + padded_map[neighbour[0]][neighbour[1]]
    if alternative < distances[neighbour]:
        distances[neighbour] = alternative
        priors[neighbour] = closest
        remove_node_from_heap(neighbour, entry_finder)
        add_node_to_heap(node_heap, neighbour, counter, entry_finder, alternative)


def construct_map(risk_map):
    horizontal_extension = np.hstack(list(risk_map + i for i in range(5)))
    vertical_extension = np.vstack(list(horizontal_extension + i for i in range(5)))
    return np.where(vertical_extension > 9, vertical_extension % 9, vertical_extension)


def main(data):
    risk_data = [[float(c) for c in l] for l in data.split("\n")]
    risk_map = np.array(risk_data, dtype=float)
    large_map = construct_map(risk_map)
    padded_map = np.pad(large_map, 1, 'constant', constant_values=np.nan)
    endpoint = (padded_map.shape[0]-2, padded_map.shape[1]-2)
    return dijkstra(padded_map, (1, 1), endpoint)


if __name__ == "__main__":
    with open("test_input.txt") as f:
        result = main(f.read())
    print(result)
    assert result == 315, f"result not as expected: {result}"
    print(main(aocd.get_data(day=15, year=2021)))
