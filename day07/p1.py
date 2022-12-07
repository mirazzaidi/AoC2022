from collections import deque

from day07.classes import Directory
from day07.common import create_filesystem
from utils.utils import get_lines_from_file

DEBUG = 0

if DEBUG:
    lines = get_lines_from_file('day07/test_input.txt')
else:
    lines = get_lines_from_file('day07/input.txt')

root = create_filesystem(lines)

ans = 0

q = deque()
q.append(root)

while q:
    current_node = q.pop()
    current_node_size = current_node.total_size()
    if current_node_size <= 100000:
        ans += current_node_size
    for child in current_node.children:
        if isinstance(child, Directory):
            q.append(child)

print(ans)
