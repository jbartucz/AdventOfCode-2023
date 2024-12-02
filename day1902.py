
flows = dict()

with open("day19.txt", "r") as f:
    rules = True
    for line in f:
        if len(line.strip()) == 0:
            rules = False

        if rules == True:
            name, flow = line.strip()[:-1].split("{")
            flow = flow.split(",")
            t = dict()
            for f in flow:
                if "<" in f or ">" in f:
                    f, nxt = f.split(":")
                    t[f[0]] = (f[1], int(f[2:]), nxt)
                else:
                    t["def"] = f
            flows[name] = t


vals = dict()
vals["A"] = 1
vals["R"] = 0


def checkpart(rulename):
    # print(part, rule)
    tot = 0
    if rulename in vals:
        return vals[rulename]

    rule = flows[rulename]

    tot = 0
    mult = 1
    for letter in "xmas":
        if letter not in rule:
            mult *= 4000
            continue

        if rule[letter][0] == "<":
            tot += mult * (rule[letter][1] - 1) * checkpart(rule[letter][2])
            mult *= 4000 - rule[letter][1]
        else:
            tot += mult * (4000 - rule[letter][1]) * checkpart(rule[letter][2])
            mult *= rule["x"][1] - 1

    if "def" in rule:
        tot += mult * checkpart(rule["def"][0])

    return tot


print(flows)
print(checkpart("in"))
