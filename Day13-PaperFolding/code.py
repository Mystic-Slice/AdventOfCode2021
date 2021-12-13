with open("input.txt", "r") as f:
    inputs = [line.strip() for line in f]

grid = []

pointInputs = [line for line in inputs if "," in line]
foldInputs = [line for line in inputs if "=" in line]

mxx= 0
mxy = 0

def printGrid(grid):
    for x in grid:
        for y in x:
            char = "#" if y else "."
            print(char, end="")
        print()

for line in pointInputs:
    x, y = [int(x) for x in line.split(",")]
    mxx = max(mxx, x)
    mxy = max(mxy, y)

for i in range(mxy+1):
    dummy = []
    for j in range(mxx+1):
        dummy.append(0)
    grid.append(dummy)

for line in pointInputs:
    x, y = [int(x) for x in line.split(",")]
    grid[y][x] = 1

def foldAlongY(y, grid):
    
    up = grid[:y]
    down = grid[y+1:]

    heightNew = max(len(up), len(down))
    newGrid = [[0 for x in range(len(grid[0]))] for i in range(heightNew)]
    flipDown = []
    for x in down:
       flipDown = [x] + flipDown 

    for y in range(len(up)):
        for x in range(len(grid[0])):
            newGrid[y][x] |= up[y][x]

    for y in range(len(flipDown)):
         for x in range(len(grid[0])):
             newGrid[y][x] |= flipDown[y][x]

    return newGrid


def foldAlongX(x, grid):

    left = [lst[:x] for lst in grid]
    right = [lst[x+1:] for lst in grid]
    
    widthNew = max(len(left[0]), len(right[0]))
    newGrid = [[0 for x in range(widthNew)] for i in range(len(grid))]

    flipRight = []
    for row in right:
        dummy = []
        for i in range(len(row)):
            index = len(row)-i-1
            dummy.append(row[index])
        flipRight.append(dummy)

    for i in range(len(grid)):
        for j in range(len(left[0])):
            newGrid[i][j] |= left[i][j]

    for i in range(len(grid)):
         for j in range(len(flipRight[0])):
             newGrid[i][j] |= flipRight[i][j]

    return newGrid

def countDots(grid):
    cnt = 0
    for x in grid:
        cnt += sum(x)
    return cnt

numDots = []
for line in foldInputs:
    line = line.split()
    direction, index = line[2].split("=")
    if(direction == "x"):
        grid = foldAlongX(int(index), grid)
    if(direction == "y"):
        grid = foldAlongY(int(index), grid)
    numDots.append(countDots(grid))

print("Part1: ", numDots[0])
print("Part2: ")
printGrid(grid)
