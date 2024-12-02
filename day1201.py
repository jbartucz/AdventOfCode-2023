# when you download or copy the puzzle input,
# MAKE SURE TO USE THE CORRECT FILE NAME TO SAVE IT AND READ IT IN!

# open the file and read in the lines
lines = []
places = []
with open("day12.txt", "r") as f:
    for line in f:
        l, t = line.strip().split()
        lines.append([i for i in l])
        places.append([int(i) for i in t.split(",")])


def test(line, nums):
    # print("TESTING:", line, nums)
    lst = line.split()
    valid = True
    if len(lst) != len(nums):
        return False
    for i, n in enumerate(lst):
        if len(lst[i]) != nums[i]:
            return False
    # print("* VALID *")
    return True


def donext(i):

    if "?" in lines[i]:
        totl = 0
        nextq = lines[i].index("?")
        lines[i][nextq] = "#"
        totl += donext(i)
        lines[i][nextq] = "."
        totl += donext(i)
        lines[i][nextq] = "?"
        return totl
    else:
        if test("".join(lines[i]).replace(".", " "), places[i]):
            return 1
        else:
            return 0


tot = 0
for i in range(len(lines)):
    tot += donext(i)


print(tot)
