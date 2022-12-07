from collections import deque


DEBUG = 0


def get_lines_from_file(filename: str):
    lines = []
    with open(filename) as f:
        lines = f.readlines()
        lines = [line[0 : len(line) - 1] if line[-1] == '\n' else line for line in lines]
    return lines


def read_lines():
    if DEBUG:
        lines = get_lines_from_file('day05/test_input.txt')
    else:
        lines = get_lines_from_file('day05/input.txt')
    return lines


def make_stacks(lines):
    stack_count = (len(lines[0]) + 1) // 4
    stacks = [deque() for i in range(stack_count)]

    for line in lines:
        if line.startswith(' 1'):
            break
        line += ' '  # an extra space at the end to make it 4 char per stack item.
        stack_index = 0

        for i in range(0, len(line), 4):
            stack_name = line[i + 1]
            if stack_name != ' ':
                stacks[stack_index].appendleft(stack_name)
            stack_index += 1
    return stacks


def get_max_stack_height(stacks):
    max_height = 0
    for stack in stacks:
        max_height = max(max_height, len(stack))
    return max_height


def get_instructions(lines, stacks):
    max_height = get_max_stack_height(stacks)
    instructions = lines[max_height + 2 :]
    return instructions


def move_stacks_by_instructions(instructions, stacks):

    for instruction in instructions:

        tokens = instruction.split()

        count_items_to_move = int(tokens[1])
        move_from = int(tokens[3]) - 1  # zero based index
        move_to = int(tokens[5]) - 1  # zero based index
        temp = deque()
        for _ in range(count_items_to_move):
            item = stacks[move_from].pop()
            temp.append(item)
        while temp:
            stacks[move_to].append(temp.pop())


def get_top_items(stacks):
    ans = ''
    for s in stacks:
        ans += s[-1][0]
    return ans


if __name__ == "__main__":
    lines = read_lines()
    stacks = make_stacks(lines)
    instructions = get_instructions(lines, stacks)
    move_stacks_by_instructions(instructions, stacks)
    print(get_top_items(stacks))
