from pathlib import Path


def readFile(inputPath: str):
    input = list(filter(None, Path(inputPath).read_text().splitlines()))
    return input


def solution_part1() -> int:
    num_history = readFile("day9/in.txt")
    sum_of_predictions = 0

    for sequence in num_history:
        split_seq = [int(x) for x in sequence.split()]
        sum_of_predictions += get_differences(split_seq)

    return sum_of_predictions


def solution_part2() -> int:
    num_history = readFile("day9/in.txt")
    sum_of_predictions = 0

    for sequence in num_history:
        split_seq = [int(x) for x in sequence.split()]
        # reverse difference array so we still take the last element (which is the first)
        sum_of_predictions += get_differences(split_seq[::-1])
        # 10  13  16  21  30  45 -> 45 30 21 16 13 10
        #  -15 -9 -5 -3 -3
        #  6 4 2 0
        #  -2 -2 -2
        #   0 0

    return sum_of_predictions


def get_differences(split_seq: list[int]) -> list[int]:
    diffs = [b - a for a, b in zip(split_seq, split_seq[1:])]
    return split_seq[-1] + get_differences(diffs) if split_seq else 0


print(solution_part1())
print(solution_part2())

# 1953784198
# 957
