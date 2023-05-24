import numpy as np
import re

class Grid:
    def __init__(self, width, height):
        self.map = [[0 for _ in range(x0+width)] for _ in range(height)]

class Sand:
    def __init__(self, hor, ver):
        self.x = hor
        self.y = ver

    def Rest(self, grid):
        if grid[self.x]:  # the x and y may be flipped
            pass

    def Fall(self):
        pass

# 450 to 550 on the x, 10 to 170 on the y
width, height = 100, 200
x0 = 450
grid = Grid(width - x0, height)

for i in range(width):
    for j in range(height):
        pass


with open("demo14.txt", "r") as file:  
    for line in file:
        pass
