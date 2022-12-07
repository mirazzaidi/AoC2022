from collections import defaultdict

from utils.utils import get_lines_from_file

DEBUG = 0

if DEBUG:
    code = get_lines_from_file('day06/test_input.txt')[0]
else:
    code = get_lines_from_file('day06/input.txt')[0]

char_map = defaultdict(int)
sequence_len = 14

assert len(code) >= sequence_len

char_index = 0
while char_index < sequence_len:
    char_map[code[char_index]] += 1
    char_index += 1

while char_index < len(code):
    if len(char_map.keys()) == sequence_len:
        break
    else:
        char_map[code[char_index]] += 1
        char_map[code[char_index - sequence_len]] -= 1
        if char_map[code[char_index - sequence_len]] == 0:
            del char_map[code[char_index - sequence_len]]
    char_index += 1

if len(char_map.keys()) == sequence_len:
    print(char_index)
else:
    print('Not found')
