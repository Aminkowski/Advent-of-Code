class Part:
    def __init__(self, Number, IsIn = False):
        self.num = Number
        self.pn = IsIn

    def 
schematic = []
text = open("demo3.txt","r")
for line in text:
    line = line.strip()
    schematic.append([])
    for char in line:
        schematic[-1].append(char)
print(schematic)


