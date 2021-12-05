with open("input.txt", "r") as f:
    inputs = [line.strip() for line in f]

draws = [int(x) for x in inputs[0].split(",")]
inputs = inputs[2:]
inputs.append("")
boards = []

for i in range(len(inputs)//6):
    dummy = []
    for j in range(5):
        dummy.append([int(x) for x in inputs[6*i+j].split()])
    boards.append(dummy)

def checkRowMatch(board):
    for i in range(len(board)):
        s = 0
        for j in range(len(board[0])):
            s += board[i][j]
        if s == -5:
            return True
    return False

def checkColMatch(board):
    for j in range(len(board[0])):
        s = 0
        for i in range(len(board)):
            s += board[i][j]
        if s == -5:
            return True
    return False

def checkWin(board):
    return checkRowMatch(board) or checkColMatch(board)

def addMark(board, x):
    for i in range(len(board)):
        for j in range(len(board[0])):
            if(board[i][j] == x):
                board[i][j] = -1
                return
    return

def calcAns(board, x):
    s = 0
    for i in range(len(board)):
        for j in range(len(board[0])):
            if not board[i][j] == -1:
                s += board[i][j]
    return s*x

res1 = -1
res2 = -1
for draw in draws:
    for board in boards:
        addMark(board, draw)
        win = checkWin(board)
        if win and res1 == -1:
            res1 = calcAns(board, draw)
        if win and len(boards) == 1:
            res2 = calcAns(board, draw)
    boards = [board for board in boards if not checkWin(board)]

print("Part1: ", res1)
print("Part2: ", res2)
