def list_of_coords(file):
    sensor_coords = []
    beacon_coords = []
    with open(file, 'r') as f:
        for line in f:
            temp = line.split(":")
            sensor_string = temp[0][10:]
            beacon_string = temp[1][22:]
            temp = sensor_string.split(", ")
            sensor_x, sensor_y = int(temp[0][2:]), int(temp[1][2:])
            sensor_coords.append((sensor_x, sensor_y))
            temp = beacon_string.split(", ")
            beacon_x, beacon_y = int(temp[0][2:]), int(temp[1][2:])
            beacon_coords.append((beacon_x, beacon_y))
    if len(sensor_coords) != len(beacon_coords):
        raise Exception("Parsing Error: number of sensor coordinates doesn't match up with the number of beacon coordinates.")
    return zip(sensor_coords, beacon_coords)

# There is never a tie where two beacons are the same distance to a sensor.
def l1(p1, p2):
    return abs(p1[0]-p2[0]) + abs(p1[1]-p2[1])

def disc(point, distance):
    # there is room for some optimization by removing the set stuff and replacing it with a faster data structure,
    # and instead modify i and j to start from 1 and add the 0 coords once. but it's less elegant and more cumbersome
    set_of_points_in_disc = set()
    for i in range(distance + 1):
        for j in range(distance-i + 1):
            set_of_points_in_disc.add((point[0]+i, point[1]+j))
            set_of_points_in_disc.add((point[0]-i, point[1]+j))
            set_of_points_in_disc.add((point[0]+i, point[1]-j))
            set_of_points_in_disc.add((point[0]-i, point[1]-j))
    # print(f'point {point} has been processed')
    return set_of_points_in_disc

def draw_disc(point, distance):
    sopid = disc(point, distance)
    representation = ""
    max_x = max(point[0] + distance + 2, 0)
    max_y = max(point[1] + distance + 2, 0)
    min_x = min(point[0] - distance - 2, 0)
    min_y = min(point[1] - distance - 2, 0)
    for i in range(min_x, max_x +1):
        # representation += f'{i} '
        for j in range(min_y, max_y +1):
            if (i,j) in sopid:
                representation += "#"
            else:
                representation += "."
        representation += "\n"
    print(representation)

def draw_disc(pointsNbeacons):
    # finding boundar values, making the set of all points
    soap = set()
    max_x = 0
    max_y = 0
    min_x = 0
    min_y = 0
    for sensor, beacon in pointsNbeacons:
        distance = l1(sensor, beacon)
        soap = soap.union(disc(sensor, distance))
        max_x = max(max_x, sensor[0] + distance)
        max_y = max(max_y, sensor[1] + distance)
        min_x = min(min_x, sensor[0] - distance)
        min_y = min(min_y, sensor[1] - distance)
    max_x += 2
    max_y += 2
    min_x -= 2
    min_y -= 2
    # making the first row_characters)
    ## initializing the first row characters into a list
    first_row_characters = [(str(i) if i%5 == 0 else " ") for i in range(min_x, max_x +1)]
    ## removing the first / last index if too long to fit
    if len(first_row_characters[0]) > 1:       # mostly personal pref, assumes -99 < index < 99
        first_row_characters[0] = " "
    elif (len(first_row_characters[1]) == 3) and (first_row_characters[1][0] == "-"):
        first_row_characters[1] = " "
    if len(first_row_characters[-1]) > 1: first_row_characters[-1] = " "
    ## creating first row
    first_row = ""
    index = 0
    while index < len(first_row_characters):
        if first_row_characters[index] != " ":
            # a number. is it positive or negative? what is it's length in total?
            negative = first_row_characters[index][0] == "-"
            digits = len(first_row_characters[index])
            if negative:    # take away last digits-1 spaces and replace it with the number
                # as such the number ends at the appropriate index
                digits = (digits * -1) + 1
                first_row = first_row[:digits] + first_row_characters[index]
            else:       # just concat the number at the end, skip the corresponding spaces
                first_row += first_row_characters[index]
                index += digits - 1
        else:
            first_row += " "
        index += 1
    # print(first_row)
    # print(first_row_characters)
    # making the representation of all the l1-discs
    representation = ""
    for j in range(min_y, max_y +1):
        # representation += f'{i} '
        for i in range(min_x, max_x +1):
            if (i,j) in soap:
                representation += "#"
            else:
                representation += "."
        representation += "\n"
    # representation = first_row + "\n" + representation
    # print(representation)
    # adding in the index column
    first_col_characters = [str(i) for i in range(min_y, max_y +1)]
    for i in range(len(first_col_characters)):   # since I know boundaries are between +/- 99, I'll just pad them with spaces till they reach 4 characters
        while len(first_col_characters[i]) < 4:
            first_col_characters[i] += " "
    # print(first_col_characters)
    lines = representation.split("\n")
    lines.pop()
    representation = "    " + first_row + "\n"
    for i in range(len(lines)):
        representation += first_col_characters[i] + lines[i] + "\n"
    print(representation)
    # print(len(lines))
    # print(len(first_col_characters))

###############################

# soap = set()    # set_of_all_points
# beacons = []
# for sensor_p, beacon_p in list_of_coords("demo.txt"):
    # beacons.append(beacon_p)
    # print(l1(sensor_p, beacon_p))
    # draw_disc(sensor_p, l1(sensor_p, beacon_p))
    # soap.union(disc(sensor_p, l1(sensor_p, beacon_p)))

# counter = 0
# for point in soap:
#     if (point[1] == 10) and (point not in beacons):
#         counter += 1
# print(counter)

