from __future__ import annotations

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

total_size = 70000000
free_space_needed = 30000000
current_space = root.total_size()
space_to_delete = free_space_needed - (total_size - current_space)
ans = 0

q = deque()
q.append(root)
dirs = []

while q:
    current_node = q.pop()
    current_node_size = current_node.total_size()
    if current_node_size >= space_to_delete:
        dirs.append(current_node)

    for child in current_node.children:
        if isinstance(child, Directory):
            q.append(child)

dirs.sort(key=lambda x: x.total_size())

print(dirs[0].total_size())
