
# open the file and read in the lines
lines = []
rules = True
parts = list()
flows = dict()

with open("day19.txt", "r") as f:
    for line in f:
        if len(line.strip()) == 0:
            rules = False
            continue

        if rules == True:
            name, flow = line.strip()[:-1].split("{")
            flow = flow.split(",")
            flows[name] = flow
        else:
            part = dict()
            pt = (line.strip()[1:-1].split(","))
            for p in pt:
                part[p.split("=")[0]] = int(p.split("=")[1])
            parts.append(part)

        lines.append(line.strip())


def checkpart(part, rule):
    # print(part, rule)
    for r in rule:
        if ":" in r:
            r, nxt = r.split(":")
            if r[0] in "xmas":
                if r[1] == '<' and part[r[0]] < int(r[2:]):
                    # print(f"{r[1]} == '<' and {part[r[0]]} < {int(r[2:])}")
                    if nxt == "A":
                        return "A"
                    elif nxt == "R":
                        return "R"
                    else:
                        return checkpart(part, flows[nxt])
                if r[1] == '>' and part[r[0]] > int(r[2:]):
                    # print(f"{r[1]} == '>' and {part[r[0]]} > {int(r[2:])}")
                    if nxt == "A":
                        return "A"
                    elif nxt == "R":
                        return "R"
                    else:
                        return checkpart(part, flows[nxt])
        elif r == "A":
            return "A"
        elif r == "R":
            return "R"
        else:
            return checkpart(part, flows[r])


result = ""
tot = 0
for part in parts:
    cp = checkpart(part, flows["in"])
    if cp == "A":
        tot += part["x"] + part["m"] + part["a"] + part["s"]

print(tot)