# draw_disc(list_of_coords("demo.txt"))

# read out and make a list of the sensor locations + beacon locations + distance corresponding to the pair
# make a function which takes in a row number, along with the given list, and outputs the number of points on that row where there can be no beacon
# you do this by going through the sensors and their corresponding distances and seeing how many points in that row fall within that disc
# then you either make a list of these points, and make a union of these points in a set, then take away the beacon points and read out the length
# or you do it more manually (since this is the other extreme from what I've been doing so far I'll try this)
# where you don't use sets, and just use inequalities to add new points for maximal efficiency

# got the "range" in the row which falls within the disc, now "make a union" of the ranges
# ok this is taking a while, what's left is making this list of ranges, adding them up, and then counting
# but the adding them up part is proving to be a bit annoying in the details (try/except, well-ordering, ...)
# at this point this can have next to no runtime, since it scales just with the number of items. so maybe it's best if I just leave the hyper optimizations for later if I feel eager to do it after the fact, but just get it over for now

def unbeacon_row(row, point, distance):
    dy = abs(point[1] - row)
    if dy > distance: return None
    row_from = point[0] - (distance - dy)
    row_to = point[0] + (distance - dy)
    return (row_from, row_to)

def union_of_ranges(r1, r2):
    '''
    parameters: r1, r2 both **ordered** numeric tuples
    output: a list of tuples
    '''
    # 3 scenarios: one envelopes the other / disjoint / intersect
    begins_lower = r1 if r1[0] < r2[0] else r2
    ends_higher = r1 if r1[1] > r2[1] else r2
    if begins_lower == ends_higher:
        return [ begins_lower ]
    else:
        disjoint = begins_lower[1] < ends_higher[0]
        if disjoint:
            return [begins_lower, ends_higher]
        else:
            return [ (begins_lower[0], ends_higher[1]) ]

# just realized union could have merged things that end right next to eachother, like (1,2) and (3,4) becomes (1,4) because we're dealing with ints not reals

# print(union_of_ranges( (0,10), (0,10) ))   # should return [(0,10)]
# print(union_of_ranges( (0,10), (0,9) ))   # should return [(0,10)]
# print(union_of_ranges( (0,10), (1,10) ))   # should return [(0,10)]
# print(union_of_ranges( (0,8), (0,9) ))   # should return [(0,9)]
# print(union_of_ranges( (1,9), (0,9) ))   # should return [(0,9)]
#
# print(union_of_ranges( (3,6), (3,6) ))   # should return [(,)]
# print(union_of_ranges( (3,6), (3,6) ))   # should return [(,)]
# print(union_of_ranges( (4,6), (3,7) ))   # should return [(,)]
# print(union_of_ranges( (3,7), (4,6) ))   # should return [(,)]
#
# print(union_of_ranges( (3,6), (4,7) ))   # should return [(,)]     ## r1 below r2 intesecting
# print(union_of_ranges( (4,7), (3,6) ))   # should return [(,)]     ## r1 above r2 intesecting
# print(union_of_ranges( (3,6), (6,9) ))   # should return [(,)]     ## r1 just below r2 intesecting
# print(union_of_ranges( (6,9), (3,6) ))   # should return [(,)]     ## r1 just above r2 intesecting
# print(union_of_ranges( (3,6), (7,10) ))   # should return [(,)]    ## disjoint, r1 below r2
# print(union_of_ranges( (7,10), (3,6) ))   # should return [(,)]    ## disjoint, r1 above r2

# =================

def range_in_row(row, file):    # takes in the file and the row you want to investigate, returns the range of intersections in the row
    ranges = []
    # sensors_in_row = 0
    # beacons_in_row = set()
    for sensor_p, beacon_p in list_of_coords(file):
        # print(sensor_p, l1(sensor_p, beacon_p))
        # print(unbeacon_row(0, sensor_p, l1(sensor_p, beacon_p)))
        # if sensor_p[1] == row: sensors_in_row += 1
        # if beacon_p[1] == row: beacons_in_row.add(beacon_p)
        pair = unbeacon_row(row, sensor_p, l1(sensor_p, beacon_p))
        if pair is None:
            continue
        else:
            ranges.append(pair)
    ranges.sort()
    # print(beacons_in_row)
    # print(ranges)
    return ranges

def number_of_elts(ranges):     # takes in ranges of intersection, returns number of elements in those ranges
    rindex = 0
    if len(ranges) == 0:
        print("just 0")
        return 0
    elif len(ranges) == 1:
        # print(f'there is only one interval: {range[0]}\n which has {range[0][1] - range[0][0] + 1} elements in it')    # nvm this - sensors_in_row  doesn't affect it  # - len(beacons_in_row)
        return range[0][1] - range[0][0] + 1
    else:
        while rindex < len(ranges) -1:
            u = union_of_ranges(ranges[rindex], ranges[rindex +1])
            if len(u) == 2:
                rindex +=1      # disjoint, let it be
            elif len(u) == 1:   # union made a diff, replace two pairs with union
                before = ranges[:rindex]    # everything up until what has been unioned
                after = ranges[rindex+2:]   # everything after what has been unioned
                ranges = before + u + after
                print(ranges)
            # else:
            #     raise Exception("wtf")
        total=0
        for r in ranges:
            total += r[1] - r[0] + 1
        print(f'the intervals add up to having {total} elements.')     # nvm sensors are already counted    #  - len(beacons_in_row)
        return total

row = 2000000
# for row in range(4000001):
    # pass
file = "input.txt"
number_of_elts(range_in_row(row, file) )
