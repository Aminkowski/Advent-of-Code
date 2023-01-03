# define classes for the pointers, move, touching
class pointer:
    def __init__(self, horizontal, vertical, partner):
        self.x = horizontal
        self.y = vertical
        self.p = partner

    def touching(self):
        dx = abs(self.x - self.p.x)
        dy = abs(self.y - self.p.y)
        if dx < 2 and dy < 2:
            return True
        else:
            return False

    def move(self, direction):
        pass


som = open("demo9.txt")
motions = []
for line in som:
    motions.append([])
    lie = line.strip()
    temp = lie.partition(" ")
    motions[-1].append(temp[0])
    motions[-1].append(int(temp[2]))
print(motions)
size = {"U": 0, "D": 0, "L": 0, "R": 0}
vertical = 0
horizontal = 0
for pair in motions:
    if pair[0] == "U":
        vertical += pair[1]
    elif pair[0] == "D":
        vertical -= pair[1]
    elif pair[0] == "R":
        horizontal += pair[1]
    else:
        horizontal -= pair[1]
    if vertical > 0:
        size["U"] = max(vertical, size["U"])
    else:
        size["D"] = max(-1 * vertical, size["D"])
    if horizontal > 0:
        size["R"] = max(horizontal, size["R"])
    else:
        size["L"] = max(-1 * horizontal, size["L"])
print(size)
# do I make the grid by dictionary or list? can make both equiv.
# if list then I make it with for i in len(U + 1 + D + 1 - 1)
# and similar for horizontal direction
# then set th starting point at 
