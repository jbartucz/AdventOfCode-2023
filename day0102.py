lines = []
with open("day01.txt", "r") as f:
    for line in f:
        lines.append(line.strip())

total = 0
for line in lines:
    first = -1
    last = -1
    for n in range(0, len(line)):
        if line[n].isdigit():
            if first == -1:
                first = int(line[n])
            last = int(line[n])
        else:
            if line[n:n+3] == "one":
                if first == -1:
                    first = 1
                last = 1
            elif line[n:n+3] == "two":
                if first == -1:
                    first = 2
                last = 2
            elif line[n:n+5] == "three":
                if first == -1:
                    first = 3
                last = 3
            elif line[n:n+4] == "four":
                if first == -1:
                    first = 4
                last = 4
            elif line[n:n+4] == "five":
                if first == -1:
                    first = 5
                last = 5
            elif line[n:n+3] == "six":
                if first == -1:
                    first = 6
                last = 6
            elif line[n:n+5] == "seven":
                if first == -1:
                    first = 7
                last = 7
            elif line[n:n+5] == "eight":
                if first == -1:
                    first = 8
                last = 8
            elif line[n:n+4] == "nine":
                if first == -1:
                    first = 9
                last = 9

    total += first * 10 + last

print(total)
