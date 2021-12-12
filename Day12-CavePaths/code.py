with open("input.txt", "r") as f:
    inputs = [line.strip() for line in f]

adjList = {}
isSmall = {}
for line in inputs:
    u, v = line.split("-")
    if(u in adjList.keys()):
        adjList[u].append(v)
    else:
        adjList[u] = [v]

    if(v in adjList.keys()):
        adjList[v].append(u)
    else:
        adjList[v] = [u]

    isSmall[u] = u == u.lower()
    isSmall[v] = v == v.lower()

def dfs():
    allPathsOnce = []
    allPathsTwice = []
    st = [[["start"], False]]
    
    while len(st):
        currPath, twiceTaken = st.pop()
        node = currPath[-1]
        
        if(node == "end"):
            if not twiceTaken:
                allPathsOnce.append(currPath.copy())
            allPathsTwice.append(currPath.copy())
            continue

        for x in adjList[node]:
            
            if((x == "start" or x == "end") and x in currPath):
                continue

            if(isSmall[x] and twiceTaken and x in currPath):
                continue

            if(isSmall[x] and x in currPath):
                twiceTaken = True

            currPath.append(x)
            st.append([currPath.copy(), twiceTaken])
            currPath.pop()

            if(isSmall[x] and x in currPath):
                twiceTaken = False

    return allPathsOnce, allPathsTwice

allPathsOnce, allPathsTwice = dfs()

print("Part1: ", len(allPathsOnce))
print("Part2: ", len(allPathsTwice))
