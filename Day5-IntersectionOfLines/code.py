with open("input.txt") as f:
    inputs = [x.strip() for x in f]

lines = []


for line in inputs:
    points = line.split(" -> ")
    x1, y1 = [int(x) for x in points[0].split(",")]
    x2, y2 = [int(x) for x in points[1].split(",")]
    lines.append([x1, y1, x2, y2])

mnx, mny, mxx, mxy = lines[0]

for point in lines:
    mnx = min(point[0], point[2], mnx)
    mxx = max(point[2], point[0], mxx)
    mny = min(point[1], point[3], mny)
    mxy = max(point[3], point[1], mxy)

dp1 = []
dp2 = []
for i in range(mxx-mnx+1):
    dummy = []
    for j in range(mxy-mny+1):
        dummy.append(0);
    dp1.append(dummy)

for i in range(mxx-mnx+1):
    dummy = []
    for j in range(mxy-mny+1):
        dummy.append(0);
    dp2.append(dummy)

def addLine(point, arr):
    x1, y1, x2, y2 = point
    diffx = 1 if x2 > x1 else 0 if x2 == x1 else -1
    diffy = 1 if y2 > y1 else 0 if y2 == y1 else -1
    while(True):
        arr[x1-mnx][y1-mny] += 1
        if(x1 == x2 and y1 == y2):
            break
        x1 += diffx
        y1 += diffy

for line in lines:
    if(line[0] == line[2] or line[1]==line[3]):
        addLine(line, dp1)
    addLine(line, dp2)

cnt1 = 0
for row in dp1:
    for x in row:
        if x >= 2:
            cnt1 += 1
        # print(x, end=" ")
    # print()

print("Part1: ", cnt1)

cnt2 = 0
for row in dp2:
    for x in row:
        if x >= 2:
            cnt2 += 1
        # print(x, end=" ")
    # print()

print("Part2: ", cnt2)