# when you download or copy the puzzle input,
# MAKE SURE TO USE THE CORRECT FILE NAME TO SAVE IT AND READ IT IN!

# open the file and read in the lines
lines = []
origlines = []
with open("day10.txt", "r") as f:
    for line in f:
        print(line.strip())
        lines.append([i for i in line.strip()])
        origlines.append([i for i in line.strip()])


start = ()
for i, line in enumerate(lines):
    for j, c in enumerate(line):
        if c == "|":
            lines[i][j] = ("N", "S")
        elif c == "-":
            lines[i][j] = ("E", "W")
        elif c == "L":
            lines[i][j] = ("N", "E")
        elif c == "J":
            lines[i][j] = ("N", "W")
        elif c == "7":
            lines[i][j] = ("S", "W")
        elif c == "F":
            lines[i][j] = ("E", "S")
        elif c == ".":
            lines[i][j] = ()
        elif c == "S":
            start = (i, j)
            lines[i][j] = []
            if i > 0 and lines[i-1][j] in ["|", "7", "F"]:
                lines[i][j].append("N")
            if i < len(lines) - 1 and lines[i+1][j] in ["|", "L", "J"]:
                lines[i][j].append("S")
            if j > 0 and lines[i][j-1] in ["-", "L", "F"]:
                lines[i][j].append("W")
            if j < len(line) - 1 and lines[i][j+1] in ["-", "7", "J"]:
                lines[i][j].append("E")
        else:
            print("ASDFASDFASDFASDFASDFASDFASDFASDFASDF")

print(start)

here = start
last = start
nxt = ()
path = set()
while nxt != start:
    path.add(here)
    if "N" in lines[here[0]][here[1]] and last[0] != here[0] - 1:
        nxt = (here[0] - 1, here[1])
    elif "S" in lines[here[0]][here[1]] and last[0] != here[0] + 1:
        nxt = (here[0] + 1, here[1])
    elif "E" in lines[here[0]][here[1]] and last[1] != here[1] + 1:
        nxt = (here[0], here[1]+1)
    elif "W" in lines[here[0]][here[1]] and last[1] != here[1] - 1:
        nxt = (here[0], here[1]-1)
    last = here
    here = nxt

start = ()
insides = set()
done = False
for i in range(len(lines) + 1):
    if done == True:
        break
    for j in range(len(lines[0]) + 1):
        if (i, j) in path and (i, j-1) not in path and (i, j+1) not in path:
            start = (i, j+1)  # find somewhere to start
            insides.add(start)
            done = True
            break


def checkall(st):
    if st[0] > 0:
        if (st[0]-1, st[1]) not in path and (st[0]-1, st[1]) not in insides:
            insides.add((st[0]-1, st[1]))
            checkall((st[0]-1, st[1]))
    if st[1] > 0:
        if (st[0], st[1]-1) not in path and (st[0], st[1]-1) not in insides:
            insides.add((st[0], st[1]-1))
            checkall((st[0], st[1]-1))
    if st[0] < len(lines[0]) - 1:
        if (st[0]+1, st[1]) not in path and (st[0]+1, st[1]) not in insides:
            insides.add((st[0]+1, st[1]))
            checkall((st[0]+1, st[1]))
    if st[1] < len(lines) - 1:
        if (st[0], st[1]+1) not in path and (st[0], st[1]+1) not in insides:
            insides.add((st[0], st[1]+1))
            checkall((st[0], st[1]+1))


checkall(start)


print(len(insides))
