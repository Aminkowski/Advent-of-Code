
class Grid:
    def __init__(self):
        self.visited = set()

    def mark_visited(self, position):
        self.visited.add(position)

    def is_visited(self, position):
        return position in self.visited


class Knot:
    def __init__(self, position, leader=None):
        self.position = position
        self.leader = leader

    def move(self, direction):
        if direction == 'L':
            self.position = (self.position[0] - 1, self.position[1])
        elif direction == 'R':
            self.position = (self.position[0] + 1, self.position[1])
        elif direction == 'U':
            self.position = (self.position[0], self.position[1] + 1)
        elif direction == 'D':
            self.position = (self.position[0], self.position[1] - 1)

    def move_towards_leader(self):
        if self.leader is None:
            return

        leader_x, leader_y = self.leader.position
        knot_x, knot_y = self.position

        if abs(leader_x - knot_x) <= 1 and abs(leader_y - knot_y) <= 1:
            return

        if knot_x < leader_x:
            self.position = (knot_x + 1, knot_y)
        elif knot_x > leader_x:
            self.position = (knot_x - 1, knot_y)

        if knot_y < leader_y:
            self.position = (self.position[0], knot_y + 1)
        elif knot_y > leader_y:
            self.position = (self.position[0], knot_y - 1)


# Initializing
series_of_motions = []  # making the list of the series of motions
with open('input9.txt', 'r') as file:
    for line in file:
        line = line.strip().split(' ')
        character = line[0]
        number = int(line[1])
        series_of_motions.append((character, number))
grid = Grid()
knot0 = Knot((0, 0))
knot = [knot0]
n = 9
for i in range(n):
    knot.append(Knot((0, 0), knot[i]))


# Makin' Moves
grid.mark_visited((0, 0))
for motion in series_of_motions:
    for rep in range(motion[1]):
        for k in range(len(knot)):
            if k == 0:
                knot[k].move(motion[0])
            elif k == len(knot) - 1:
                knot[k].move_towards_leader()
                grid.mark_visited(knot[k].position)
            else:
                knot[k].move_towards_leader()

print(f'the number of positions visited: {len(grid.visited)}')
