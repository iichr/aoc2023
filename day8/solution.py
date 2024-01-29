import collections
from pathlib import Path


def readFile(inputPath: str):
    input = list(filter(None, Path(inputPath).read_text().splitlines()))
    return input


def solution_part1(directions: str, nodes: list[str]) -> int:
    [directions, *nodes] = readFile("day8/in.txt")
    node_dict = collections.defaultdict(list)
    for node_entry in nodes:
        [node, instr] = node_entry.split(" = ")
        [instr_left, instr_right] = instr.strip(" ()").split(", ")
        node_dict[node] = [instr_left, instr_right]

    current_location = "AAA"
    count = 0
    while current_location != "ZZZ":
        for direction in directions:
            if direction == "L":
                current_location = node_dict[current_location][0]
            if direction == "R":
                current_location = node_dict[current_location][1]
            count += 1
    return count


print(solution_part1(directions, nodes))
# 17873
