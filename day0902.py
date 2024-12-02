# when you download or copy the puzzle input,
# MAKE SURE TO USE THE CORRECT FILE NAME TO SAVE IT AND READ IT IN!

# open the file and read in the lines
lines = []
with open("day09.txt", "r") as f:
    for line in f:
        lines.append([int(i) for i in line.strip().split()])


def addend(line):
    if len(set(line)) == 1:  # if they're all the same #, return that number
        return line[0]
    nextline = []
    for i in range(len(line)-1):
        nextline.append(line[i+1]-line[i])
    nextval = line[0] - addend(nextline)  # subtract from the first for part 2
    # print(line, nextval)
    return nextval


total = 0
for line in lines:
    total += addend(line)

print(total)
