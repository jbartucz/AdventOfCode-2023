
def checkmirror(lines):
    # try to match vertical starting with the bottom line and moving down from the top
    bottomline = lines[len(lines)-1]
    top = -1
    bottom = len(lines) - 1
    for i in range(len(lines) - 1):
        if (bottom - i) % 2 == 0:
            continue
        if lines[i] == bottomline:
            top = i  # start testing the rest of the match
            for j in range(bottom - i):
                if lines[i + j] != lines[bottom - j]:
                    top = -1  # mismatch
                    break
            if top == i:  # if we get to the middle and there was no mismatch
                break
    if top != -1:
        return (top, bottom)

    return (-1, -1)


def getreflects(lines):

    cols = list()
    for i in range(len(lines[0])):
        cols.append("")
    for l in lines:
        for i, c in enumerate(l):
            cols[i] += c

    (top, bottom) = checkmirror(lines)
    if top != -1:
        print("l1:", top)
        return 100 * ((bottom - top + 1) / 2 + top)

    lines.reverse()
    (top, bottom) = checkmirror(lines)
    if top != -1:
        print("l2:", top)
        return 100 * ((bottom - top + 1) / 2 + top)

    (top, bottom) = checkmirror(cols)
    if top != -1:
        print("c1:", top)
        return (bottom - top + 1) / 2 + top

    cols.reverse()
    (top, bottom) = checkmirror(cols)
    if top != -1:
        print("l2:", top)
        return (bottom - top + 1) / 2 + top

    print("*** well, fuck ***")

    # print("\n".join(lines))
    # print()
    # print("\n".join(cols))

    return 0


# open the file and read in the lines
with open("day13.txt", "r") as f:
    lines = []
    total = 0
    for line in f:
        if len(line.strip()) == 0:
            gl = getreflects(lines)
            print("-", gl)
            total += gl
            lines = []
        else:
            lines.append(line.strip())

print(total)
