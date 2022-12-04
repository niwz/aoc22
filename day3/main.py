from typing import Tuple

def get_compartments(rucksack: str) -> Tuple[str, str]:
    mid = len(rucksack) // 2
    return (rucksack[:mid], rucksack[mid:])

def find_duplicate(left: str, right: str) -> str:
    intersection = set(left).intersection(set(right))
    assert len(intersection) == 1
    return list(intersection)[0]

def get_item_priority(char: str) -> int:
    if char.islower():
        return 1 + ord(char) - ord('a')
    return 27 + ord(char) - ord('A')

if __name__ == '__main__':
    with open('./input.txt', 'r') as f:
        rucksacks = list(map(str.strip, f.readlines()))
        priority_sum = 0
        badge_priority_sum = 0
        for i in range(0, len(rucksacks), 3):
            rucksack_group = rucksacks[i: i+3]
            
            # Part 1
            for rucksack in rucksack_group:
                l, r = get_compartments(rucksack)
                duplicate = find_duplicate(l, r)
                priority_sum += get_item_priority(duplicate)

            # Part 2
            badge_set = set(rucksack_group[0]) & set(rucksack_group[1]) & set(rucksack_group[2])
            badge = list(badge_set)[0]
            badge_priority_sum += get_item_priority(badge)

        print(f"Priority Sum: {priority_sum}\nBadge Priority Sum: {badge_priority_sum}")