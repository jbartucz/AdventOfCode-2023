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
    max = {"red": 12,
           "green": 13,
           "blue": 14}
    game = int(line[1][0:-1])
    valid = True
    for i in range(2, len(line), 2):
        # print(line[i], line[i+1].strip(";,"))
        if int(line[i]) > max[line[i+1].strip(";,")]:
            print(line[i+1].strip(";,"), line[i])
            valid = False
    if valid == True:
        total += game

print(total)
