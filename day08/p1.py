from utils.utils import get_lines_from_file

DEBUG = 0

grid = []

if DEBUG:
    grid = get_lines_from_file('day08/test_input.txt')
else:
    grid = get_lines_from_file('day08/input.txt')

rows = len(grid)
cols = len(grid[0])


def count_visible_trees(grid):
    visible_trees = 0

    for i in range(rows):
        for j in range(len(grid[i])):
            tree_height = int(grid[i][j])

            if i == 0 or j == 0 or i == rows - 1 or j == len(grid[i]) - 1:  # Edges
                visible_trees += 1
            else:
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

                if (tree_height > max(row_left)) or (tree_height > max(row_right)) or (tree_height > max(col_up)) or (tree_height > max(col_dn)):
                    visible_trees += 1
    return visible_trees


print(count_visible_trees(grid))
