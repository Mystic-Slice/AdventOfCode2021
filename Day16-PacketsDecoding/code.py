with open("input.txt", "r") as f:
    inputs = [line.strip() for line in f]

hexDict = {
        "0" : "0000",
        "1" : "0001",
        "2" : "0010",
        "3" : "0011",
        "4" : "0100",
        "5" : "0101",
        "6" : "0110",
        "7" : "0111",
        "8" : "1000",
        "9" : "1001",
        "A" : "1010",
        "B" : "1011",
        "C" : "1100",
        "D" : "1101",
        "E" : "1110",
        "F" : "1111"
}

stringList = [hexDict[x] for x in list(inputs[0])]
string = "".join(stringList)

totalVersion = 0

def parseLiteral(s):
    nums = []
    while True:
        subStr = s[:5]
        nums.append(subStr[1:])
        s = s[5:]
        if subStr[0] == '0':
            break
    num = int("".join(nums), 2)
    return s, num

def parse(s):
    global totalVersion
    if '1' not in s:
        return "", 0
    versionOp = int(s[:3], 2)
    totalVersion += versionOp

    typeId = int(s[3:6], 2)
    s = s[6:]
    
    num = -1
    if typeId == 4:
        s, num = parseLiteral(s)
    else:
        typeLengthId = int(s[0], 2)
        s = s[1:]
        arr = []
        if typeLengthId == 0:
            lenSubPacket = int(s[:15], 2)
            s = s[15:]
            subStr = s[:lenSubPacket]
            s = s[lenSubPacket:]
            res = subStr
            while res != "":
                res, n = parse(res)
                arr.append(n)
        else:
            numSubPacket = int(s[:11], 2)
            s = s[11:]
            while numSubPacket:
                numSubPacket -= 1
                s, n = parse(s)
                arr.append(n)
        if typeId == 0:
            num = sum(arr)
        elif typeId == 1:
            num = 1
            for x in arr:
                num *= x
        elif typeId == 2:
            num = arr[0]
            for x in arr:
                num = min(x, num)
        elif typeId == 3:
            num = arr[0]
            for x in arr:
                num = max(x, num)
        elif typeId == 5:
            num = (arr[0] > arr[1])
        elif typeId == 6:
            num = (arr[0] < arr[1])
        elif typeId == 7:
            num = (arr[0] == arr[1])

    return s, num

string, ans = parse(string)
print("Part1: ", totalVersion)
print("Part2: ", ans)
