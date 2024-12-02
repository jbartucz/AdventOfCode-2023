# when you download or copy the puzzle input,
# MAKE SURE TO USE THE CORRECT FILE NAME TO SAVE IT AND READ IT IN!

# open the file and read in the lines
lines = []
origlines = []
with open("day10.txt", "r") as f:
    for line in f:
        # print(line.strip())
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
            print("*** Illegal Character ***")

# print(start)

# create the path
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

# clean up (just for debugging)
for i in range(len(lines)):
    for j in range(len(lines[0])):
        if (i, j) not in path:
            origlines[i][j] = "."

# fix "S"
o = origlines
(i, j) = start
if o[i][j+1] in ["7", "J", "-"]:  # east
    if o[i][j-1] in ["L", "F", "-"]:  # west
        origlines[i][j] = "-"
    elif o[i+1][j] in ["L", "J", "|"]:  # south
        origlines[i][j] = "F"
    elif o[i-1][j] in ["7", "F", "|"]:  # north
        origlines[i][j] = "L"
elif o[i+1][j] in ["L", "J", "|"]:  # south
    if o[i][j-1] in ["L", "F", "-"]:  # west
        origlines[i][j] = "7"
    elif o[i-1][j] in ["7", "F", "|"]:  # north
        origlines[i][j] = "|"
elif o[i][j-1] in ["L", "F", "-"]:  # west
    if o[i-1][j] in ["7", "F", "|"]:  # north
        origlines[i][j] = "J"


# for l in origlines:
#     print("".join(l))

# use rays, ignoring horizontal lines
insides = 0
for i in range(len(lines)):
    crosses = 0
    fromdir = ""
    for j in range(0, len(lines[0])):
        c = origlines[i][j]
        if c == "|":
            crosses += 1
        elif c == "L":
            fromdir = "up"
        elif c == "F":
            fromdir = "down"
        elif c == "7" and fromdir == "up":
            crosses += 1
        elif c == "J" and fromdir == "down":
            crosses += 1
        elif c == ".":
            if crosses % 2 == 1:  # odd
                insides += 1
                origlines[i][j] = "*"

print(insides)
