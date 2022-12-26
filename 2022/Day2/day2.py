# we playin RPS now, game contains many rounds, std rps rules
# encrypted strat guide = input, A = rocks, B = paper, C = scissors
# input may be winning strat, {X,Y,Z} = {r,p,s}, not sus, max score wins
# total score = sum(round scores), round scores = shape pt + outcome pt
# shape pt: r = 1, p = 2, s = 3; outcome pt = 0 loss, 3 draw, 6 win
# apparently x = rock, y = paper, z = scissors
class Round:
    def __init__(self, opponent, response):
        self.op = opponent
        self.r = response

    def outcome(self):
        if ((self.op == "A" and self.r == "Y")
                or (self.op == "B" and self.r == "Z")
                or (self.op == "C" and self.r == "X")):
            return 6
        elif ((self.op == "A" and self.r == "Z")
                or (self.op == "B" and self.r == "X")
                or (self.op == "C" and self.r == "Y")):
            return 0
        else:
            return 3

    def shape(self):
        if self.r == "X":
            return 1
        elif self.r == "Y":
            return 2
        elif self.r == "Z":
            return 3
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

'''for letter in line:
        print("henlo")
        if ((letter == "\n")
                or (letter == " ")
                or (letter == "A")
                or (letter == "B")
                or (letter == "C")
                or (letter == "X")
                or (letter == "Y")
                or (letter == "Z")):
            continue
            # pass
            print("hi")
        print(letter, type(letter))
'''
