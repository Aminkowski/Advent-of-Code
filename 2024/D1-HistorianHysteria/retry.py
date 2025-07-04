from myFuncs import timer

g1List = []
g2List = []

with open("input.txt") as file:
    for line in file:
        line = line.strip().split("   ")
        if len(line) == 2:
            fst, snd = map(int, line)
            g1List.append(fst)
            g2List.append(snd)
        else:
            raise Exception(line)

assert len(g1List) == len(g2List), "Lists not of same size!?!"

@timer
def simplest(l1, l2):
    distance = 0
    for x in l1:
        counter = 0
        for y in l2:
            if x == y:
                counter += 1
        distance += x*counter
    return distance

print(simplest(g1List, g2List))
