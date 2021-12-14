with open("input.txt", "r") as f:
    inputs = [line.strip() for line in f]

string = list(inputs[0])
insertions = {}

for i in range(2, len(inputs)):
    pattern, insertedChar = inputs[i].split(" -> ")
    insertions[pattern] = insertedChar

# Use this to get the actual string (will take a long time to compute)
def insertChars(string, insertions):
    res = string.copy()
    for insertion in insertions:
        pattern, insertedChar = insertion
        i = 0
        while True:
            if(i == len(res)-1):
                break
            if(res[i] == pattern[0] and res[i+1] == pattern[1]):
                res = res[:i+1] + [insertedChar.lower()] + res[i+1:]

            i += 1
    res = [x.upper() for x in res]
    return res

def polymerize(string, insertions, steps):
    pairsCount = {}
    for i in range(len(string)-1):
        dummy = string[i]+string[i+1]
        if dummy in insertions:
            if dummy in pairsCount:
                pairsCount[dummy] += 1
            else:
                pairsCount[dummy] = 1

    for i in range(steps):
        newPairsCount = {}
        for pair, count in pairsCount.items():
            if pair in insertions:
                for x in [pair[0] + insertions[pair], insertions[pair] + pair[1]]:
                    if x in newPairsCount:
                        newPairsCount[x] += count
                    else:
                        newPairsCount[x] = count
            else:
                if pair in newPairsCount:
                    newPairsCount[pair] += count
                else:
                    newPairsCount[pair] = count
        pairsCount = newPairsCount
    
    d = {}
    cnt = 0
    for pair, count in pairsCount.items():
        for x in pair:
            if x in d:
                d[x] += count
            else:
                d[x] = count
        cnt += count
    
    d[string[0]] += 1
    d[string[-1]] += 1
    
    for key, value in d.items():
        d[key] = value/2
    
    minItem = 'A'
    minFreq = cnt
    maxItem = 'A'
    maxFreq = 0 
    
    for key, value in d.items():
        if(value < minFreq):
            minFreq = value
            minItem = key
        if(value > maxFreq):
            maxFreq = value
            maxItem = key
    
    return((maxFreq-minFreq))

print("Part1: ", int(polymerize(string, insertions, 10)))
print("Part2: ", int(polymerize(string, insertions, 40)))
