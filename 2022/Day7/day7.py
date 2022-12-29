class File:
    def __init__(self, name, parent=None, contents=[]):
        self.n = name
        self.p = parent
        self.c = contents

    def size(self):
        total = 0
        if type(self.c) == int:
            total = self.c
            # print(total)
        else:
            for f in self.c:
                total += f.size()
                # print(total)
        return int(total)

    def disp(self):
        out = str("")
        out = out + self.n
        print(out)
        if type(self.c) == int:
            print(self.c)
        else:
            print("begin")
            for f in self.c:
                f.disp()
            print("end")


terminal = open("input7.txt")
wd = "fuck"  # working directory
fs = [File("/")]  # filesystem
terminall = []
for line in terminal:
    terminall.append(line)
for line in terminall:
    if line[0] == "$":
        if line[2] == "c":
            to = line.rpartition("cd")[2].strip()
            if to == "..":
                wd = wd.p
                '''print(line.strip())
                print("working directory changed to ", wd.n)'''
            else:
                if wd == "fuck":
                    '''print(line.strip())
                    print("from None to /")'''
                    wd = fs[0]
                    continue
                # wd = wd.c[wd.c.index(File(to, fs[fs.index(wd)], []))]
                for f in wd.c:
                    if f.n == to:
                        wd = f
                '''print(line)
                print("working directory changed to ", wd.n)'''
        else:
            pass
            '''print(line, " did nothing")'''
    elif line[0] == "d":
        ch = line.partition(" ")
        fs.append(File(ch[2].strip(), fs[fs.index(wd)], []))
        wd.c.append(fs[-1])
        '''print(line.strip())
        for f in wd.c:
            print(f.n)'''
    else:
        ch = line.partition(" ")
        fs.append(File(ch[2].strip(), fs[fs.index(wd)], int(ch[0])))
        wd.c.append(fs[-1])
        '''print(line.strip())
        for f in wd.c:
            print(f.n)'''
# fs[0].disp()
# directory, size <= 100,000, output sum of sizes
# totall = 0
# need = 30000000 - available space (70000000 = tot space - "/".size)
need = fs[0].size() - 40000000
candidate = fs[0]
for f in fs:
    if type(f.c) == int:
        continue
    elif f.size() < need:  # > 100000:
        continue
    # totall += f.size()
    # print(f.n, f.size())
    if f.size() < candidate.size():
        candidate = f
print(candidate.n, candidate.size())
# print(totall)
# delete a dir, total spoace = 70,000,000, for update need 30,000,000
# find smallest directory whose deletion would leave enough space for upd
