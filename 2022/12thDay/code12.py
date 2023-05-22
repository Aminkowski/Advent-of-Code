""" starting at the S... I guess first we could go through the map and turn it into ints so that we can compare easy
then we do two things. feels like there is a recursion here somewhere. 
one we evaluate what paths are possible. so at most 4 based on this puzzle, but no ruturning to where you came from and no going up by two. 
then we take every path? and keep track of the least number of steps it took to reach that spot. 
so here's what I'm thinking: have the set of all vertices. assuming they're all connected, by the end they should all have been visited
then if we could go to all of thim then the problem would be trivial, so let's not start with all the possible edges.
we keep track of the visited vertices, where the list is initially [S]. then we loop through the list and check what edges they have
we do that in this case by considering the 4 orthogonal directions, and discarding the paths we can't take (diff >= 2) and the paths which have been taken?
nah, that'll require keeping track of all paths taken which is like ~ n^2 items. could blow up. 
instead keep track of how many steps it has taken to get there and terminate if it is longer than what has been previously reached. if it is shorter we update
ok so recap... wait.
ok so let V be the set of all vertices. make a dictionary that has elts of v bound to +infinity. 
then have a subset of v of "current" vertices, say R. initially set R = {S}.
then loop over R. for all v in R, check edges. here we do that by checking orthos, and those give an element of V
    actually we first see the associated elevation of the vertex. if it's higher than v+1 then we discard it (continue? pass?)
before / with the loop set a counter for how many iterations we have gone through. 
for each V, compare the current associated number with V in the dictionary with the number of current iterations. 
if the number of iterations is less, then we replace the dictionary value. 
continue to do this for all vertices until we reach the endpoint? because after that we ... do we? 
yeah, I think all the paths found after that will be longer...?
ok is it possible to find a shorter path to vertex already reached? no
yead we done. ''', then we replace the dictionary value. 
continue to do this for all vertices until we reach the endpoint? because after that we ... do we? 
yeah, I think all the paths found after that will be longer...?
ok is it possible to find a shorter path to vertex already reached? no
yead we done. """



import time
import numpy as np

def Climbable(current: int, destination: int) -> bool:
    #if current == -14:
    #    current = 0
    if current == -28:
        current = 25
#destination == -28:
#        destination = 25

    #if destination <= current + 1:
    if current - 1 <= destination:  # want to start from end and reach the first a, so it's "descendable" if current - 1 <= destination
        return True
    else:
        return False

def Inbounds(edge, row, col):
    return edge[0] >= 0 and edge[1] >= 0 and edge[0] <= row - 1 and edge[1] <= col - 1


def Find(array: list, value: int) -> tuple:
    for i in array:
        if value in i:
            return (array.index(i), i.index(value))
        else:
            continue

def Paths(i: int, j: int) -> list:
    return [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]

hmap = []

with open("input12.txt", "r") as file:
    for line in file:
        line = line.strip()
        hmap.append([])
        for col in line:
            hmap[-1].append(ord(col) - 97)
#print(hmap)
row = len(hmap)
col = len(hmap[0])
infinity = row * col
shortest_path = [[infinity for i in range(col)] for j in range(row)]
#print(shortest_path)
start = Find(hmap, -14)
end = Find(hmap, -28)
#print(start, end)
reached = set([end]) #set([start])
desired_nodes = set()
for i in range(row):
    for j in range(col):
        if hmap[i][j] == 0 or hmap[i][j] == -14:
            desired_nodes.add((i, j))
step = 0
while not desired_nodes.intersection(reached): #while not end in reached:
    temp = []
    for node in reached:
        #print(f'looking at {node}')
        shortest_path[node[0]][node[1]] = step
        for edge in Paths(node[0], node[1]):
            if Inbounds(edge, row, col) and Climbable(hmap[node[0]][node[1]], hmap[edge[0]][edge[1]]):
                #print(f'{edge} is a valid path')
                if shortest_path[edge[0]][edge[1]] > step:
                    temp.append(edge) 
        #print(f'all edges of {node} have been checked, {temp} are reached')
    reached = set(temp)
    step += 1
print(np.array(shortest_path))
print(step)
