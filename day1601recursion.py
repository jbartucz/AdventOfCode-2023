# when you download or copy the puzzle input,
# MAKE SURE TO USE THE CORRECT FILE NAME TO SAVE IT AND READ IT IN!

# open the file and read in the lines
lines = []
with open("day16.txt", "r") as f:
    for line in f:
        lines.append([i for i in line.strip()])


# last spot, current spot [line#][col#]
ens = set()
dones = set()


def ray(l, c):
    s = lines[c[0]][c[1]]

    if (l, c) in dones:
        return
    else:
        dones.add((l, c))
    ens.add(s)
    if s == ".":
        if l[1] == c[1] - 1:  # coming from the left
            if c[1] < len(lines[0]) - 1:  # pass through
                ray(c, (c[0], c[1]+1))
        elif l[1] == c[1] + 1:  # coming from the right
            if c[1] > 0:  # pass through
                ray(c, (c[0], c[1]-1))
        elif l[0] == c[0] - 1:  # coming from the top
            if c[0] < len(lines) - 1:  # pass through
                ray(c, (c[0]+1, c[1]))
        elif l[0] == c[0] + 1:  # coming from the bottom
            if c[0] > 0:  # pass through
                ray(c, (c[0]-1, c[1]))
        return
    elif l[1] == c[1] - 1:  # coming from the left
        if s == '-':
            if c[1] < len(lines[0]) - 1:  # pass through
                ray(c, (c[0], c[1]+1))
        if s == '|':
            if c[0] > 0:  # go up
                ray(c, (c[0] - 1, c[1]))
            if c[0] < len(lines) - 1:  # go down
                ray(c, (c[0] + 1, c[1]))
        if s == '/':
            if c[0] > 0:  # go up
                ray(c, (c[0] - 1, c[1]))
        if s == '\\':
            if c[0] < len(lines) - 1:  # go down
                ray(c, (c[0] + 1, c[1]))
    elif l[1] == c[1] + 1:  # coming from the right
        if s == '-':
            if c[1] > 0:  # pass through
                ray(c, (c[0], c[1]-1))
        if s == '|':
            if c[0] > 0:  # go up
                ray(c, (c[0] - 1, c[1]))
            if c[0] < len(lines) - 1:  # go down
                ray(c, (c[0] + 1, c[1]))
        if s == '\\':
            if c[0] > 0:  # go up
                ray(c, (c[0] - 1, c[1]))
        if s == '/':
            if c[0] < len(lines) - 1:  # go down
                ray(c, (c[0] + 1, c[1]))
    elif l[0] == c[0] - 1:  # coming from the top
        if s == '|':
            if c[0] < len(lines) - 1:  # pass through
                ray(c, (c[0]+1, c[1]))
        if s == '-':
            if c[1] > 0:  # go left
                ray(c, (c[0], c[1]-1))
            if c[1] < len(lines[0]) - 1:  # go right
                ray(c, (c[0], c[1] + 1))
        if s == '/':
            if c[1] > 0:  # go left
                ray(c, (c[0], c[1]-1))
        if s == '\\':
            if c[1] < len(lines[0]) - 1:  # go right
                ray(c, (c[0], c[1]+1))
    elif l[0] == c[0] + 1:  # coming from the bottom
        if s == '|':
            if c[0] > 0:  # pass through
                ray(c, (c[0]-1, c[1]))
        if s == '-':
            if c[1] > 0:  # go left
                ray(c, (c[0], c[1]-1))
            if c[1] < len(lines[0]) - 1:  # go right
                ray(c, (c[0], c[1] + 1))
        if s == '/':
            if c[1] > 0:  # go right
                ray(c, (c[0], c[1]+1))
        if s == '\\':
            if c[1] < len(lines[0]) - 1:  # go left
                ray(c, (c[0], c[1]-1))


ray((0, -1), (0, 0))

for line in lines:
    print("".join(line))

print(len(ens))
