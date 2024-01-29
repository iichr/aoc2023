from pathlib import Path
import re


def readFile(inputPath: str):
    return Path(inputPath).read_text().split("\n")


red_threshold = 12
green_threshold = 13
blue_threshold = 14


def extract_game_id_and_rgb_values(line: str):
    regex_game_id = r"Game\s(\d{1,3})"
    regex_red = r"(\d{0,2})\sred"
    regex_green = r"(\d{0,2})\sgreen"
    regex_blue = r"(\d{0,2})\sblue"

    regexs = [regex_game_id, regex_red, regex_green, regex_blue]

    game_id, r, g, b = tuple(map(lambda regex: re.findall(regex, line), regexs))

    return game_id, r, g, b


def process_line_part1(line: str):
    game_id, r, g, b = extract_game_id_and_rgb_values(line)

    game_id_int = int(game_id[0])
    r_int = all([int(x) <= red_threshold for x in r])
    g_int = all([int(x) <= green_threshold for x in g])
    b_int = all([int(x) <= blue_threshold for x in b])

    if r_int & g_int & b_int:
        # print('success - game', game_id_int)
        return game_id_int
    else:
        return 0


def process_line_part2(line: str):
    game_id, r, g, b = extract_game_id_and_rgb_values(line)

    game_id_int = int(game_id[0])
    r_int = max([int(x) for x in r], default=0)
    g_int = max([int(x) for x in g], default=0)
    b_int = max([int(x) for x in b], default=0)

    # print('Game', game_id_int, 'max R', r_int, 'max G', g_int, 'max B', b_int)

    return r_int, g_int, b_int


def solution_part1():
    sum = 0
    file = readFile("day2/in.txt")
    for line in file:
        sum += process_line_part1(line)
    return sum


def solution_part2():
    sum = 0
    file = readFile("day2/in.txt")
    for line in file:
        r_max, g_max, b_max = process_line_part2(line)
        sum += r_max * g_max * b_max
    return sum


print(solution_part1())
print(solution_part2())
