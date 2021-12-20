with open("input.txt", "r") as f:
    inputs = [line.strip() for line in f]
d = {'#':1, '.':0}
algo = [d[x] for x in inputs[0]]

grid = []
for line in inputs[2:]:
    dummy = [d[x] for x in line]
    grid.append(dummy)

def printGrid(grid):
    s = ''
    for x in grid:
        for c in x:
            if(c == 1):
                s += '#'
            else:
                s += '.'
        s += '\n'
    print(s)

def expandGrid(grid, char):
    for i in range(len(grid)):
        grid[i] = [char] + grid[i] + [char]
    grid = [[char for x in grid[0]]] + grid + [[char for x in grid[0]]]
    return grid

def getIndex(grid, x, y):
    s = ''
    for i in [-1,0,1]:
        for j in [-1, 0, 1]:
            s += str(grid[x+i][y+j])
    return s, int(s, 2)
    
def sumGrid(grid):
    return sum(sum(x) for x in grid)

def enhance(image, iteration):
    boundaryChars = 0
    if(iteration%2 and algo[0]):
        boundaryChars = 1
    res = expandGrid(expandGrid(image, boundaryChars), boundaryChars)
    finalImage = [x[:] for x in res]

    for i in range(1, len(res)-1):
        for j in range(1, len(res[0])-1):
            s, index = getIndex(res, i, j)
            finalImage[i][j] = algo[index]
    
    if(finalImage[0][0] == 0):
        index = 0
    else:
        index = 511
    for j in range(len(finalImage[0])):
        finalImage[0][j] = algo[index]
        finalImage[len(finalImage)-1][j] = algo[index]

    for i in range(len(finalImage)):
        finalImage[i][0] = algo[index]
        finalImage[i][len(finalImage[0])-1] = algo[index]

    return finalImage

steps = 2
grid1 = [x[:] for x in grid]
for i in range(steps):
    grid1 = enhance(grid1, i)

steps = 50
grid2 = [x[:] for x in grid]
for i in range(steps):
    grid2 = enhance(grid2, i)

print("Part1: ", sumGrid(grid1))
print("Part2: ", sumGrid(grid2))

