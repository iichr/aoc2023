from functools import reduce
from pathlib import Path


def readFile(inputPath: str):
    return Path(inputPath).read_text().split()


def extract_first_last_digit(item):
    only_digits = [x for x in item if str.isdigit(x)]
    if len(only_digits) == 1:
        only_digits = only_digits + only_digits
    if len(only_digits) > 2:
        only_digits = [only_digits[0], only_digits[-1]]
    return (only_digits[0], only_digits[-1])


def solution_part1(tokens: list[str]):
    digits = []

    for item in tokens:
        first_digit, last_digit = extract_first_last_digit(item)
        digits.append(int(first_digit + last_digit))

    return print(sum(digits))


def solution_part2(tokens: list[str]):
    spelt_number_replacements = {
        "one": "o1e",
        "two": "t2o",
        "three": "t3e",
        "four": "f4r",
        "five": "f5e",
        "six": "s6x",
        "seven": "s7n",
        "eight": "e8t",
        "nine": "n9e",
    }

    digits = []

    for item in tokens:
        item_with_substitued_numbers = ""

        if any(x in item for x in spelt_number_replacements):
            item_with_substitued_numbers = reduce(
                lambda acc, kv: acc.replace(*kv),
                spelt_number_replacements.items(),
                item,
            )

        first_digit, last_digit = extract_first_last_digit(
            item_with_substitued_numbers or item
        )
        digits.append(int(first_digit + last_digit))

    return print(sum(digits))


solution_part1(readFile("day1/in.txt"))
solution_part2(readFile("day1/in.txt"))
