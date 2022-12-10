from utils.utils import get_lines_from_file

DEBUG = 0

lines = []

if DEBUG:
    lines = get_lines_from_file('day10/test_input.txt')
else:
    lines = get_lines_from_file('day10/input.txt')


def run_cycle(cycle, crt, sprite_pos, screen):
    if cycle % 40 == 0:
        screen.append(''.join(crt))
        crt = ['.'] * 40
    index = cycle % 40 - 1
    crt[index] = '#' if sprite_pos - 1 <= index <= sprite_pos + 1 else '.'


def get_screen():
    cycle = 0
    X = 1
    crt = ['.'] * 40
    screen = []
    sprite_pos = 1

    for line in lines:
        command = line.split()

        if command[0] == 'noop':
            cycle += 1
            run_cycle(cycle, crt, sprite_pos, screen)
        else:
            for _ in range(2):
                cycle += 1
                run_cycle(cycle, crt, sprite_pos, screen)
            X += int(command[1])
            sprite_pos = X
    return screen


screen = get_screen()
for row in screen:
    print(row)
