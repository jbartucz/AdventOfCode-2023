# when you download or copy the puzzle input,
# MAKE SURE TO USE THE CORRECT FILE NAME TO SAVE IT AND READ IT IN!

# open the file and read in the lines
lines = []
with open("day00.txt", "r") as f:
    for line in f:
        lines.append(line.strip())

# print out the lines to make sure it's correct
for line in lines:
    print(line)
