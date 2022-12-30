# trees in grids, treehouse: hidden -> #treesvisible from outside the grid
# looking along row or column, input of heights of trees
# each digit a tree's height, visible if E a line to edge st
# all trees shorter than it in that  line. line = 4 ontho dirs
# how many trees in grid visible?

def up(grid, i, j):
    tall = grid[i][j]
    row = i
    visible = False
    while (not visible):
        if row == 0:
            visible = True
        elif tall > grid[row - 1][j]:
            row -= 1
        else:
            row -= 1
            break
    return i - row  # visible


def down(grid, i, j):
    tall = grid[i][j]
    row = i
    visible = False
    while (not visible):
        if row == (len(grid) - 1):
            visible = True
        elif tall > grid[row + 1][j]:
            row += 1
        else:
            row += 1
            break
    return row - i  # visible


def left(grid, i, j):
    tall = grid[i][j]
    col = j
    visible = False
    while (not visible):
        if col == 0:
            visible = True
        elif tall > grid[i][col - 1]:
            col -= 1
        else:
            col -= 1
            break
    return j - col  # visible


def right(grid, i, j):
    tall = grid[i][j]
    col = j
    visible = False
    while (not visible):
        if col == (len(grid[i]) - 1):
            visible = True
        elif tall > grid[i][col + 1]:
            col += 1
        else:
            col += 1
            break
    return col - j  # visible


trees = open("input8.txt")
grid = []
for line in trees:
    grid.append([])
    row = line.strip()
    for col in row:
        grid[-1].append(int(col))
# print(grid)
height = len(grid)
width = len(grid[0])
visible = []
for i in range(height):
    visible.append([])
    for j in range(width):
        vis = up(grid, i, j) * down(grid, i, j)  # or down(grid, i, j)
        ible = left(grid, i, j) * right(grid, i, j)  # or right(grid, i, j)
        visible[-1].append(vis * ible)
print(visible)
counter = 0
for i in visible:
    for j in i:
        counter = max(counter, j)
        # if j:
        # counter += 1
print(counter)
