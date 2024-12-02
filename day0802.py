from math import lcm
directions = ""
# open the file and read in the lines

nodict = dict()
with open("day08.txt", "r") as f:
    for line in f:
        if len(set([i for i in line.strip()])) == 2:
            directions = line.strip()
        elif len(line) > 1:
            node, edges = line.strip().split(" = ")
            edgetuple = edges.split("(")[1].split(")")[0].split(", ")

            nodict[node] = dict()
            nodict[node]["L"] = edgetuple[0]
            nodict[node]["R"] = edgetuple[1]

startlist = []
for k in nodict.keys():
    if k[-1] == "A":
        startlist.append(k)

stepslist = []
for i, here in enumerate(startlist):
    steps = 0
    while here[-1] != 'Z':
        for d in directions:
            here = nodict[here][d]
            steps += 1
            if here[-1] == 'Z':
                stepslist.append(steps)
                break


print("***", stepslist)
print(lcm(*stepslist))
