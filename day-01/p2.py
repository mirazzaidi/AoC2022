from utils.utils import get_lines_from_file


def get_top_3_calories(input_file):
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
    calories_count.sort(reverse=True)

    return sum(calories_count[:3])


if __name__ == '__main__':
    ans = get_top_3_calories('day-01/input.txt')
    print(f'Answer is {ans}')
