# create an empty list of lines
lines = []
with open("day05.txt", "r") as f:
    for line in f:
        lines.append(line.strip())

seeds = [int(i) for i in lines[0].split(":")[1].split()]
# print(seeds)

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

locations = []
for seed in seeds:
    for name in names:
        # print(seed, name, maps[name])
        for map in maps[name]:
            if seed >= map[1] and seed < map[1] + map[2]:
                # print("yes")
                seed = map[0] + (seed - map[1])
                # print(seed)
                break
    locations.append(seed)

print(locations)
print(min(locations))
