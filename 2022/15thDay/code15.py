import re

class Node:
    def __init__(self, name, value, edges):
        self.name = name
        self.value = value
        self.edges = edges

# make a breadth first search for the nodes

info = []
with open("15thDay/demo15.txt", "r") as file:
    for line in file:
        line = line.strip().split("; tunnel")
        valve = re.search(r"[A-Z]{2}", line[0]).group()
        flow = int(re.search(r"\d+", line[0]).group())
        tindex = re.search(r"[A-Z]{2}", line[1]).span()[0]
        tunnels = line[1][tindex:]
        connections = tunnels.split(", ")
        info.append([valve, flow, connections])

print(info)