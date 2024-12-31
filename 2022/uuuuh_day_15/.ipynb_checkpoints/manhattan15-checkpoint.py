# There is never a tie where two beacons are the same distance to a sensor.
def l1(p1, p2):
    return abs(p1[0]-p2[0]) + abs(p1[1]-p2[1])