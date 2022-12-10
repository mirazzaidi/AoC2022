from utils.utils import get_lines_from_file

DEBUG = 0

lines = []

if DEBUG:
    lines = get_lines_from_file('day10/test_input.txt')
else:
    lines = get_lines_from_file('day10/input.txt')

cycle = 0
X = 1
cycle_strength = []


def run_cycle(cycle, cycle_strength):
    if cycle in (20, 60, 100, 140, 180, 220):
        cycle_strength.append(cycle * X)


for line in lines:
    command = line.split()

    if command[0] == 'noop':
        cycle += 1
        run_cycle(cycle, cycle_strength)
    else:
        for _ in range(2):
            cycle += 1
            run_cycle(cycle, cycle_strength)
        X += int(command[1])

print(sum(cycle_strength))
