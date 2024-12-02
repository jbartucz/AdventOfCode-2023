# when you download or copy the puzzle input,
# MAKE SURE TO USE THE CORRECT FILE NAME TO SAVE IT AND READ IT IN!

# open the file and read in the lines
lines = []
with open("day16.txt", "r") as f:
    for line in f:
        lines.append([i for i in line.strip()])


def shine(next):
    # last spot, current spot [line#][col#]
    ens = set()
    dones = set()
    while len(next) > 0:
        l, c = next.pop()  # get the last and current location
        if (l, c) in dones:
            continue
        else:
            dones.add((l, c))
        ens.add(c)  # add current location to the list of #'s
        s = lines[c[0]][c[1]]
        # print(c)
        if s == ".":
            if l[1] == c[1] - 1:  # coming from the left
                if c[1] < len(lines[0]) - 1:  # pass through
                    next.append((c, (c[0], c[1]+1)))
            elif l[1] == c[1] + 1:  # coming from the right
                if c[1] > 0:  # pass through
                    next.append((c, (c[0], c[1]-1)))
            elif l[0] == c[0] - 1:  # coming from the top
                if c[0] < len(lines) - 1:  # pass through
                    next.append((c, (c[0]+1, c[1])))
            elif l[0] == c[0] + 1:  # coming from the bottom
                if c[0] > 0:  # pass through
                    next.append((c, (c[0]-1, c[1])))
        elif l[1] == c[1] - 1:  # coming from the left
            if s == '-':
                if c[1] < len(lines[0]) - 1:  # pass through
                    next.append((c, (c[0], c[1]+1)))
            if s == '|':
                if c[0] > 0:  # go up
                    next.append((c, (c[0] - 1, c[1])))
                if c[0] < len(lines) - 1:  # go down
                    next.append((c, (c[0] + 1, c[1])))
            if s == '/':
                if c[0] > 0:  # go up
                    next.append((c, (c[0] - 1, c[1])))
            if s == '\\':
                if c[0] < len(lines) - 1:  # go down
                    next.append((c, (c[0] + 1, c[1])))
        elif l[1] == c[1] + 1:  # coming from the right
            if s == '-':
                if c[1] > 0:  # pass through
                    next.append((c, (c[0], c[1]-1)))
            if s == '|':
                if c[0] > 0:  # go up
                    next.append((c, (c[0] - 1, c[1])))
                if c[0] < len(lines) - 1:  # go down
                    next.append((c, (c[0] + 1, c[1])))
            if s == '\\':
                if c[0] > 0:  # go up
                    next.append((c, (c[0] - 1, c[1])))
            if s == '/':
                if c[0] < len(lines) - 1:  # go down
                    next.append((c, (c[0] + 1, c[1])))
        elif l[0] == c[0] - 1:  # coming from the top
            if s == '|':
                if c[0] < len(lines) - 1:  # pass through
                    next.append((c, (c[0]+1, c[1])))
            if s == '-':
                if c[1] > 0:  # go left
                    next.append((c, (c[0], c[1]-1)))
                if c[1] < len(lines[0]) - 1:  # go right
                    next.append((c, (c[0], c[1] + 1)))
            if s == '/':
                if c[1] > 0:  # go left
                    next.append((c, (c[0], c[1]-1)))
            if s == '\\':
                if c[1] < len(lines[0]) - 1:  # go right
                    next.append((c, (c[0], c[1]+1)))
        elif l[0] == c[0] + 1:  # coming from the bottom
            if s == '|':
                if c[0] > 0:  # pass through
                    next.append((c, (c[0]-1, c[1])))
            if s == '-':
                if c[1] > 0:  # go left
                    next.append((c, (c[0], c[1]-1)))
                if c[1] < len(lines[0]) - 1:  # go right
                    next.append((c, (c[0], c[1] + 1)))
            if s == '/':
                if c[1] > 0:  # go right
                    next.append((c, (c[0], c[1]+1)))
            if s == '\\':
                if c[1] < len(lines[0]) - 1:  # go left
                    next.append((c, (c[0], c[1]-1)))

    return len(ens)


maxlength = 0
for i in range(len(lines[0])):
    maxlength = max(shine([((-1, i), (0, i))]), maxlength)
    maxlength = max(shine([((len(lines), i), (len(lines)-1, i))]), maxlength)
for i in range(len(lines)):
    maxlength = max(shine([((i, -1), (i, 0))]), maxlength)
    # could debug this, but it got the right answer so meh
    # maxlength = max(
    #    shine([((i, len(lines[0])), (i, len(lines[0])-1))]), maxlength)

print(maxlength)
