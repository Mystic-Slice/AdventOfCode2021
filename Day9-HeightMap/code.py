from collections import deque
with open("input.txt", "r") as f:
    inputs = [line.strip() for line in f]

grid = []
for line in inputs:
    dummy = [int(x) for x in list(line)]
    grid.append(dummy)

taken = []
for x in grid:
    dummy = []
    for y in x:
        dummy.append(False)
    taken.append(dummy)

def getNeighbours(grid, currx, curry):
    neighbours = []
    if currx > 0:
        neighbours.append([currx-1, curry])
    if curry > 0:
        neighbours.append([currx, curry-1])
    if currx < len(grid)-1:
        neighbours.append([currx+1, curry])
    if curry < len(grid[0])-1:
        neighbours.append([currx, curry+1])
    return neighbours

def findRisk(grid, x, y):
    dip = True
    neighbours = getNeighbours(grid, x, y)
    for nx, ny in neighbours:
        dip *= grid[nx][ny] > grid[x][y]
    return grid[x][y]+1 if dip else 0

def markBasin(grid, x, y):
    global taken
    q = deque()
    q.append([x,y])
    taken[x][y] = True
    res = 0
    while len(q):
        currx, curry = q.pop()
        if(grid[currx][curry] == 9):
            continue
        neighbours = getNeighbours(grid, currx, curry)
        for nx, ny in neighbours:
            if not taken[nx][ny]:
                q.append([nx, ny])
                taken[nx][ny] = True
        res += 1
    return res

totalRisk = 0
ans = []
for i in range(len(grid)):
    for j in range(len(grid[0])):
        risk = findRisk(grid, i, j)
        if risk:
            totalRisk += findRisk(grid, i, j)
            ans.append(markBasin(grid, i, j))

ans = sorted(ans)
final = 1
for x in ans[-3:]:
    final *= x

print("Part1: ", totalRisk)
print("Part2: ", final)





