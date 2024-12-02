# create an empty list of lines
lines = []
with open("day05.txt", "r") as f:
    for line in f:
        lines.append(line.strip())

seedseeds = [int(i) for i in lines[0].split(":")[1].split()]

maps = dict()
names = []
for i, line in enumerate(lines):
    if "map" in line:
        name = line.split()[0]
        names.append(name)
        maps[name] = []
        for nums in lines[i+1:]:
            if len(nums) == 0:
                break
            maps[name].append([int(k) for k in nums.split()])


start = 1
done = False
names.reverse()  # LOLOLOL
while done == False:
    seed = start
    for name in names:
        for map in maps[name]:
            if seed >= map[0] and seed < map[0] + map[2]:
                seed = map[1] + (seed - map[0])
                break

    for i in range(0, 10, 2):
        # print(seedseeds[i], seedseeds[i] + seedseeds[i+1])
        if seed >= seedseeds[i] and seed < seedseeds[i] + seedseeds[i+1]:
            print("start:", start)
            done = True
            break

    start += 1
