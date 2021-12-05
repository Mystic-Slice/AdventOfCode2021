with open("input.txt", "r") as f:
    inputs = [line.strip() for line in f]

xcoord = 0
ycoord1 = 0
ycoord2 = 0
aim = 0
for command in inputs:
    direction, magnitude = command.split()
    magnitude = int(magnitude)

    if direction == "forward":
        xcoord += magnitude
        ycoord2 += aim*magnitude
    elif direction == "down":
        ycoord1 += magnitude
        aim += magnitude
    elif direction == "up":
        ycoord1 -= magnitude
        aim -= magnitude
    else:
        raise RuntimeError("Unknown direction") from None

print("Part1: ", ycoord1*xcoord)
print("Part2: ", ycoord2*xcoord)
