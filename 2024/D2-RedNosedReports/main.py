# line = report, data = level
# which are safe: monotonic and gradual (1 <= d <= 3)
# from ../../.. import myFuncs

reports = []
with open("input.txt") as file:
    for report in file:
        report = report.strip().split(" ")
        reports.append(list(map(int, report)))

# numberOfLevels = len(reports[0])
# for report in reports:
    # assert len(report) == numberOfLevels, "didn't parse correctly"
# There must be a better way to check than this (more concise, more time eff)

'''counter = 0
for report in reports:
    d1 = int(report[1]) - int(report[0])
    increasing = d1 > 0
    # print(increasing)
    if ( abs(d1) >= 1 and abs(d1) <= 3 ):
        safe = True
        tolerance = 1
        # print("new loop, safe = true")
    else:
        # safe = False
        safe = True
        tolerance = 0
        # print("new loop, starts off too big")
    for i in range(2, len(report)):
        diff = int(report[i]) - int(report[i-1])
        # print(diff)
        if (diff > 0) == increasing:
            if 1 <= abs(diff) and abs(diff) <= 3:
                # print("both conditions met, safe")
                continue
            else:
                safe = False
                # print("diff not between 1 and 3. unsafe + break")
                break
        else:
            safe = False
            # print("diff changed sign. unsafe")
            break
    counter += safe
    # print(safe)
print(counter)'''
def compose(f, g):  return lambda x: f(g(x))
def both(b1, b2):   return (b1 and b2) or (not b1 and not b2)
def isNone(x): return x is None

def isMonotonic(report):
    for i in range(2, len(report)):
        if both(report[i-2] < report[i-1], report[i-1] < report[i]):    continue
        else: return False #i
    return True #None

def isGradual(report):
    for i in range(1, len(report)):
        diff = abs(report[i] - report[i-1])
        if (1 <= diff) and (diff <= 3):     continue
        else: return False #i
    return True #None

# def brutus(report, i):
#     r1 = report[:i-1] + report[i:]
#     r2 = report[:i] + report[i+1:]
#     return (r1, r2)
#
# def brutusMono(report, i):
#     r0 = report[:i-2] + report[i-1:]
#     r1 = report[:i-1] + report[i:]
#     r2 = report[:i] + report[i+1:]
#     return (r0, r1, r2)

def brutus(report):
    possibilities = []
    for i in range(len(report)):
        possibilities.append(report[:i]+report[i+1:])
    return possibilities

def safe(report):
    # monotonics = list(map(isMonotonic, brutus(report)))
    # graduals = list(map(isGradual, brutus(report)))
    # pairs = any(map(all, zip(monotonics, graduals)))
    return any(map(all, zip(list(map(isMonotonic, brutus(report))), list(map(isGradual, brutus(report))))))

# @myFuncs.timer
def bruteForce(reports):
    counter = 0
    for report in reports:
        # print(isMonotonic(report))
        # print(isGradual(report))
        # if isMonotonic(report) is None and isGradual(report) is None:
            # print("safe")
        # else:
            # print("unsafe")
            # brutus(report, isGradual(report))
            # brutusMono(report, isMonotonic(report))
        # if isMonotonic(report) is not None:
            # print(any(map(compose(isNone, isMonotonic), brutusMono(report, isMonotonic(report)))))
        # if isGradual(report) is not None:
            # print(any(map(compose(isNone, isGradual), brutus(report, isGradual(report)))))
        # monotonic = (isMonotonic(report) is None) or any(map(compose(isNone, isMonotonic), brutusMono(report, isMonotonic(report))))
        # gradual = (isGradual(report) is None) or any(map(compose(isNone, isGradual), brutus(report, isGradual(report))))
        # if monotonic and gradual:   counter += 1
        if safe(report): counter += 1
    return counter
print(bruteForce(reports))

# this was the most straight forward way
# but is very slow
# main issue: carries out every computation to the end even when the outcome is determined
# attempting to quicken via managing variables manually

def main(reports):
    counter = 0
    for report in reports:
        i, j = 0, 1     # assuming len(report) > 1
