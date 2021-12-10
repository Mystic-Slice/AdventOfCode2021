with open("input.txt", "r") as f:
    inputs = [line.strip() for line in f]

openingBrackets = ['(', '[', '{', '<']
closingBrackets = [')', ']', '}', '>']
illegalCharPoints = [3, 57, 1197, 25137]
strCompletionPoints = [1, 2, 3, 4]

def checkValid(string):
    st = []

    for bracket in string:
        if(bracket in openingBrackets):
            st.append(bracket)
        else:
            index = closingBrackets.index(bracket)
            if(openingBrackets[index] != st[-1]):
                 return illegalCharPoints[index], st
            else:
                st.pop()
    return 0, st

def completeString(string):
    remSt = checkValid(string)[1]
    res = ""
    ans = 0

    while len(remSt):
        bracket = remSt.pop()
        index = openingBrackets.index(bracket)
        res += closingBrackets[index]
        ans *= 5
        ans += strCompletionPoints[index]

    return ans, res

ans = sum([checkValid(string)[0] for string in inputs])

scores = [completeString(string)[0] for string in inputs if checkValid(string)[0] == 0]

print("Part1: ", ans)
print("Part2: ", sorted(scores)[len(scores)//2])
