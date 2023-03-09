import random
from copy import deepcopy
board = [[' ']*8 for i in range(8)]
board[3][3] = 'X'
board[3][4] = 'O'
board[4][3] = 'O'
board[4][4] = 'X'


def drawBoard(board):
    columns = ''
    table = ''
    for i in range(8):
        columns += f'   {i+1}'
    print(columns)
    for row in range(len(board)):
        table += f'{row+1}'
        for col in range(len(board[row])):
             table += f'| {board[row][col]} '
        table += '|\n  '
        table += '----'*8
        table += '\n'
    print(table)

def getMove(x):
    while True:
        if x:
            first = 'X'
        else:
            first = 'O'
        print(f'{first} Where would you like to place your piece')
        move = input().split()
        if move[0].isdigit() and move[1].isdigit():
            move[0] = int(move[0])
            move[1] = int(move[1])
            if move[0] <=8 and move[1] <= 8:
                move[0] -= 1
                move[1] -= 1
                return move
            print('row and col must be less than or equal to 8')
        print('please enter 2 numbers (1-8)')
def getFirst():
    x = random.randint(0,1)
    if x == 1:
        return True
    else:
        return False
def isWinner(board,x):
    b1 = deepcopy(board)
    for i in range(1,7):
        for j in range(1,7):
            if board[i][j] == ' ':
                if checkMove(b1,[i,j],x):
                    return True
    return False




