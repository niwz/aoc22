from typing import Tuple


def get_compartments(rucksack: str) -> Tuple[str, str]:
    mid = len(rucksack) // 2
    return (rucksack[:mid], rucksack[mid:])

def find_duplicate(left: str, right: str) -> str:
    intersection = set(left).intersection(set(right))
    assert len(intersection) == 1
    return list(intersection)[0]

def get_priority(char: str) -> int:
    if char.islower():
        return 1 + ord(char) - ord('a')
    return 27 + ord(char) - ord('A')

if __name__ == '__main__':
    with open('./input.txt', 'r') as f:
        rucksacks = f.readlines()
        priority_sum = 0
        for rucksack in rucksacks:
            rucksack = rucksack.strip()
            l, r = get_compartments(rucksack)
            duplicate = find_duplicate(l, r)
            priority_sum += get_priority(duplicate)
        print(priority_sum)