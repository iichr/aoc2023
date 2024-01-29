import collections
from pathlib import Path


def readFile(inputPath: str):
    input = list(filter(None, Path(inputPath).read_text().splitlines()))
    return input


# default dict is ordered by insertion order
def countchars_defaultdict(chars):
    d = collections.defaultdict(int)
    for ch in chars:
        d[ch] += 1
    return dict(d)


def get_hand_type(freq_list: list[tuple[str, int]]):
    list_len = len(freq_list)
    most_freq_card_count = freq_list[0][1]
    if list_len == 1:
        return 7
    if most_freq_card_count == 4:
        return 6
    if list_len == 2:
        # can only be full house after 5 and 4 are exhausted
        return 5
    if list_len == 5:
        # can only be High
        return 1
    if most_freq_card_count == 3:
        # can only be 3 of a kind (3 total card kinds)
        return 4
    if most_freq_card_count == 2 and list_len == 3:
        # can only be 2 pair
        return 3
    if list_len == 4:
        # 2 same, 3 other different categories = 4 in total
        return 2
    else:
        # 5 different
        return 1


def solution_part1(string_input: list[str]):
    cards_by_strength_desc = ["A", "K", "Q", "J", "T"]
    cards_by_strength_desc.extend([str(x) for x in list(range(9, 1, -1))])
    sort_order = {k: i for i, k in enumerate(cards_by_strength_desc)}

    cards_with_type_and_value = []
    for line in string_input:
        (hand, val) = line.split()
        hand_card_freq = countchars_defaultdict(hand)
        sorted_hand_card_freq = sorted(
            hand_card_freq.items(), key=lambda kv: kv[1], reverse=True
        )
        hand_type = get_hand_type(sorted_hand_card_freq)
        cards_with_type_and_value.append((hand, hand_type, int(val)))

    # reverse order of alphabetical sort, smallest should come first - use negative sign
    sorted_cards_by_type = sorted(
        cards_with_type_and_value,
        key=lambda entry: (entry[1], [-sort_order.get(c) for c in entry[0]]),
    )

    total_sum = 0
    for index, item in enumerate(sorted_cards_by_type):
        total_sum += (index + 1) * item[2]

    return total_sum


def solution_part2(string_input: list[str]):
    cards_by_strength_desc = ["A", "K", "Q", "J", "T"]
    cards_by_strength_desc.extend([str(x) for x in list(range(9, 1, -1))])
    sort_order = {k: i for i, k in enumerate(cards_by_strength_desc)}

    cards_with_type_and_value = []
    for line in string_input:
        (hand, val) = line.split()
        hand_card_freq = countchars_defaultdict(hand)

        sorted_hand_card_freq = sorted(
            hand_card_freq.items(), key=lambda kv: kv[1], reverse=True
        )

        if "J" in hand and not "JJJJJ" in hand:
            [(J_index, J_count)] = list(
                (index, j[1])
                for index, j in enumerate(sorted_hand_card_freq)
                if j[0] == "J"
            )

            # print("BEFORE", sorted_hand_card_freq, J_index, J_count)

            del sorted_hand_card_freq[J_index]
            sorted_hand_card_freq[0] = (
                sorted_hand_card_freq[0][0],
                sorted_hand_card_freq[0][1] + J_count,
            )
            # print("AFTER", sorted_hand_card_freq, J_index, J_count)

        # print(sorted_hand_card_freq)
        hand_type = get_hand_type(sorted_hand_card_freq)
        cards_with_type_and_value.append((hand, hand_type, int(val)))

    # reverse order of alphabetical sort, smallest should come first - use negative sign
    sorted_cards_by_type = sorted(
        cards_with_type_and_value,
        key=lambda entry: (entry[1], [-sort_order.get(c) for c in entry[0]]),
    )

    total_sum = 0
    for index, item in enumerate(sorted_cards_by_type):
        total_sum = total_sum + ((index + 1) * item[2])

    return total_sum


print(solution_part1(readFile("day7/in.txt")))
print(solution_part2(readFile("day7/in.txt")))

# 255048101
# 253718286