def checkMove(board,move,x):
    row = move[0]
    col = move[1]
    y = False
    if board[row][col] == ' ':
        if x:
            if row < 7 and row > 0 and col < 7 and col > 0:
                if board[row+1][col] == 'O' or board[row-1][col] =='O':
                    if verticle(board,move,x) >0:
                        y = True
                if board[row][col-1]=='O' or board[row][col+1]=='O':
                    if horizontal(board,move,x) > 0:
                        y = True
                if board[row+1][col+1] == 'O' or board[row-1][col+1]=="O" or board[row-1][col-1]=='O' or board[row+1][col-1]=='O':
                    if diagonal(board,move,x) >0:
                        y = True
                return y
            elif row>=7:   
                if col >= 7:
                    if board[row-1][col] =='O':
                        if verticle(board,move,x) >0:
                            y = True
                    if board[row][col-1]=='O':
                        if horizontal(board,move,x) >0:
                            y = True
                    if board[row-1][col-1]=='O':
                        if diagonal(board,move,x)  >0:
                            y = True
                elif col<=0:
                    if board[row-1][col] =='O':
                        if verticle(board,move,x) > 0:
                            y = True
                    if board[row][col+1]=='O':
                        if horizontal(board,move,x) >0:
                            y = True
                    if board[row-1][col+1]=='O':
                        if diagonal(board,move,x) >0:
                            y = True
                else:
                    if board[row-1][col] =='O':
                        if verticle(board,move,x) >0:
                            y = True
                    if board[row][col-1]=='O' or board[row][col+1]=='O':
                        if horizontal(board,move,x) >0:
                            y = True
                    if board[row-1][col+1]=='O' or board[row-1][col-1]=='O':
                        if diagonal(board,move,x) > 0:
                            y =  True
                return y
            elif row <= 0:
                if col >= 7:
                    if board[row+1][col] == 'O':
                        if verticle(board,move,x)>0:
                            y = True
                    if board[row][col-1]=='O':
                        if horizontal(board,move,x) > 0:
                            y = True
                    if board[row+1][col-1]=='O':
                        if diagonal(board,move,x) >0:
                            y =  True
                elif col<=0:
                    if board[row+1][col] == 'O':
                        if verticle(board,move,x) > 0:
                            y = True
                    if board[row][col+1]=='O':
                        if horizontal(board,move,x) >0:
                            y = True
                    if board[row+1][col+1] == 'O':
                        if diagonal(board,move,x) >0:
                            y =  True
                else:
                    if board[row+1][col] == 'O': 
                        if verticle(board,move,x) >0:
                            y = True
                    if board[row][col-1]=='O' or board[row][col+1]=='O':
                        if horizontal(board,move,x) > 0:
                            y = True
                    if board[row+1][col+1] == 'O'or board[row+1][col-1]=='O':
                        if diagonal(board,move,x) >0:
                            y =  True
                return y
            elif col >= 7:
                if board[row+1][col] == 'O' or board[row-1][col] =='O':
                    if verticle(board,move,x) > 0:
                        y = True
                if board[row][col-1]=='O':
                    if horizontal(board,move,x) > 0:
                        y = True
                if board[row-1][col-1]=='O' or board[row+1][col-1]=='O':
                    if diagonal(board,move,x) > 0:
                        y =  True
                return y
            elif col<=0:
                if board[row+1][col] == 'O' or board[row-1][col] =='O':
                    if verticle(board,move,x) > 0:
                        y = True
                if board[row][col+1]=='O':
                    if horizontal(board,move,x) > 0:
                        y = True
                if board[row+1][col+1] == 'O' or board[row-1][col+1]=="O":
                    if diagonal(board,move,x) >0:
                        y =  True
            return y
        else:
            if row < 7 and row > 0 and col < 7 and col > 0:
                if board[row+1][col] == 'X' or board[row-1][col] =='X':
                    if verticle(board,move,x) > 0:
                        y = True
                if board[row][col-1]=='X' or board[row][col+1]=='X':
                    if horizontal(board,move,x) > 0:
                        y = True
                if board[row+1][col+1] == 'X' or board[row-1][col+1]=="X" or board[row-1][col-1]=='X' or board[row+1][col-1]=='X':
                    if diagonal(board,move,x) > 0:
                        y = True
                return y
            elif row>=7:   
                if col >= 7:
                    if board[row-1][col] =='X':
                        if verticle(board,move,x) > 0:
                            y = True
                    if board[row][col-1]=='X':
                        if horizontal(board,move,x) > 0:
                            y = True
                    if board[row-1][col-1]=='X':
                        if diagonal(board,move,x) >0:
                            y = True
                elif col<=0:
                    if board[row-1][col] =='X':
                        if verticle(board,move,x) > 0:
                            y = True
                    if board[row][col+1]=='X':
                        if horizontal(board,move,x) >0:
                            y = True
                    if board[row-1][col+1]=='X':
                        if diagonal(board,move,x) > 0:
                            y = True
                else:
                    if board[row-1][col] =='X':
                        if verticle(board,move,x) > 0:
                            y = True
                    if board[row][col-1]=='X' or board[row][col+1]=='X':
                        if horizontal(board,move,x) > 0:
                            y = True
                    if board[row-1][col+1]=='X' or board[row-1][col-1]=='X':
                        if diagonal(board,move,x) > 0:
                            y =  True
                return y
            elif row <= 0:
                if col >= 7:
                    if board[row+1][col] == 'X':
                        if verticle(board,move,x) > 0:
                            y = True
                    if board[row][col-1]=='X':
                        if horizontal(board,move,x) > 0:
                            y = True
                    if board[row+1][col-1]=='X':
                        if diagonal(board,move,x) > 0:
                            y =  True
                elif col<=0:
                    if board[row+1][col] == 'X':
                        if verticle(board,move,x)>0:
                            y = True
                    if board[row][col+1]=='X':
                        if horizontal(board,move,x) > 0:
                            y = True
                    if board[row+1][col+1] == 'X':
                        if diagonal(board,move,x)>0:
                            y =  True
                else:
                    if board[row+1][col] == 'X': 
                        if verticle(board,move,x) >0:
                            y = True
                    if board[row][col-1]=='X' or board[row][col+1]=='X':
                        if horizontal(board,move,x) >0:
                            y = True
                    if board[row+1][col+1] == 'X'or board[row+1][col-1]=='X':
                        if diagonal(board,move,x)> 0:
                            y =  True
                return y
            elif col >= 7:
                if board[row+1][col] == 'X' or board[row-1][col] =='X':
                    if verticle(board,move,x) > 0:
                        y = True
                if board[row][col-1]=='X':
                    if horizontal(board,move,x) > 0:
                        y = True
                if board[row-1][col-1]=='X' or board[row+1][col-1]=='X':
                    if diagonal(board,move,x) >0:
                        y =  True
                return y
            elif col<=0:
                if board[row+1][col] == 'X' or board[row-1][col] =='X':
                    if verticle(board,move,x) > 0:
                        y = True
                if board[row][col+1]=='X':
                    if horizontal(board,move,x) > 0:
                        y = True
                if board[row+1][col+1] == 'X' or board[row-1][col+1]=="X":
                    if diagonal(board,move,x) > 0:
                        y =  True
            return y

