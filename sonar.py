import random
import math

def displayBoard(lis):
    print('             1         2         3         4         5') 
    print("   " + '0123456789'*6 + "\n")
    for i in range(len(lis)):
        if i <= 9:
            print(str(i)+"  " + "".join(map(str, lis[i])) +" "+ str(i))
        else:
            print(str(i)+" "+  "".join(map(str, lis[i])) +" "+ str(i))
    print("   " + '0123456789'*6 )
    print('             1         2         3         4         5\n') 
def placeChest(lis,chest):
    x = chest
    coord = []
    while x>0:
        num1 = random.randint(0,14)
        num2 = random.randint(0,58)
        coord.append((num1,num2))
        x-=1
    return coord
def getGuess(guess):
    if len(guess) == 2:
        if guess[0].isdigit() and guess[1].isdigit():
            if int(guess[0]) > 14 or int(guess[1]) > 59:
                print("not a valid number. (row 0-14, col 0-59)")
                return False
            else:
                return int(guess[0]), int(guess[1])
        else:
            print("not a number. (row, col)")
            return False
    else:
        print("not entered in correct format (row, col)")
        return False
def checkGuess(row,col,coords,chests):
    distance = []
    for i in range(len(coords)):
        y = (coords[i][0] - row)**2
        x = (coords[i][1] - col)**2
        dist = math.sqrt(y + x)
        if dist == 0:
            chests -= 1
            print(f"found one. {chests} to go")
            return 0
        else:
            distance.append(dist)
    if min(distance)%1 > .5:
        return int((min(distance)//1) +1)
    else:
        return int(min(distance)//1)
def Difficulty():
    print("Select difficulty: Easy, Medium, Hard, Insane")
    diff = True
    while diff == True:
        difficulty = input().lower()
        match difficulty:
            case "insane":  
               return 40,8
            case "hard":
                return 30, 6
            case "medium":
                return 20, 3
            case "easy":
                return 20, 2
            case default:
                print("not a valid anwser. Try again")
                diff = True
def play(COUNT,CHEST,board,coord):
    while(COUNT != 0 and CHEST != 0):
        displayBoard(board)
        print(f"You have: {CHEST} chests remaining\nYou have: {COUNT} tries left\n")
        while True:
            print("Please enter a guess (row 0-14, col 0-59)")
            guess = input().split(",")
            if getGuess(guess) != False:
                row, col = getGuess(guess)
                if (row,col) in guesses:
                    print("You have already guessed that. Try again.")
                else:
                    guesses.append((row,col))
                    break
        val = checkGuess(row,col,coordinate,CHEST)
        if col != 0:
            if col != 58:
                x = board[row][col-1:].split(board[row][col],1)
                if val > 9:
                    y = x[1].split(x[1][0],1)
                    y.pop(0)
                    board[row] = board[row][:col-1]
                    board[row] += x[0] + str(val)
                    board[row] += "".join(y)
                elif val == 0:
                    x[0] += "X"
                    board[row] = board[row][:col-1]
                    board[row] += "".join(x)
                    CHEST -= 1
                    coord.remove((row,col))
                else:
                    x[0] += str(val)
                    board[row] = board[row][:col-1]
                    board[row] += "".join(x)
            else:
                y = board[row][:-1]
                if val == 0:
                    board[row] = board[row][-1].replace(board[row][-1], "X",1)
                    CHEST -=1
                    x = [y, board[row]]
                    board[row] = "".join(x)
                    coord.remove((row,col))
                else:
                    board[row] = board[row][-1].replace(board[row][-1], str(val),1)
                    x = [y, board[row]]
                    board[row] = "".join(x)
        else:
           if val > 9: 
                board[row] = board[row].replace(board[row][1],"",1)
                board[row] = board[row].replace(board[row][col],str(val),1)
           elif val == 0:
                board[row] = board[row].replace(board[row][col],"X",1)
                CHEST -= 1 
                coord.remove((row,col))
           else:
                board[row] = board[row].replace(board[row][0], str(val),1)
                x = [y, board[row]]
                board[row] = "".join(x) 
        COUNT-=1
    if CHEST == 0:
        print("Congratulations you found all the Chests. Would you like to play again(Yes/No)")
    else:    
        print("You ran out of guesses, Would you like to play again(Yes/No)")

playAgain = True
while playAgain == True:
    guesses = []
    board = ["|`~`~`~`~`"*6 ]*15
    print("\nSonar Game \n\nThe goal of the game is to find all three chests\nClues are given based on how close you are.\n")
    count, chest = Difficulty()
    coordinate = placeChest(board,chest)
    play(count,chest,board,coordinate)
    playAgain = input().lower().startswith("y")    