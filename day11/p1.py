from __future__ import annotations

from collections import deque
from typing import List, Deque
from dataclasses import dataclass, field
from utils.utils import get_lines_from_file

DEBUG = 0

lines = []

if DEBUG:
    lines = get_lines_from_file('day11/test_input.txt')
else:
    lines = get_lines_from_file('day11/input.txt')


@dataclass
class Monkey:
    operator: str
    operand: str
    test_divisible_by: int
    index_if_true: int
    index_if_false: int
    inspections: int = 0
    worry_levels: Deque[int] = field(default_factory=Deque)

    def test(self, worry_level):
        self.inspections += 1
        if self.operator == '+':
            return worry_level + int(self.operand) if self.operand != 'old' else worry_level + worry_level
        elif self.operator == '*':
            return worry_level * int(self.operand) if self.operand != 'old' else worry_level * worry_level

    def throws_at_index(self, worry):
        i, j = self.index_if_true, self.index_if_false
        return i if worry % self.test_divisible_by == 0 else j

    @staticmethod
    def from_lines(lines) -> Monkey:
        worry_levels = deque([int(i) for i in (lines[1].split(': ')[1]).split(', ')])
        operation = lines[2].split('= ')[1]
        _, operator, operand = operation.split()
        divisible_by = int(lines[3].split(' ')[-1])
        index_if_true = int(lines[4].split(' ')[-1])
        index_if_false = int(lines[5].split(' ')[-1])

        return Monkey(
            worry_levels=worry_levels,
            operand=operand,
            operator=operator,
            test_divisible_by=divisible_by,
            index_if_true=index_if_true,
            index_if_false=index_if_false,
        )


def get_monkeys_from_input_lines(lines):
    monkeys: List[Monkey] = []
    for line_index in range(0, len(lines), 7):
        current_monkey = lines[line_index : line_index + 7]
        monkey = Monkey.from_lines(current_monkey)
        monkeys.append(monkey)
    return monkeys


def run_simulation_for_rounds(rounds=20):
    monkeys: List[Monkey] = get_monkeys_from_input_lines(lines)

    for round in range(rounds):
        for monkey in monkeys:
            length_of_items = len(monkey.worry_levels)
            for _ in range(length_of_items):
                item_worry_level = monkey.worry_levels.popleft()
                worry = monkey.test(item_worry_level) // 3
                throws_at_index = monkey.throws_at_index(worry)
                monkeys[throws_at_index].worry_levels.append(worry)

    monkeys.sort(key=lambda x: x.inspections, reverse=True)
    print(monkeys[0].inspections * monkeys[1].inspections)


run_simulation_for_rounds()
