
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
series_of_motions = open('demo9.txt')
grid = Grid()
knot0 = Knot((0, 0))
knot = [knot0]
n = 1
for i in range(n):
    knot.append(Knot((0, 0), knot[i-1]))



grid.mark_visited((0, 0))  # Marking the initial position of the leader knot as visited

# Moving the leader knot
knot0.move('R')
knot0.move('U')
knot0.move('R')

# Moving knots towards the leader knot
knot[1].move_towards_leader()

print(grid.is_visited((0, 0)))  # Output: True
print(grid.is_visited((2, 1)))  # Output: False
print(grid.is_visited((3, 2)))  # Output: False

print(knot0.position)  # Output: (1, 1)
print(knot[1].position)  # Output: (2, 1)

