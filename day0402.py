lines = []
with open("day04.txt", "r") as f:
    for line in f:
        lines.append(line.strip())

numcards = [1 for i in range(len(lines))]
print(numcards)

for line in lines:
    card = int(line.split(":")[0][5:])
    winners = line.split(":")[1].split("|")[0].split()
    mynums = line.split(":")[1].split("|")[1].split()
    cards = 0
    for i in mynums:
        if i in winners:
            cards += 1

    for i in range(cards):
        numcards[card + i] += numcards[card - 1]

print(numcards)

total = 0
for i in numcards:
    total += i
print(total)
