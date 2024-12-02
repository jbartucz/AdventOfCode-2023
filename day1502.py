# when you download or copy the puzzle input,
# MAKE SURE TO USE THE CORRECT FILE NAME TO SAVE IT AND READ IT IN!

# open the file and read in the lines
chars = []
with open("day15.txt", "r") as f:
    for line in f:
        chars = line.strip().split(",")

boxes = [[] for _ in range(256)]


def hashit(chars):
    val = 0

    label = ""
    s = chars.split("=")
    if len(s) == 2:
        label = s[0]
    else:
        label = chars[:-1]

    for ch in label:
        val += ord(ch)
        val *= 17
        val %= 256

    if len(s) == 2:
        found = False
        for i, (l, f) in enumerate(boxes[val]):
            if l == label:
                boxes[val][i] = (s[0], int(s[1]))
                found = True
                break
        if found == False:
            boxes[val].append((s[0], int(s[1])))
    else:
        for i, (l, f) in enumerate(boxes[val]):
            if l == label:
                boxes[val] = boxes[val][0:i] + boxes[val][i+1:]
                break
    return val


for c in chars:
    val = hashit(c)

tot = 0
for i, b in enumerate(boxes):
    for j, (l, f) in enumerate(b):
        tot += (i + 1) * (j + 1) * f

print(tot)
