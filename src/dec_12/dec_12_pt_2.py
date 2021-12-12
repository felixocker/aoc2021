#!/usr/bin/env python3
"""aoc21 day 12 pt 2"""

from collections import Counter
import copy
from io import StringIO
import aocd


def find_inverted_edges(edges):
    inverted_edges = [[edge[1], edge[0]] for edge in edges]
    return inverted_edges


def build_path(edges, current_path, all_paths):
    occurrences = Counter(current_path)
    twice_allowed = all(v < 2 for k, v in occurrences.items() if k.islower())
    if current_path[-1] != "end":
        for edge in edges:
            if edge[0] == current_path[-1] and (edge[1].isupper() or edge[1].islower() and (twice_allowed or occurrences[edge[1]] < 1)):
                new_path = copy.copy(current_path)
                new_path.append(edge[1])
                if edge[1] == "end":
                    all_paths.append(new_path)
                else:
                    all_paths = build_path(edges, new_path, all_paths)
    return all_paths


def main(data):
    edges = [l.split("\n")[0].split("-") for l in data if l[:-1]]
    edges.extend(find_inverted_edges(edges))
    edges = [edge for edge in edges if not edge[1] == "start" and not edge[0] == "end"]
    current_path = ["start"]
    paths = build_path(edges, current_path, [])
    return len(paths)


if __name__ == "__main__":
    for t in ("test_input_1.txt", 36), ("test_input_2.txt", 103), ("test_input_3.txt", 3509):
        with open(t[0]) as f:
            result = main(f)
        assert result == t[1], f"result for {t[0]} not as expected: {result}"
    print(main(StringIO(aocd.get_data(day=12, year=2021))))
