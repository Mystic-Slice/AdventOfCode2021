with open("input.txt", "r") as f:
    inputs = [line.strip() for line in f]

count = []
for x in inputs[0]:
    count.append(0)

for binString in inputs:
    for i in range(len(binString)):
        count[i] += 1 if binString[i] == '1' else -1

gamma = []
epsilon = []
for x in count:
    gamma.append("1" if x >= 0 else "0")
    epsilon.append("0" if x > 0 else "1")

gammaVal = int("".join(gamma), 2)
epsilonVal = int("".join(epsilon), 2)

o2 = inputs.copy()
o2Count = count.copy()
o2Bits = gamma.copy()

co2 = inputs.copy()
co2Count = count.copy()
co2Bits = epsilon.copy()

def countBits():
    global o2, o2Count, o2Bits, co2, co2Count, co2Bits
    for i in range(len(o2Count)):
        o2Count[i] = 0
        co2Count[i] = 0
    for binString in o2:
        for i in range(len(binString)):
            o2Count[i] += 1 if binString[i] == '1' else -1
    for binString in co2:
        for i in range(len(binString)):
            co2Count[i] += 1 if binString[i] == '1' else -1
    for i, x in enumerate(o2Count):
        o2Bits[i] = "1" if x >= 0 else "0"
    for i, x in enumerate(co2Count):
        co2Bits[i] = "0" if x >= 0 else "1"
    
for i in range(len(gamma)):
    if not len(o2) == 1:
        o2 = [x for x in o2 if x[i] == o2Bits[i]]
    if not len(co2) == 1:
        co2 = [x for x in co2 if x[i] == co2Bits[i]]
    countBits()

print(gamma, epsilon)
print(o2, co2)
o2Val = int(o2[0], 2)
co2Val = int(co2[0], 2)

print("Part1: ", gammaVal*epsilonVal)
print("Part2: ", o2Val*co2Val)

