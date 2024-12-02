# when you download or copy the puzzle input,
# MAKE SURE TO USE THE CORRECT FILE NAME TO SAVE IT AND READ IT IN!

# open the file and read in the lines
lines, nums = [], []
with open("day12.txt", "r") as f:
    for line in f:
        l, t = line.strip().split()
        l = '.'+l+'.'  # so I don't have to check edges later on
        lines.append(l)
        print(l, t)
        nums.append([int(i) for i in t.split(",")])
        # break

# check whether we can fit list ns springs starting at position i


def checkline(line, ns, start):

    # minimum number of characters to fit all springs
    mincharsneeded = sum(ns) + len(ns) - 1

    tot = 0
    n = ns[0]

    # if there is a spring, we have to use it, otherwise go to the end of the line
    end = line.find("#", start, start+n)
    if end == -1:
        end = len(line)-mincharsneeded

    for i in range(start, end+1):

        # must fit exactly
        if "." in line[i:i+n]:
            continue  # doesn't fit
        elif line[i-1] == "#" or line[i+n] == "#":
            continue  # has # on either side
        elif len(ns) == 1:  # if we're on the last number
            if "#" not in line[i+n:]:  # make sure there are no leftover stars at the end
                print("*** IT FIT!!! at", i, "***", fits)
                tot += 1
        else:
            print("putting " + str(n) + " springs at " + str(i))
            testline = line[:i] + "#" * n + line[i + n:]
            print("testline:", testline)
            newstart = i + n + 1
            if len(ns) == 2:
                hashash = line.find("#", i + n + 1)
                if hashash != -1:
                    newstart = hashash

            print("checking " + str(ns[1:]) +
                  " starting at " + str(i + n + 1) + " ---> " + line[newstart:])
            tot += checkline(line, ns[1:], newstart)

    return tot


totallytotal = 0
for i, l in enumerate(lines):
    print("\nLINE:", l)
    linetotal = checkline(l, nums[i], 1)
    print("Line total: ", linetotal)

    totallytotal += linetotal


print(totallytotal)
