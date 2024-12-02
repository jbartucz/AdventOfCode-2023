# when you download or copy the puzzle input,
# MAKE SURE TO USE THE CORRECT FILE NAME TO SAVE IT AND READ IT IN!

# open the file and read in the lines
lines = []
rows = set() # empty rows
with open("day11.txt", "r") as f:
    for r, line in enumerate(f):
        l = [i for i in line.strip()]
        lines.append(l)
        if len(set(l)) == 1:
            rows.add(r) # add empty rows

# find the empty columns
cols = set() # empty columns
for i in range(len(lines[0])):
    alldots = True
    for l in lines:
        if l[i] != '.':
            alldots = False
            break
    if alldots == True:
        cols.add(i)

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
        for r in rows:
            if r > s[0] and r < t[0] or r > t[0] and r < s[0]:
                dist += 999999
        for c in cols:
            if c > s[1] and c < t[1] or c > t[1] and c < s[1]:
                dist += 999999
        tot += dist
    sts.remove(s)

print(tot)
        
