import time

class Register:
    def __init__(self):
        self.register = 1
        self.cycle = 1
        self.tracker = 0
        self.value = 0

    def tick(self):
        self.cycle += 1
        self.tracker -= 1
        if self.tracker == 0:
            self.register += self.value
        #print(f'Cycle ended, all due instructions executed')
        
    def noop(self):
        self.tracker = 1
        self.value = 0

    def addx(self, V):
        self.tracker = 2
        self.value = V

    def signal_strength(self):
        return self.register * self.cycle

       
cpu = Register()
sample = []
program = []

with open("input10.txt") as file:
    for line in file:
        line = line.strip().split(" ")
        if len(line) == 2:
            program.append((line[0], int(line[1])))
        else:
            program.append((line[0], 0))

while program or cpu.tracker > 0:
    if cpu.tracker == 0:
        if program[0][0] == "addx":
            cpu.addx(program[0][1])
            #print(f'{cpu.cycle}: addx {program[0][1]} begins, X = {cpu.register}, process will execute in {cpu.tracker} cycles')
        elif program[0][0] == "noop":
            cpu.noop()
            #print(f'{cpu.cycle}: noop begins, X = {cpu.register}, process will execute in {cpu.tracker} cycles')
    if (cpu.cycle - 1) % 40 in [cpu.register - 1, cpu.register, cpu.register + 1]:
        sample.append("#")
    else:
        sample.append(".")
    cpu.tick()
    if cpu.tracker == 0:
        program.pop(0)
    #time.sleep(0.1)
#print(sample)
line = ["", "", "", "", "", ""]
for i in range(6):
    for j in range(40):
        line[i] += sample[i * 40 + j]
        
for l in line:
    print(l)
