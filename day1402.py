# when you download or copy the puzzle input,
# MAKE SURE TO USE THE CORRECT FILE NAME TO SAVE IT AND READ IT IN!

# open the file and read in the lines
lines = []
with open("day14.txt", "r") as f:
    for line in f:
        lines.append([i for i in line.strip()])


for i in range(100):

    # north
    for k in range(len(lines)):
        for i in range(1, len(lines)):
            for j, c in enumerate(lines[i]):

                if c == "O" and lines[i-1][j] == '.':
                    lines[i-1][j] = 'O'
                    lines[i][j] = '.'

    # west
    for k in range(len(lines[0])):
        for j in range(1, len(lines[0])):
            for i in range(len(lines)):
                c = lines[i][j]

                if c == "O" and lines[i][j-1] == '.':
                    lines[i][j-1] = 'O'
                    lines[i][j] = '.'

    # south
    for k in range(len(lines)):
        for i in range(len(lines) - 2, -1, -1):
            for j, c in enumerate(lines[i]):

                if c == "O" and lines[i+1][j] == '.':
                    lines[i+1][j] = 'O'
                    lines[i][j] = '.'

    # east
    for k in range(len(lines[0])):
        for j in range(len(lines[0])-2, -1, -1):
            for i in range(len(lines)):
                c = lines[i][j]

                if c == "O" and lines[i][j+1] == '.':
                    lines[i][j+1] = 'O'
                    lines[i][j] = '.'

weight = 0
for i, l in enumerate(lines):
    weight += (len(lines) - i) * l.count("O")

print(weight)
