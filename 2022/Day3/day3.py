# elf didn't pack properly => need to rearrange
# rucksack, 2 compartments, item types separated into comps
# 1 item per comp of different type from the rest (rather than 0)
# input = list of all items in each ruck sack, find errors
# item types identified w/ unique ucase or lcase letters
# characters in a line = all items in a sack, # of items in each comp is =
# looking for repeats in each comp, then want 'prio sum' of errors

def priority(char):
    if char.islower():
        return ord(char) - 96
    else:
        return ord(char) - 64 + 26


def errorlist(filename):
    list = open(filename)
    error = []
    counter = 0
    for sack in list:
        counter += 1
        comp = int((len(sack) - 1)/2)
        for i in range(0, comp):
            if len(error) == counter:
                continue
            for j in range(comp, 2*comp):
                if len(error) == counter:
                    continue
                # print(i, sack[i], j, sack[j], error, counter)
                if sack[i] == sack[j]:
                    error.append(sack[i])
                    continue
    return error


def badgelist(filename):
    list = open(filename)
    badge = []
    counter = 0
    for sack in list:
        counter += 1
        if counter % 3 == 1:  # then make set1
            itemset = set({})
            for item in sack:
                itemset.add(item)
            itemset.remove("\n")
            # print(itemset)
        elif counter % 3 == 2:  # then make set2
            itemset2 = set({})
            for item in sack:
                itemset2.add(item)
            itemset2.remove("\n")
            # print(itemset2)
        else:  # on third line find badge by:
            inter = itemset.intersection(itemset2)
            # print(inter)
            if len(inter) == 1:  # if intersection is a singleton then done
                for x in inter:
                    badge.append(x)
                    # print("singleton")
            else:  # else find the one item that is in all 3 and badge it
                for item in sack:
                    if len(badge) == int(counter/3):
                        continue
                    # print(item)
                    if not inter.isdisjoint({item}):
                        # print("found it!")
                        badge.append(item)
        # print(badge, counter)
    return badge


'''
zum = 0
for item in errorlist("input3.txt"):
    zum += priority(item)

print(zum)
'''

# elves divided into groups of three, all carry a badge related to group
# badge is an item type, only item type carried by all members of group
# find badge
# print(badgelist("demo3.txt"))

zum = 0
for item in badgelist("input3.txt"):
    zum += priority(item)

print(zum)
