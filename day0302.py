# create an empty list of lines
lines = []

nums = []  # a list of the numbers and their locations

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

                nums.append((count, begin, i - 1, num))

                # reset for the next number
                begin = -1
                num = 0
            # else:
                # print(count, i, line[i], "not in a number")

for count, line in enumerate(lines):
    for i, c in enumerate(line):
        if c == '*':
            print("star at: ", count, i)
            starnums = set()
            for k in range(max(0, count - 1), min(len(lines), count + 2)):
                for j in range(max(0, i - 1), min(len(line), i+2)):
                    for num in nums:
                        # if the num is next to the star
                        if num[0] == k and j >= num[1] and j <= num[2]:
                            starnums.add(num)

            if len(starnums) == 2:
                mult = 1
                for starnum in starnums:
                    mult *= starnum[3]
                total += mult

print(total)
