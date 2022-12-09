# Parse the input to create a grid of trees
from utils.utils import get_lines_from_file


grid = []
DEBUG = 0
if DEBUG:
    grid = get_lines_from_file('day08/test_input.txt')
else:
    grid = get_lines_from_file('day08/input.txt')

rows = len(grid)
cols = len(grid[0])


def get_max_scenic_score(grid):
    max_scenic_score = 0

    for i in range(rows):
        for j in range(len(grid[i])):
            tree_height = int(grid[i][j])

            if not (i == 0 or j == 0 or i == rows - 1 or j == len(grid[i]) - 1):  # Not Edge
                row_left = []
                row_right = []

                for col_itr in range(0, cols):
                    row_itr = i
                    if col_itr < j:
                        row_left.append(int(grid[row_itr][col_itr]))
                    elif col_itr > j:
                        row_right.append(int(grid[row_itr][col_itr]))

                col_up = []
                col_dn = []

                for row_itr in range(0, rows):
                    col_itr = j
                    if row_itr < i:
                        col_up.append(int(grid[row_itr][col_itr]))
                    elif row_itr > i:
                        col_dn.append(int(grid[row_itr][col_itr]))

                left_trees = 0
                right_trees = 0

                for col_itr in range(len(row_left) - 1, -1, -1):
                    left_trees += 1
                    if row_left[col_itr] >= tree_height:
                        break
                for col_itr in range(len(row_right)):
                    right_trees += 1
                    if row_right[col_itr] >= tree_height:
                        break

                up_trees = 0
                dn_trees = 0

                for row_itr in range(len(col_up) - 1, -1, -1):
                    up_trees += 1
                    if col_up[row_itr] >= tree_height:
                        break
                for row_itr in range(len(col_dn)):
                    dn_trees += 1
                    if col_dn[row_itr] >= tree_height:
                        break

                scenic_score = left_trees * right_trees * up_trees * dn_trees

                max_scenic_score = max(scenic_score, max_scenic_score)

    return max_scenic_score


print(get_max_scenic_score(grid))
