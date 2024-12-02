# when you download or copy the puzzle input,
# MAKE SURE TO USE THE CORRECT FILE NAME TO SAVE IT AND READ IT IN!

# open the file and read in the lines
lines = []
with open("day10.txt", "r") as f:
    for line in f:
        print(line)
        lines.append([i for i in line.strip()])


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
steps = 0
while nxt != start:
    print(here)
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
    steps += 1

print(int(steps/2))
