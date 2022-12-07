from utils.utils import get_lines_from_file

DEBUG = 0

if DEBUG:
    rucksacks = get_lines_from_file('day03/test_input.txt')
else:
    rucksacks = get_lines_from_file('day03/input.txt')


missed_items = []

for rucksack in rucksacks:
    count = len(rucksack)
    half = count // 2
    first = rucksack[:half]
    second = rucksack[half:]
    common = set(first).intersection(set(second))
    char = common.pop()
    if char.islower():
        missed_items.append(ord(char) - ord('a') + 1)
    else:
        missed_items.append(ord(char) - ord('A') + 27)

print(sum(missed_items))
