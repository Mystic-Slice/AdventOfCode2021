with open("input.txt", "r") as f:
    inputs = [line.strip() for line in f]


octs = []

for line in inputs:
    octs.append([int(x) for x in line])

def printOcts(octs):
    for x in octs:
        print(x)

def increase(octs):

    for x in range(len(octs)):
        octs[x] = [e+1 for e in octs[x]]
    
    return octs

def getNeighbours(octs, x, y):
    neighbours = []
    if(x > 0):
        neighbours.append([x-1, y])
        if(y>0):
            neighbours.append([x-1, y-1])
        if(y<len(octs[0])-1):
            neighbours.append([x-1, y+1])

    if(x < len(octs)-1):
        neighbours.append([x+1, y])
        if(y>0):
            neighbours.append([x+1, y-1])
        if(y<len(octs[0])-1):
            neighbours.append([x+1, y+1])

    if(y>0):
        neighbours.append([x, y-1])
    if(y<len(octs[0])-1):
        neighbours.append([x, y+1])
    
    return neighbours

def increaseNeighbours(octs):
    change = False
    flashes = 0
    for i in range(len(octs)):
        for j in range(len(octs[0])):
            if(octs[i][j] <=9):
                continue
            change = True
            flashes += 1
            neighbours = getNeighbours(octs, i, j)
            octs[i][j] = 0
            for x,y in neighbours:
                if(octs[x][y] == 0):
                    continue
                octs[x][y] += 1
    return octs, change, flashes

totalSteps = 100
totalFlashes = 0
step = 1
while True:
    change = True
    octs = increase(octs)
    flashes = 0
    while change:
        octs, change, currflashes = increaseNeighbours(octs)
        flashes += currflashes
    
    if step<=100:
        totalFlashes += flashes

    if(flashes == len(octs)*(len(octs[0]))):
        break
    step += 1

print("Part 1:", totalFlashes)
print("Part 2:", step)
