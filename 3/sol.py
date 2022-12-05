from typing import List, Set, Tuple


def get_compartments(rucksack: str) -> Tuple[str, str]:
    half_length = len(rucksack) // 2
    return rucksack[:half_length], rucksack[half_length:]


def get_common_item_types(rucksack: str) -> Set[str]:
    first_compartment, second_compartment = get_compartments(rucksack)
    return set(first_compartment) & set(second_compartment)


def get_item_type_priority(item_type: str) -> int:
    if item_type.islower():
        return ord(item_type) - ord('a') + 1
    elif item_type.isupper():
        return ord(item_type) - ord('A') + 27


def calculate_common_item_type_priorities_sum(rucksacks: List[str]) -> int:
    common_item_type_priorities_sum = 0
    for rucksack in rucksacks:
        common_item_types = get_common_item_types(rucksack)
        for item_type in common_item_types:
            common_item_type_priorities_sum += get_item_type_priority(item_type)
    return common_item_type_priorities_sum


if __name__ == '__main__':
    with open('input.txt') as f:
        rucksacks = f.read().strip().split('\n')
    print(calculate_common_item_type_priorities_sum(rucksacks))