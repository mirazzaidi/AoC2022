from utils.utils import get_lines_from_file


def get_max_calories(input_file):
    lines = get_lines_from_file(input_file)
    calories_count = []
    calories = 0
    for line in lines:
        if line == '':
            calories_count.append(calories)
            calories = 0
        else:
            calories += int(line)
    calories_count.append(calories)
    return max(calories_count)


if __name__ == '__main__':
    ans = get_max_calories('day-1/input.txt')
    print(f'Answer is {ans}')
