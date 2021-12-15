with open("input.txt", "r") as f:
    inputs = [line.strip() for line in f]
    
grid = []
for line in inputs:
    dummy = [int(x) for x in list(line)]
    grid.append(dummy)

def getNeighbours(x, y, grid):
    neighbours = []
    if(x < len(grid)-1):
        neighbours.append([x+1, y])
    if(y < len(grid[0])-1):
        neighbours.append([x, y+1])
    if(x > 0):
        neighbours.append([x-1, y])
    if(y > 0):
        neighbours.append([x, y-1])
    return neighbours

def findShortestPath(grid):
    mnDist = sum([sum(x) for x in grid])
    st = []
    st.append([grid[0][0], [0, 0]])
    dp = [[mnDist for x in l] for l in grid]
    dp[0][0] = grid[0][0]
    endx = len(grid)-1
    endy = len(grid[0])-1
    while len(st):
        dist, coord = st[0]
        st = st[1:]
        x, y = coord
        if(x == len(grid)-1 and y == len(grid[0])-1):
            return dist
        
        neighbours = getNeighbours(x, y, grid)
        for pair in neighbours:
            if(dp[pair[0]][pair[1]] <= dist + grid[pair[0]][pair[1]]):
                continue

            dp[pair[0]][pair[1]] = dist + grid[pair[0]][pair[1]]

            st.append([dp[pair[0]][pair[1]], pair])
        st = sorted(st)
    return mnDist

expanded = [[0 for x in range(5*len(grid[0]))] for l in range(5*len(grid))]
for x in range(len(expanded)):
	for y in range(len(expanded[0])):
		increments = x//len(grid) + y//len(grid[0])
		newval = grid[x%len(grid)][y%len(grid[0])]
		for i in range(increments):
			newval+=1
			if newval==10:
				newval=1
		expanded[x][y] = newval

print("Part1: ", findShortestPath(grid) - grid[0][0])
print("Part2: ", findShortestPath(expanded) - expanded[0][0])

