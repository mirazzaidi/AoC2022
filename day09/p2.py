from dataclasses import dataclass
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
        return abs(self.x - other.x) <= 1 and abs(self.y - other.y) <= 1

    def go_right(self):
        self.x += 1

    def go_left(self):
        self.x -= 1

    def go_up(self):
        self.y += 1

    def go_down(self):
        self.y -= 1


head = Pos(0, 0)
tails = [Pos(0, 0) for _ in range(9)]
tails.append(head)

tail_path = set()
tail_path.add((0, 0))

for line in lines:
    dir, steps = line.split()
    steps = int(steps)

    for _ in range(steps):
        prev_x = head.x
        prev_y = head.y

        if dir == 'R':
            head.go_right()
        elif dir == 'U':
            head.go_up()
        elif dir == 'L':
            head.go_left()
        elif dir == 'D':
            head.go_down()

        for i in range(len(tails) - 2, -1, -1):
            current_head = tails[i + 1]
            current_tail = tails[i]

            if not current_head.is_touching(current_tail) and (current_tail.x == current_head.x or current_tail.y == current_head.y):
                if dir == 'R':
                    current_tail.go_right()

                elif dir == 'L':
                    current_tail.go_left()

                elif dir == 'U':
                    current_tail.go_up()

                elif dir == 'D':
                    current_tail.go_down()

            if not current_head.is_touching(current_tail) and not (current_tail.x == current_head.x or current_tail.y == current_head.y):

                prev_x, prev_y = current_tail.x, current_tail.y

                current_tail.go_right() if current_head.x - prev_x > 0 else current_tail.go_left()
                current_tail.go_up() if current_head.y - prev_y > 0 else current_tail.go_down()

        tail_path.add((tails[0].x, tails[0].y))

print(len(tail_path))
