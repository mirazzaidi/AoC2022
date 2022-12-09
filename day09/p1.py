from dataclasses import dataclass
from collections import deque

from day07.classes import Directory
from day07.common import create_filesystem
from utils.utils import get_lines_from_file

DEBUG = 0

if DEBUG:
    lines = get_lines_from_file('day09/test_input.txt')
else:
    lines = get_lines_from_file('day09/input.txt')


@dataclass
class Pos:
    x: int
    y: int

    def is_touching(self, other):
        if abs(self.x - other.x) <= 1 and abs(self.y - other.y) <= 1:
            return True
        else:
            return False


head = Pos(0, 0)
tail = Pos(0, 0)

tail_path = set()
tail_path.add((0, 0))
for line in lines:
    dir, steps = line.split()
    steps = int(steps)

    for _ in range(steps):
        last_x = head.x
        last_y = head.y

        if dir == 'R':
            head.x += 1
        elif dir == 'U':
            head.y += 1
        elif dir == 'L':
            head.x -= 1
        elif dir == 'D':
            head.y -= 1

        if not head.is_touching(tail) and (tail.x == head.x or tail.y == head.y):
            if dir == 'R':
                tail.x += 1
            elif dir == 'U':
                tail.y += 1
            elif dir == 'L':
                tail.x -= 1
            elif dir == 'D':
                tail.y -= 1
        if not head.is_touching(tail) and not (tail.x == head.x or tail.y == head.y):
            tail.x = last_x
            tail.y = last_y
        tail_path.add((tail.x, tail.y))
print(len(tail_path))
