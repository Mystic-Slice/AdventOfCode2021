import itertools
with open("input.txt", "r") as f:
    inputs = [line.strip() for line in f]

random10 = []
digits4 = []

for line in inputs:
    random, digits = line.split(" | ")
    random10.append(random.split(" "))
    digits4.append(digits.split(" "))

print(digits4)

cnt = 0
lengths = [2, 3, 4, 7]

for x in digits4:
    for y in x:
        if(len(y) in lengths):
            cnt += 1

print("Part 1:", cnt)

masterD = {
        "abcdeg": 0,
        "ab": 1,
        "acdfg": 2,
        "abcdf": 3,
        "abef": 4,
        "bcdef": 5,
        "bcdefg": 6,
        "abd": 7,
        "abcdefg": 8,
        "abcdef": 9
}

def replaceChars(s, d):
    return ''.join(sorted(d[x] for x in s))

def buildNum(nums):
    ans = 0
    for x in nums:
        ans += x 
        ans *= 10
    return ans/10

def checkForValidPerm(random, output):
    global masterD
    for perm in itertools.permutations('abcdefg'):
        d = {x:y for x, y in zip(perm, 'abcdefg')}
        afterReplace = []
        for s in random:
            afterReplace.append(replaceChars(s, d))
        if all((x in masterD) for x in afterReplace):
            output = [masterD[replaceChars(x, d)] for x in output]
            return buildNum(output)
    return 0

ans = 0
for random, digits in zip(random10, digits4):
    ans += checkForValidPerm(random, digits)
print("Part 2:", ans)
