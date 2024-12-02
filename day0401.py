lines = []
with open("day04.txt", "r") as f:
    for line in f:
        lines.append(line.strip())

sum = 0
for line in lines:
    card = int(line.split(":")[0][5:])
    winners = line.split(":")[1].split("|")[0].split()
    mynums = line.split(":")[1].split("|")[1].split()
    lineexp = -1
    for i in mynums:
        if i in winners:
            lineexp += 1

    if lineexp >= 0:
        sum += 2 ** lineexp

print(sum)
