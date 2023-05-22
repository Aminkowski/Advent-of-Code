import re
import time

class Monkey:
    def __init__(self, starting_items = [], operation = ( ), test = 0, target = ( )):
        self.s = starting_items
        self.o = operation
        self.test = test
        self.t = target

    def __repr__(self):
        return f'{self.s}, {self.o}, {self.test}, {self.t}'

    def Worry(self):
        multiplier = 0
        if self.o[1] == "old":
           multiplier = self.s[0]
        else:
            multiplier = int(self.o[1])
        if self.o[0] == "*":
            self.s[0] *= multiplier
        elif self.o[0] == "+":
            self.s[0] += multiplier
        else:
            return "ERROR"

    def Test(self):
        if self.s[0] % self.test == 0:
            return True
        else:
            return False

def Calm(worry):
    return worry % simplify  #// 3

def Throw(ms, thrower):
    ms[thrower.t[not thrower.Test()]].s.append(thrower.s[0])
    thrower.s.pop(0)


monkeys = []
with open("input11.txt", "r") as file:
    for line in file:
        line = line.strip().split(":")
        if line == [""]:
            continue
        if re.match("M", line[0]):
            monkeys.append(Monkey())
        elif re.match("S", line[0]):
            monkeys[-1].s = list(map(int, line[1].split(",")))
        elif re.match("O", line[0]):
            monkeys[-1].o = tuple(line[1].split(" old ")[1].split(" "))
        elif re.match("T", line[0]):
            monkeys[-1].test = int(line[1].split(" by ")[1])
        elif re.search("true", line[0]):
            monkeys[-1].t = (int(line[1][-1]), )
        elif re.search("false", line[0]):
            monkeys[-1].t = (monkeys[-1].t[0], int(line[1][-1]))

simplify = 1
for m in monkeys:
    simplify *= m.test  # i love math. math is too good for this world. math is pure beauty. math is transcendent. 

#for m in monkeys:
#    print(m)
inspect = [0,0,0,0,0,0,0,0]
for round in range(10000):
    counter = 0
    for turn in monkeys:
        while turn.s:
            inspect[counter] += 1
            turn.Worry()  # monkey inspects and I worry
            turn.s[0] = Calm(turn.s[0])  # monkey gets bored and I calm
            Throw(monkeys, turn)  # test occurs and thrown
        counter += 1
    if round % 1000 == 999:
        print(inspect)
most = max(inspect)
inspect.remove(most)
mbusiness = most * max(inspect)
print(mbusiness)
