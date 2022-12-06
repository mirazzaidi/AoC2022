from utils.utils import get_lines_from_file

DEBUG = 0

if DEBUG:
    lines = get_lines_from_file('day-4/test_input.txt')
else:
    lines = get_lines_from_file('day-4/input.txt')
count = 0

from dataclasses import dataclass


@dataclass
class Range:
    start: int
    end: int

    def __str__(self) -> str:
        return f'{self.start}-{self.end}'

    def overlaps_with(self, other):
        return other.start <= self.start <= other.end or other.start <= self.end <= other.end


for line in lines:
    first_assignment, second_assignment = line.split(',')
    section_a, section_b = first_assignment.split('-')
    range1 = Range(int(section_a), int(section_b))

    section_c, section_d = second_assignment.split('-')
    range2 = Range(int(section_c), int(section_d))

    if range1.overlaps_with(range2) or range2.overlaps_with(range1):
        count += 1
print(count)
