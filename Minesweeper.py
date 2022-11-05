import random
def GenerateMineSweeperMap(n, k):#n represents the size of matrix and k represents number of bombs
    arr = [[0 for row in range(n)] for column in range(n)]
    for num in range(k):
        x = random.randint(0,n-1)
        y = random.randint(0,n-1)
        arr[y][x] = 'X'
        if (x >=0 and x <= n-2) and (y >= 0 and y <= n-1):
            if arr[y][x+1] != 'X':
                arr[y][x+1] += 1 # center right
        if (x >=1 and x <= n-1) and (y >= 0 and y <= n-1):
            if arr[y][x-1] != 'X':
                arr[y][x-1] += 1 # center left
        if (x >= 1 and x <= n-1) and (y >= 1 and y <= n-1):
            if arr[y-1][x-1] != 'X':
                arr[y-1][x-1] += 1 # top left
 
        if (x >= 0 and x <= n-2) and (y >= 1 and y <= n-1):
            if arr[y-1][x+1] != 'X':
                arr[y-1][x+1] += 1 # top right
        if (x >= 0 and x <= n-1) and (y >= 1 and y <= n-1):
            if arr[y-1][x] != 'X':
                arr[y-1][x] += 1 # top center
 
        if (x >=0 and x <= n-2) and (y >= 0 and y <= n-2):
            if arr[y+1][x+1] != 'X':
                arr[y+1][x+1] += 1 # bottom right
        if (x >= 1 and x <= n-1) and (y >= 0 and y <= n-2):
            if arr[y+1][x-1] != 'X':
                arr[y+1][x-1] += 1 # bottom left
        if (x >= 0 and x <= n-1) and (y >= 0 and y <= n-2):
            if arr[y+1][x] != 'X':
                arr[y+1][x] += 1 # bottom center
    return arr
def GeneratePlayerMap(n):# Hides the game board with '-'
    arr = [['-' for row in range(n)] for column in range(n)]
    return arr
def DisplayMap(map):
    for row in map:
        print(" ".join(str(cell) for cell in row))
        print("")
def CheckWon(map):
    for row in map:
        for cell in row:
            if cell == '-':
                return False
    return True
def CheckContinueGame(score):#Ask's to play again or not
    print("Your score: ", score)
    isContinue = input("Do you want to try again? (y/n) :")
    if isContinue == 'n':
        return False
    return True
    #modification
Best_score=[]
def best_score(score):
     Best_score.append(score)
     return max(Best_score)

def Game():
    GameStatus = True
    while GameStatus:
        difficulty = input("Select your difficulty (b, i, h):")# Allowing to select difficulty level
        if difficulty.lower() == 'b':
            n = 5
            k = 3
        elif difficulty.lower() == 'i':
            n = 6
            k = 8
        else:
            n = 8
            k = 20
 
        minesweeper_map = GenerateMineSweeperMap(n, k)
        player_map = GeneratePlayerMap(n)
        score = 0
        while True:
            if CheckWon(player_map) == False:
                print("Enter your cell you want to open :")
                x = input("x(1 to"+str(n)+") :",)
                y = input("y(1 to"+str(n)+") :",)
                print()
                x = int(x) - 1 # 0 based indexing
                y = int(y) - 1 # 0 based indexing
                if (minesweeper_map[y][x] == 'X'):
                    print("Game Over!")
                    print()
                    DisplayMap(minesweeper_map)
                    #modification
                    print("Best score: ",best_score(score))
                    GameStatus = CheckContinueGame(score)
                    print()
                    break
                else:
                    player_map[y][x] = minesweeper_map[y][x]
                    DisplayMap(player_map)
                    score += 1
 
            else:
                DisplayMap(player_map)
                print("You have Won!")
                GameStatus = CheckContinueGame(score)
               
                break
# Start of Program
if __name__ == "__main__":
    try:
        Game()
    except KeyboardInterrupt:
        print('\nEnd of Game. Bye Bye!')
