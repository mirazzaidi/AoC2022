from utils.utils import get_lines_from_file

DEBUG = 0

if DEBUG:
    lines = get_lines_from_file('day-04/test_input.txt')
else:
    lines = get_lines_from_file('day-04/input.txt')
count = 0

from dataclasses import dataclass


@dataclass
class Range:
    start: int
    end: int

    def __str__(self) -> str:
        return f'{self.start}-{self.end}'

    def is_fully_overlapped_by(self, other):
        return other.start <= self.start <= self.end <= other.end


for line in lines:
    first_assignment, second_assignment = line.split(',')
    section_a, section_b = first_assignment.split('-')
    range1 = Range(int(section_a), int(section_b))

    section_c, section_d = second_assignment.split('-')
    range2 = Range(int(section_c), int(section_d))

    if range1.is_fully_overlapped_by(range2) or range2.is_fully_overlapped_by(range1):
        count += 1
print(count)
