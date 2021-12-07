with open("input.txt", "r") as f:
    inputs = [line.strip() for line in f]

pos = [int(x) for x in inputs[0].split(",")]
pos.sort()
n = len(pos)

def calcCost(pos, x, rate = "constant"):
    cost = 0
    for i in pos:
        diff = abs(x-i)
        if rate == "incremental":
            diff = diff*(diff + 1)/2
        cost += diff
    return cost

median1 = pos[n//2]
median2 = pos[n//2 + 1]
print("Part 1:", min(calcCost(pos, median1), calcCost(pos, median2)))

average1 = sum(pos)//n
average2 = round(sum(pos)/n)
print("Part 2:", min(calcCost(pos, average1, "incremental"), calcCost(pos, average2, "incremental")))
