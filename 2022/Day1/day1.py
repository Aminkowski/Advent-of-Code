# magical energy, star fruit snack, 50+ needed by dec 25, 
# grabbed other fruits; collct stars by solving puzzles? x/2
# track calories: written in files with given format
# output how much calories the elf with the most calories is carrying
# method 1: create loop going through file tracking current elf and maxelf
# method 2: f(i,m) = if endoffile return m, else f(i w.o 'head', max(m, sum of 'head')) 
# method 3: make elf / group object and have methods do the work
# since I feel least comfortable with option 3 I'll do that

class Elf:
    def __init__(self, name, bag):
        self.name = name
        self.bag = bag

    def pick(self, fruit):
        self.bag.append(fruit)

    def total(self):
        return sum(self.bag)

group = [Elf(1,[])]
#group.append(Elf("howard", [0,2,3,4]))

list = open("input1.txt")
#list = open("demo1.txt")
for l in list:
    if l == "\n":
        group.append(Elf(1+len(group),[]))
    else:
        group[-1].pick(int(l))

maks = [0,0,0]
for e in group:
    if maks[0] < e.total():
        maks = [e.total(), maks[0], maks[1]]
    elif  maks[1] < e.total():
        maks = [maks[0], e.total(), maks[1]]
    elif maks[2] < e.total():
        maks = [maks[0], maks[1], e.total()]

print(maks, sum(maks))
# it turned out a lot less elegant than I was hoping I'd make it, 
# but oh well
