# create an empty list of lines
lines = []

# open the file and read in the lines
# when you download or copy the puzzle input,
# MAKE SURE TO USE THE CORRECT FILE NAME TO SAVE IT AND READ IT IN!
with open("day01.txt", "r") as f:
    for line in f:
        lines.append(line.strip())

# print out the lines to make sure it's correct
total = 0
for line in lines:
    first = -1
    last = -1
    for c in line:
        if c.isdigit():
            if first == -1:
                first = int(c)
            last = int(c)
    total += first * 10 + last

print(total)
