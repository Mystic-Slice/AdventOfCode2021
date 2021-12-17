with open("input.txt", "r") as f:
    inputs = [line.strip() for line in f]

inputs = inputs[0][13:]

xRange, yRange = inputs.split(", ")

xRange = xRange[2:]
yRange = yRange[2:]

xRange = [int(x) for x in xRange.split("..")]
yRange = [int(x) for x in yRange.split("..")]

def withinRange(x, y):
    return xRange[0] <= x <= xRange[1] and yRange[0] <= y <= yRange[1]

def throw(vx, vy):
    x, y = 0, 0
    while x<=xRange[1] and y >= yRange[0]:
        x, y = x + vx, y + vy
        if withinRange(x, y):
            return True
        vx = vx-1 if vx > 0 else 0
        vy -= 1
    return False

maxHeight = 0
num = 0
for vx in range(xRange[1]+1):
    for vy in range(-1000, 1000):
        valid = throw(vx,vy)
        if valid:
            maxHeight = max(vy*(vy+1)/2, maxHeight)
            num += 1

print("Part1: ", int(maxHeight))
print("Part2: ", num)
