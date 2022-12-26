# okay so x is lose, y is draw, z is win
class Round:
    def __init__(self, opponent, result):
        self.op = opponent
        self.r = result

    def shape(self):
        if ((self.op == "A" and self.r == "Y")  # rock, draw = rock
                or (self.op == "B" and self.r == "X")  # paper, lose
                or (self.op == "C" and self.r == "Z")):  # scissors, win
            return 1
        elif ((self.op == "A" and self.r == "Z")  # rock, win = paper
                or (self.op == "B" and self.r == "Y")  # paper, draw
                or (self.op == "C" and self.r == "X")):  # scissors, lose
            return 2
        else:
            return 3

    def outcome(self):
        if self.r == "X":
            return 0
        elif self.r == "Y":
            return 3
        elif self.r == "Z":
            return 6
        else:
            return "error"

    def score(self):
        return self.shape() + self.outcome()


guide = open("input2.txt")
game = []

for line in guide:
    game.append(Round(line[0], line[2]))

tot = 0
for roun in game:
    tot += roun.score()

print(tot)
