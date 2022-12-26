# section ID, elves, clear space, assignment overlap, reduce redundant eff
# range of IDs per elf, list of sect. assignments = input
# pairs of elves, overlap of sections; outcome1 = how many inclusions

def fullycontain(tuple1, tuple2):
    bot = min(tuple1[0], tuple2[0])
    top = max(tuple1[1], tuple2[1])
    if (bot, top) == tuple1 or (bot, top) == tuple2:
        return 1  # True
    else:
        return 0  # False


def overlap(tuple1, tuple2):
    if tuple1[0] > tuple2[1]:
        return 0
    elif tuple1[1] < tuple2[0]:
        return 0
    else:
        return 1


balist = open("input4.txt")
pairsect = []
for line in balist:
    ep = ["", "", "", ""]
    index = 0
    for letter in line:
        if letter == "-" or letter == ",":
            index += 1
            continue
        elif letter == "\n":
            continue
        ep[index] = ep[index] + letter
    pairsect.append(((int(ep[0]), int(ep[1])), (int(ep[2]), int(ep[3]))))
    # continue or pass here affect nothing. pass obvi, ctu cuz nothing after
# print(pairsect)
# containlist = [fullycontain(pair[0], pair[1]) for pair in pairsect]
# print(sum(containlist))
overlaplist = [overlap(pair[0], pair[1]) for pair in pairsect]
print(sum(overlaplist))
