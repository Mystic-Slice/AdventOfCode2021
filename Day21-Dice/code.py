dieRoll = 0
playerPos = [9, 6]
playerScores = [0, 0]
currDie = 0
def currRoll():
    global currDie, dieRoll
    currDie += 1
    dieRoll += 1
    if(currDie>100):
        currDie -= 100
    return currDie
ans1 = 0
while(True):
    playerPos[0] += currRoll() + currRoll() + currRoll()
    while(playerPos[0] > 10):
        playerPos[0] -= 10

    playerScores[0] += playerPos[0]
    if(playerScores[0] >= 1000):
        ans1 = (playerScores[1]*dieRoll)
        break

    playerPos[1] += currRoll() + currRoll() + currRoll()
    while(playerPos[1] > 10):
        playerPos[1] -= 10

    playerScores[1] += playerPos[1]
    if(playerScores[1] >= 1000):
        ans1 = (playerScores[0]*dieRoll)
        break

dp = {}
def roll(player1, player2, score1, score2):
    if(score1 >= 21):
        return [1, 0]
    if(score2 >= 21):
        return [0, 1]
    if (player1, player2, score1, score2) in dp:
        return dp[(player1, player2, score1, score2)]
    ans = (0,0)
    for i in range(1, 4):
        for j in range(1, 4):
            for k in range(1, 4):
                newPlayerPos = player1+i+j+k
                if(newPlayerPos>10):
                    newPlayerPos -= 10
                newScore = score1 + newPlayerPos
                x,y = roll(player2, newPlayerPos, score2, newScore)
                ans = (ans[0]+y, ans[1]+x)
    dp[(player1, player2, score1, score2)] = ans
    return ans

print("Part1: ", ans1)
print("Part2: ", roll(9, 6, 0, 0))
    






