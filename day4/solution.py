from pathlib import Path
import re


def readFile(inputPath: str):
    return Path(inputPath).read_text().split("\n")


test = "Card   1: 75 68 35 36 86 83 30 11 14 59 | 86 25 63 57 59 91 68 14 72 32 36 74 66 44 30 28 11 35 75 34 55 83 69 56 38"
test2 = "Card  85:  1  9 56  7 47  5 30 17 81 36 | 61 83 58 97 10 24  8 94 46 75 52 42 28 25 86 66 82 73 87 23 29 15 26 54 31"


def parse_line(line: str):
    # Card 123:
    [winning, current] = re.sub(r"Card\s*\d*:", "", line).split("|")
    winning_numbers = set([int(x) for x in winning.strip().split()])
    current_numbers = set([int(x) for x in current.strip().split()])

    # set intersection
    return len(winning_numbers & current_numbers)


def solution_part1():
    matching_cards = list()
    file = readFile("day4/in.txt")

    for line in file:
        matching_cards.append(parse_line(line))

    return sum([2 ** int(i - 1) if i > 0 else 0 for i in matching_cards])


def solution_part2():
    matching_cards = list()
    file = readFile("day4/in.txt")

    for line in file:
        matching_cards.append((parse_line(line), 1))

    for index, (card, count) in enumerate(matching_cards):
        while card > 0 and index + 1 < len(matching_cards):
            modify_card_number_count(matching_cards, index + 1, count)
            index += 1
            card -= 1

    return sum(i for _, i in matching_cards)


def modify_card_number_count(cards: list(), index: int, original_count: int):
    """
    increment the count of the card with a given index n times
    """
    (card, count) = cards[index]
    cards[index] = (card, count + original_count)


print(solution_part1())
print(solution_part2())
