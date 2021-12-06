with open("input.txt", "r") as f:
    inputs = [line.strip() for line in f]

fishes = [int(x) for x in inputs[0].split(",")]

fishCount = []
for i in range(9):
    fishCount.append(0)
for fish in fishes:
    fishCount[fish] += 1

def calcFishes(fishCount, numDays):
    while numDays > 0:
        numDays -= 1
        first = fishCount[0]
        for i in range(1, 9):
            fishCount[i-1] = fishCount[i]
        fishCount[8] = first
        fishCount[6] += first
    return fishCount

print("Part1: ", sum(calcFishes(fishCount.copy(), 80)))
print("Part2: ", sum(calcFishes(fishCount.copy(), 256)))
