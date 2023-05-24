import ast
import random
from dead_hopes_and_rotting_dreams import Partition, Qsort

def generate_random_list(size, min_value, max_value):
    random_list = []
    for _ in range(size):
        random_list.append(random.randint(min_value, max_value))
    return random_list

def is_sorted(lst):
    return all(lst[i] <= lst[i+1] for i in range(len(lst)-1))

def Compare(a, b):
    if type(a) is type(b):
        if type(a) is list:  # if both are lists
            try:
                for i in range(max(len(a), len(b))):
                    c = Compare(a[i], b[i])
                    if type(c) is bool:
                        return c
                    else:
                        continue
                print(f'{a} and {b} are the same.')
            except IndexError:
                return len(a) < len(b)
        else:  # if both are ints
            if a == b:
                return None
            else:
                return a < b
    else: 
        if type(b) is list:
            return Compare([a], b)  # make sure to return the recursive call...
        else:
            return Compare(a, [b])  # lost so much time debugging this little bs. I almost flashed ;(


def Brute_sort(pack, to):
    n = len(pack)
    if n == 1 or n == 0:  # I hate coding. I fucked myself over n == 0 even though I thought of it at first. fuck
        return pack
    elif n == 2:
        if to(pack[0], pack[1]):
            return pack
        else:
            return [pack[1], pack[0]]
    pivot = pack.pop()
    lower = []
    upper = []
    for item in pack:
        if to(item, pivot):
            lower.append(item)
        else:
            upper.append(item)
    lower = Brute_sort(lower, to)
    upper = Brute_sort(upper, to)
    return lower + [pivot] + upper

packets = []
with open("demo13.txt", 'r') as file:
    for line in file:
        line = line.strip()
        if line:
            try:
                evaluated = ast.literal_eval(line)
                packets.append(evaluated)
            except (SyntaxError, ValueError):
                print(f"Invalid line: {line}")
#print(packets)

if False:
    right_order = []
    for i in range(int(len(packets)/2)):
        if Compare(packets[2*i], packets[2*i + 1]):  # since print has None type output, when they are equal we don't add the index to the list which isn't right or wrong since that shouldn't happen
            right_order.append(i+1)
    print(f'{right_order} are the good indices. sum = {sum(right_order)}')

if True:
    packetd = packets + [ [[6]], [[2]] ]
    #print(packetd)

    for i in range(10):
        rl = generate_random_list(2*5, -100 , 200)
        print(rl)
        #brute = Brute_sort(rl, Compare)
        qs = Qsort(rl, Compare)#0, len(rl)-1, Compare)
        print(qs)
        #print("sorted" if is_sorted(qs) else "NOT SORTED")

if False:
    packetd = packets + [ [[6]], [[2]] ]
    #print(packetd)
    brute = Brute_sort(packetd, Compare)
    print(f'sorted packet is:')
    for item in brute:
        print(f'       {item}')

if False:
    packetd = packets + [ [[6]], [[2]] ]
    #print(packetd)
    brute = Brute_sort(packetd, Compare)
    indices = []
    counter = 1
    while len(indices) < 1:
        if brute[counter-1] == [[2]]:
            indices.append(counter)
        counter += 1
    while len(indices) < 2:
        if brute[counter-1] == [[6]]:
            indices.append(counter)
        counter += 1
    decoder_key = indices[0]*indices[1]
    print(decoder_key)