def verticle(board,move,x):
    enemyCoords = []
    count = 0
    if x:
        for row in range(1,(7-move[0])):
            if board[row+move[0]][move[1]] == 'O':
                enemyCoords.append([row+move[0],move[1]])
            elif board[row+move[0]][move[1]] == 'X':
                if len(enemyCoords) != 0:
                    count += 1
                    enemyCoords.append([row+move[0],move[1]])
                    for i in enemyCoords:
                        board[i[0]][i[1]] = 'X'
                        count += 1
                    board[move[0]][move[1]] = 'X'
            elif board[row+move[0]][move[1]] == ' ':
                break
        enemyCoords = []
        for row in range(1,move[0]):
            if board[move[0] - row][move[1]] == 'O':
                enemyCoords.append([move[0] - row,move[1]])
            elif board[move[0] - row][move[1]] == 'X':
                if len(enemyCoords) != 0:
                    count += 1
                    enemyCoords.append([move[0]-row,move[1]])
                    for i in enemyCoords:
                        board[i[0]][i[1]] = 'X'
                        count += 1
                    board[move[0]][move[1]] = 'X'
            elif board[move[0]-row][move[1]] == ' ':
                break
    else:
        for row in range(1,(7-move[0])):
            if board[row+move[0]][move[1]] == 'X':
                enemyCoords.append([row+move[0],move[1]])
            elif board[row+move[0]][move[1]] == 'O':
                if len(enemyCoords) != 0:
                    count += 1
                    enemyCoords.append([row+move[0],move[1]])
                    for i in enemyCoords:
                        board[i[0]][i[1]] = 'O'
                        count += 1
                    board[move[0]][move[1]] = 'O'
            elif board[row+move[0]][move[1]] == ' ':
                break
        enemyCoords = []
        for row in range(1,move[0]):
            if board[move[0] - row][move[1]] == 'X':
                enemyCoords.append([move[0] - row,move[1]])
            elif board[move[0] - row][move[1]] == 'O':
                if len(enemyCoords) != 0:
                    count += 1
                    enemyCoords.append([move[0]-row,move[1]])
                    for i in enemyCoords:
                        board[i[0]][i[1]] = 'O'
                        count += 1
                    board[move[0]][move[1]] = 'O'
            elif board[move[0] - row][move[1]] == ' ':
                break
    return count
def horizontal(board,move,x):
    enemyCoords = []
    count = 0
    if x:
        for col in range(1,(7-move[1])):
            if board[move[0]][col+move[1]] == 'O':
                enemyCoords.append([move[0],col+move[1]])
            elif board[move[0]][col+move[1]] == 'X':
                if len(enemyCoords) != 0:
                    count += 1
                    enemyCoords.append([move[0],col+move[1]])
                    for i in enemyCoords:
                        board[i[0]][i[1]] = 'X'
                        count += 1
                    board[move[0]][move[1]] = 'X'
            elif board[move[0]][col+move[1]] == ' ':
                break
        enemyCoords == []
        for col in range(1,move[1]):
            if board[move[0]][move[1] - col] == 'O':
                enemyCoords.append([move[0],move[1]-col])
            elif board[move[0]][move[1] - col] == 'X':
                if len(enemyCoords) != 0:
                    count += 1
                    enemyCoords.append([move[0],move[1]-col])
                    for i in enemyCoords:
                        board[i[0]][i[1]] = 'X'
                        count += 1
                    board[move[0]][move[1]] = 'X'
            elif board[move[0]][move[1] - col] == ' ':
                break
    else:
        for col in range(1,(7-move[1])):
            if board[move[0]][col+move[1]] == 'X':
                enemyCoords.append([move[0],col+move[1]])
            elif board[move[0]][col+move[1]] == 'O':
                if len(enemyCoords) != 0:
                    count += 1
                    enemyCoords.append([move[0],col+move[1]])
                    for i in enemyCoords:
                        board[i[0]][i[1]] = 'O'
                        count += 1
                    board[move[0]][move[1]] = 'O'
            elif board[move[0]][col+move[1]] == ' ':
                break
        enemyCoords == []
        for col in range(1,move[1]):
            if board[move[0]][move[1] - col] == 'X':
                enemyCoords.append([move[0],move[1]-col])
            elif board[move[0]][move[1] - col] == 'O':
                if len(enemyCoords) != 0:
                    count += 1
                    enemyCoords.append([move[0],move[1]-col])
                    for i in enemyCoords:
                        board[i[0]][i[1]] = 'O'
                        count += 1
                    board[move[0]][move[1]] = 'O'
            elif board[move[0]][move[1] - col] == ' ':
                break
    return count

