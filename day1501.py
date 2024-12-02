# when you download or copy the puzzle input,
# MAKE SURE TO USE THE CORRECT FILE NAME TO SAVE IT AND READ IT IN!

# open the file and read in the lines
chars = []
with open("day15.txt", "r") as f:
    for line in f:
        chars = line.strip().split(",")


def hashit(chars):
    val = 0
    for ch in chars:
        val += ord(ch)
        val *= 17
        val %= 256
    return val


tot = 0
for c in chars:
    val = hashit(c)
    print(val)
    tot += val

print(tot)
