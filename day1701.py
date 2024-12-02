
# open the file and read in the lines
lines = []
with open("day17.txt", "r") as f:
    for line in f:
        lines.append([int(i) for i in line.strip()])

h = (0,0)
while h != (len(lines),len(lines[0])):
    