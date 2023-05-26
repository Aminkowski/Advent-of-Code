import re
import ast
import matplotlib.pyplot as plt
import numpy as np

class Grid:
    def __init__(self, width, height):
        self.map = [[0 for _ in range(width)] for _ in range(height)]  # _.map[y][x]

    def scan(self):
        fig, ax = plt.subplots()
        ax.imshow(np.array(self.map), cmap='gray')
        plt.show()

    def rocks(self, p1, p2):  # could have bug related to p1 = p2
        orth = p1[0] == p2[0]  # gives which orthogonal we should move about. if True = 1 then we need to move about y (the second aka 1 index)
        unit = 1 if p1[orth] < p2[orth] else -1
        if orth:
            for i in range(p1[orth], p2[orth] + unit, unit):  # could have also just done from min to max since order doesn't matter
                self.map[i][p1[not orth]] = 2
        else:
            for i in range(p1[orth], p2[orth] + unit, unit):  # could have also just done from min to max since order doesn't matter
                self.map[p1[not orth]][i] = 2

    def floor(self, depth):  # because for whatever reason grid.rocks((-1*depth, depth), (depth, depth)) just leaves the center blank even though the pointer moves through the appropriate indices
        for i in range(len(self.map[depth])):
            self.map[depth][i] = 2

    def sand(self):
        originx, originy = 250, 0
        if True:
            while True:
                if self.map[originy + 1][originx] == 0:
                    originy += 1 
                elif self.map[originy + 1][originx - 1] == 0:
                    originy += 1 
                    originx -= 1
                elif self.map[originy + 1][originx + 1] == 0:
                    originy += 1 
                    originx += 1
                elif originy == 0:
                    self.map[originy][originx] = 1
                    return False
                else:
                    self.map[originy][originx] = 1
                    break
            return True
        else:
            try:
                while True:
                    if self.map[originy + 1][originx] == 0:
                        originy += 1 
                    elif self.map[originy + 1][originx - 1] == 0:
                        originy += 1 
                        originx -= 1
                    elif self.map[originy + 1][originx + 1] == 0:
                        originy += 1 
                        originx += 1
                    else:
                        self.map[originy][originx] = 1
                        break
                #print(f'(x, y) = {(originx, originy)} has been filled') # tentative
                return True
            except IndexError:
                print(f'sand flowing into the abyss')  # tentative
                return False

    def sand_count(self):
        counter = 0
        for row in self.map:
            for x in row:
                if x == 1:
                    counter += 1
        return counter



# 450 to 550 on the x, 10 to 170 on the y
width, height = 500, 200
x0 = 250  # normally 450
grid = Grid(width, height)
regex = r"\d{3},\d{1,3}"

with open("input14.txt", "r") as file:  
    depth = 0
    for line in file:
        curve = re.findall(regex, line)
        for i in range(len(curve)-1):
            p11, p12 = ast.literal_eval(curve[i])
            p21, p22 = ast.literal_eval(curve[i+1])
            depth = max(depth, p12, p22)
            print(f'i = {i}, {(p11, p12)} to {(p21, p22)}, where the (0,0) of the diagram is ({x0}, 0)')
            grid.rocks((p11 - x0, p12), (p21 - x0, p22))
    print(depth)
    depth += 2
    grid.floor(depth)

grid.scan()
if False:
    for j in range(10):
        for i in range(3000):
            if grid.sand():
                continue
            else:
                print("uh-oh")
                break
        #grid.scan()
else:
    while grid.sand():
        continue
grid.scan()
print(grid.sand_count())
