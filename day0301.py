# create an empty list of lines
lines = []

# open the file and read in the lines
# when you download or copy the puzzle input,
# MAKE SURE TO USE THE CORRECT FILE NAME TO SAVE IT AND READ IT IN!
with open("day03.txt", "r") as f:
    for line in f:
        lines.append(line.strip())

total = 0
for count, line in enumerate(lines):
    begin = -1
    num = 0
    for i in range(len(line)):
        if line[i].isdigit():
            if begin == -1:
                begin = i
            num = num * 10 + int(line[i])
        if not line[i].isdigit() or i == len(line) - 1:
            if begin > -1:  # must be the end of a number
                # check if there's a sybol around it
                print(count, i, line[i], "end of a number", num)
                for k in range(max(0, count - 1), min(len(lines), count + 2)):
                    for j in range(max(0, begin - 1), min(len(line), i+1)):
                        print("check:", k, j, lines[k][j])
                        if not lines[k][j].isdigit() and lines[k][j] != '.':
                            print(begin, i, count,
                                  lines[k][j], "adding: ", num)
                            total += num
                            num = 0
                # reset for the next number
                begin = -1
                num = 0
            # else:
                # print(count, i, line[i], "not in a number")

print(total)
