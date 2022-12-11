from collections import deque
from typing import List, Deque
from dataclasses import dataclass, field
from utils.utils import get_lines_from_file
from day11.p1 import get_monkeys_from_input_lines, Monkey

DEBUG = 0

lines = []

if DEBUG:
    lines = get_lines_from_file('day11/test_input.txt')
else:
    lines = get_lines_from_file('day11/input.txt')


def run_simulation_for_rounds(rounds=10000):
    monkeys: List[Monkey] = get_monkeys_from_input_lines(lines)

    lcm = 1
    for monkey in monkeys:
        lcm = lcm * monkey.test_divisible_by

    for round in range(rounds):
        for monkey in monkeys:
            while monkey.worry_levels:
                item = monkey.worry_levels.popleft()
                worry = monkey.test(item) % lcm
                throws_at_index = monkey.throws_at_index(worry)
                monkeys[throws_at_index].worry_levels.append(worry)
    monkeys.sort(key=lambda x: x.inspections, reverse=True)

    print(monkeys[0].inspections * monkeys[1].inspections)


run_simulation_for_rounds()
