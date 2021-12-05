with open("input.txt", "r") as f:
    inputs = [int(line.strip()) for line in f]

cnt1 = 0
cnt2 = 0
n = len(inputs)
for x in range(1, n):
    if inputs[x] > inputs[x-1]:
        cnt1 += 1
    if x < 3:
        continue
    if inputs[x] > inputs[x-3]:
        cnt2 += 1

print("Part 1: ", cnt1)
print("Part 2: ", cnt2)
