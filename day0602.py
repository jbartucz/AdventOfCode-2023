
races = [(51926890, 222203111261225)]

totalnumwins = 1
for race in races:
    numwins = 0
    for i in range(race[0]):
        # speed(num charge secs) * time
        if i * (race[0]-i) > race[1]:  # breaks the record
            # print("win:", i, race[0], i * (race[0]-i))
            numwins += 1
    # print(numwins)
    totalnumwins *= numwins

print(totalnumwins)
