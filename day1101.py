# when you download or copy the puzzle input,
# MAKE SURE TO USE THE CORRECT FILE NAME TO SAVE IT AND READ IT IN!

# open the file and read in the lines
lines = []
with open("day11.txt", "r") as f:
    for line in f:
        l = [i for i in line.strip()]
        lines.append(l)
        if len(set(l)) == 1:
            lines.append(list(l)) # add empty rows

# find the empty columns
locs = list()
for i in range(len(lines[0])):
    alldots = True
    for l in lines:
        if l[i] != '.':
            alldots = False
            break
    if alldots == True:
        locs.insert(0,i)

# expand the columns
for i in range(len(lines)):
    for j in locs:
        lines[i].insert(j,'.')


# find the stars
stars = set()
for i, l in enumerate(lines):
    for j, c in enumerate(l):
        if c == "#":
            stars.add((i,j))

# count the differences
tot = 0
sts = set(stars)
for s in stars:
    for t in sts:
        dist = abs(s[0] - t[0]) + abs(s[1] - t[1])
        tot += dist
    sts.remove(s)

print(tot)
        
