# comm device, lock onto signal, signal = series of random characters
# fix = add 'subroutine' to s-o-p marker, s-o-p = 4 char seq, all diff
# datastream buffer = input,

import sys
# print(sys.getrecursionlimit())
sys.setrecursionlimit(4100)
# print(sys.getrecursionlimit())


def marker(line, counter):  # set conter = 0 initially
    startmarker = []
    for i in range(14):
        startmarker.append(line[i])
    print(startmarker)
    if len(set(startmarker)) == 14:
        print(counter + 14)
        # return counter + 4  # alternatively could have just init at 4
        # for some reason return wouldn't work
    else:
        marker(line[1:], counter + 1)


datastream = open("input6.txt")
# answer = []
for line in datastream:
    marker(line, 0)  # answer.append(marker(line, 0))
# print(answer)
