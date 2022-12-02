from typing import List


def get_lines_from_file(filename: str) -> List[str]:
    lines = []
    with open(filename) as f:
        lines = f.readlines()
        lines = [line.rstrip() for line in lines]
    return lines
