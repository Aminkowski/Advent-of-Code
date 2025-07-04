# read inputs and
    # put into 2 lists, then go through the lists, pairing up and subrtracting? (very ineff)
    # tally up the differences (what I'll do here)

from myFuncs import timer

g1List = []
g2List = []
# distance = 0

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
# assert distance == 0, "distance should be zero"

@timer
def pointerWannabe(g1, g2):
    #   NOTE: ASSUMING G1 AND G2 ARE SORTED
    g1.sort()
    g2.sort()
    distance = 0
    p1 = 0
    p2 = 0
    prev1 = 0
    prev2 = 0
    while p1 < len(g1) or p2 < len(g2):
        # using 'or' because want both to be "done" (handled with try/except)
        try:
            if g1[p1] == g2[p2]:
                prev1, prev2 = p1, p2   # interval start
                while g2[p2] == g1[prev1]:  p2 += 1     # after this g2[p2] > g1[p1]
                while g1[p1] == g2[prev2]:  p1 += 1     # now g1[p1] != g2[p2] is expected
                distance += g1[prev1] * (p1 - prev1) * (p2 - prev2)
            while g1[p1] < g2[p2]:  p1 += 1
            while g2[p2] < g1[p1]:  p2 += 1
            # now expect g1 p1 == g2 p2
        except IndexError:
            assert (p2 <= len(g2) and p1 <= len(g1)), "p2 or p1 > len"
            # whichever one hasn't reached its end, should go on until it does
            if p2 == len(g2):
                if g2[-1] != g2[prev2]: break   # if didn't go oob to find end range, we done
                while g1[p1] == g2[prev2] and p1 <= len(g1): p1 += 1
            else:
                if g1[-1] != g1[prev1]: break
                while g2[p2] == g1[prev1] and p2 <= len(g2): p2 += 1
            distance += g1[prev1] * (p1 - prev1) * (p2 - prev2)
            break
    return distance

print(pointerWannabe(g1List, g2List))


"""
for i in range(len(g1List)):
    try:
        if g1List[i] == g1List[i-1]:    # if same element, just re-add and move on
            distance += pointer - previous
            continue
    except IndexError:
        pass
    # if g1[i] > g2[p] then p++
    while g1List[i] > g2List[pointer]:  pointer += 1    # after this g1[i] <= g2[p]
    # if g1[i] < g2[p] then i++ (continue)
    if g1List[i] < g2List[pointer]:     continue
    # if gi[i] = g2[p] then incerement p until they're not, then add the value thingy
"""
