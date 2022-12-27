# crate stacks, rearrange by moving N from top b.w stacks, what are top stacks?

def crame(N, fro, to, supplies):
    supplies[to-1] = supplies[fro-1][0:N] + supplies[to-1]
    for i in range(N):
        supplies[fro-1].pop(0)
    return supplies


def crane(N, fro, to, supplies):
    for i in range(N):
        # print(supplies)
        supplies[to-1].insert(0, supplies[fro-1][0])
        supplies[fro-1].pop(0)
    return supplies


# from unpleasant IO type to [[Char]] vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv
supp = open("input5.txt")
suppl = []
for line in supp:
    suppl.append([])
    for letter in line:
        suppl[-1].append(letter)

# turining inputs into a nice format vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv
# len(suppl[0]) = 3*#ofcrates+1for\n+(#ofcrates-1)
ncrates = int(len(suppl[0])/4)
# suppli = [[]] * ncrates  doing this all the entries get reffered to as one?
# as in with the loop below all "stacks" would get a copy of the crate
supply = []
for i in range(ncrates):
    supply.append([])
to = []
fro = []
N = []
for row in suppl:
    if row == ["\n"]:
        break
    for i in range(ncrates):
        if row[1 + 4 * i] != " ":
            supply[i].append(row[1 + 4 * i])
for column in supply:
    column.pop()
# supply done ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
for i in range(len(suppl)):  # removing the supply shape
    suppl.pop(0)
    if suppl[0] == ["\n"]:
        suppl.pop(0)
        break
for line in suppl:  # removing the "move " from the lines and reversirg
    for i in range(5):
        line.pop(0)
    line = line.reverse()
for line in suppl:  # filling up the to[] and from[] list
    to.append(int(line[1]))  # the indices work because
    fro.append(int(line[6]))  # the stack labels are single digit
    N.append(0)  # just initializing N
    for i in range(13):  # removing everything but N
        line.pop(0)
    # line = line.reverse()  # relevant when N has more than 1 digit
    # I'm retarded, the reverse order actually works with the digit thing
for i in range(len(suppl)):
    for j in range(len(suppl[i])):
        N[i] += int(suppl[i][j]) * (10 ** j)
# now for the actual problem solving lol vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv
for i in range(len(suppl)):
    # crane(N[i], fro[i], to[i], supply)
    crame(N[i], fro[i], to[i], supply)
answer = []
for i in range(ncrates):
    if supply[i] == []:
        answer.append([])
    else:
        answer.append(supply[i][0])
print(answer)
