# create an empty list of lines
lines = []

# open the file and read in the lines
# when you download or copy the puzzle input,
# MAKE SURE TO USE THE CORRECT FILE NAME TO SAVE IT AND READ IT IN!
with open("day02.txt", "r") as f:
    for line in f:
        lines.append(line.split())

# print out the lines to make sure it's correct
total = 0
for line in lines:
    min = {"red": 0,
           "green": 0,
           "blue": 0}

    for i in range(2, len(line), 2):
        # print(line[i], line[i+1].strip(";,"))
        if int(line[i]) > min[line[i+1].strip(";,")]:
            # print(line[i+1].strip(";,"), line[i])
            min[line[i+1].strip(";,")] = int(line[i])
    # print(min)
    total += min["red"] * min["blue"] * min["green"]

print(total)
