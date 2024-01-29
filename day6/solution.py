import math
from pathlib import Path


def readFile(inputPath: str):
    (time, distance) = list(filter(None, Path(inputPath).read_text().splitlines()))
    return (time, distance)


def zip_input():
    separated_str_list = list(map(lambda x: x.split(), readFile("day6/in.txt")))
    return list(
        map(
            (lambda x, y: (int(x), int(y))),
            separated_str_list[0][1:],
            separated_str_list[1][1:],
        )
    )


def merge_input_into_single_tuple_part2():
    separated_str_list = list(map(lambda x: x.split(), readFile("day6/in.txt")))
    res = [arr[1:] for arr in separated_str_list]
    return [tuple(map(lambda elem: int("".join(elem)), res))]


def solution_part1(time_distance_tuples: list[tuple[int, int]]):
    number_of_wins = []

    for time, distance in time_distance_tuples:
        upper_bound = (time + math.sqrt(pow(time, 2) - 4 * distance)) / 2
        lower_bound = (time - math.sqrt(pow(time, 2) - 4 * distance)) / 2
        if int(upper_bound) == upper_bound:
            upper_bound -= 1  # go down as it's a solution matching the exact distance
        if int(lower_bound) == lower_bound:
            lower_bound += 1  # go up as it's a solution matching the exact distance

        # solutions less than upper bound and greater than the lower (under the curve of the graph between the root points on the x axis)
        res = math.floor(upper_bound) - math.ceil(lower_bound) + 1
        number_of_wins.append(res)

    return math.prod(number_of_wins)


print(solution_part1(zip_input()))
print(solution_part1(merge_input_into_single_tuple_part2()))

# 3316275
# 27102791
