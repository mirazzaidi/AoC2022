from utils.utils import get_lines_from_file

DEBUG = 0

if DEBUG:
    rucksacks = get_lines_from_file('day-3/test_input.txt')
else:
    rucksacks = get_lines_from_file('day-3/input.txt')

lines = len(rucksacks)
i = 0
priority = 0
for i in range(0, lines, 3):
    group_a, group_b, group_c = rucksacks[i], rucksacks[i + 1], rucksacks[i + 2]
    common = set(group_a).intersection(set(group_b)).intersection(set(group_c))
    char = common.pop()
    if char.islower():
        priority += ord(char) - ord('a') + 1
    else:
        priority += ord(char) - ord('A') + 27
    i += 3

print(priority)
