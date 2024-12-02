from collections import defaultdict

# create an empty list of lines
lines = []
print("starting")
with open("day05.txt", "r") as f:
    for line in f:
        lines.append(line.strip())

seedseeds = [int(i) for i in lines[0].split(":")[1].split()]
print(seedseeds)


maps = dict()
names = []
for i, line in enumerate(lines):
    if "map" in line:
        name = line.split()[0]
        # print(name)
        names.append(name)
        maps[name] = []
        for nums in lines[i+1:]:
            if len(nums) == 0:
                break
            maps[name].append([int(k) for k in nums.split()])
            # print(maps[name])

minloc = 99999999999999
dones = dict()
for name in names:
    dones[name] = set()
for i, start in enumerate(seedseeds):
    print("starting: ", i)
    if i % 2 == 0:
        for seed in range(start, start + seedseeds[i+1]):
            for name in names:
                if seed in dones[name]:
                    print("done")
                    break
                else:
                    dones[name].add(seed)
                for map in maps[name]:
                    if seed >= map[1] and seed < map[1] + map[2]:
                        # print("yes")
                        seed = map[0] + (seed - map[1])
                        # print(seed)
                        break
            if seed < minloc:
                minloc = seed


print(minloc)