def diagonal(board,move,x):
    row = move[0]
    col = move[1]
    count = 0
    enemyCoords = []
    if x:
        for i in range(8):
            if row+i <= 7 and col+i <=7:
                if board[row+i][col+i] == 'O':
                    count+= 1
                    enemyCoords.append([row+i,col+i])
                elif board[row+i][col+i] == 'X':
                    if count > 0:
                        count += 1
                        enemyCoords.append([row+i,col+i])
                        for i in enemyCoords:
                            board[i[0]][i[1]] = 'X'
                        board[row][col] = 'X'
        count = 0
        for i in range(8):
            if col+i <=7 and row-1 > 0:
                if board[row-i][col+i] == 'O':
                    count+= 1
                    enemyCoords.append([row-i,col+i])
                elif board[row-i][col+i] == 'X':
                    if count > 0:
                        count += 1
                        enemyCoords.append([row-i,col+i])
                        for i in enemyCoords:
                            board[i[0]][i[1]] = 'X'
                        board[row][col] = 'X'
        count = 0
        for i in range(8):
            if row+i <= 7  and col-i>0:
                if board[row+i][col-i] == 'O':
                    count+= 1
                    enemyCoords.append([row+i,col-i])
                elif board[row+i][col-i] == 'X':
                    if count > 0:
                        count += 1
                        enemyCoords.append([row+i,col-i])
                        for i in enemyCoords:
                            board[i[0]][i[1]] = 'X'
                        board[row][col] = 'X'
        count = 0
        for i in range(8):
            if row-i>0 and col-i >0:
                if board[row-i][col-i] == 'O':
                    count+= 1
                    enemyCoords.append([row-i,col-i])
                elif board[row-i][col-i] == 'X':
                    if count > 0:
                        count+= 1
                        enemyCoords.append([row-i,col-i])
                        for i in enemyCoords:
                            board[i[0]][i[1]] = 'X'
                        board[row][col] = 'X'

        return count
    else:
        for i in range(8):
            if row+i <= 7 and col+i <=7:
                if board[row+i][col+i] == 'X':
                    count+= 1
                    enemyCoords.append([row+i,col+i])
                elif board[row+i][col+i] == 'O':
                    if count > 0:
                        count += 1
                        enemyCoords.append([row+i,col+i])
                        for i in enemyCoords:
                            board[i[0]][i[1]] = 'O'
                        board[row][col] = 'O'
        count = 0
        for i in range(8):
            if col+i <=7 and row-1 > 0 :
                if board[row-i][col+i] == 'X':
                    count+= 1
                    enemyCoords.append([row-i,col+i])
                elif board[row-i][col+i] == 'O':
                    if count > 0:
                        count += 1
                        enemyCoords.append([row-i,col+i])
                        for i in enemyCoords:
                            board[i[0]][i[1]] = 'O'
                        board[row][col] = 'O'
        count = 0
        for i in range(8):
            if row+i <= 7 and  col-i>0:
                if board[row+i][col-i] == 'X':
                    count+= 1
                    enemyCoords.append([row+i,col-i])
                elif board[row+i][col-i] == 'O':
                    if count > 0:
                        count += 1
                        enemyCoords.append([row+i,col-i])
                        for i in enemyCoords:
                            board[i[0]][i[1]] = 'O'
                        board[row][col] = 'O'
        count = 0
        for i in range(8):
            if row-i > 0 and col-i >0:
                if board[row-i][col-i] == 'X':
                    count+= 1
                    enemyCoords.append([row-i,col-i])
                elif board[row-i][col-i] == 'O':
                    if count > 0:
                        count += 1
                        enemyCoords.append([row-i,col-i])
                        for i in enemyCoords:
                            board[i[0]][i[1]] = 'O'
                        board[row][col] = 'O'
        return count
        





print('This is reversi')
x = getFirst()
if x:
    print('It is X turn to go first')
else:
    print('It is O turn to go first')
while True:
    drawBoard(board)
    move = getMove(x)
    if isWinner(board,x) != False:
        if board[move[0]][move[1]]== ' ':
            if checkMove(board,move,x) != False:
                if x:
                    x = False 
                else:
                    x = True
            else:
                print("Can't move there. Try again")
        else:
            print('Not a valid move')
    else:
        if x == True:
            print('O has won')
        else:
            print('X has won')