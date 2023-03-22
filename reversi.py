import random
from copy import deepcopy






def drawBoard(board):
    columns = ''
    table = ''
    for i in range(8):
        columns += f'   {i+1}'
    print(columns)
    for row in range(len(board.getBoard())):
        table += f'{row+1}'
        for col in range(len(board.getBoard())):
            p = board.getBoard()[row][col].getChar()
            board.setPiece([row,col],p)
            table = table + f'| {p} '
        table += '|\n  '
        table += '----'*8
        table += '\n'
    print(table)
 
class piece():
    Char = ' '
    def __init__(self,color):
        if color == "X":
            self.Char = 'X'
        elif color == 'O':
            self.Char = 'O'
        else:
            self.Char = ' '

    def getChar(self):
        return self.Char
    def setChar(self,char):
        self.Char = char
    
class board():
    def __init__(self,board,turn):
        self.board = board
        self.turn = turn
    def setBoard(self,board):
        self.board = board
    def checkMove(self,move):
        row = move[0]
        col = move[1]   
        if self.board[row][col].getChar() == ' ':
            if row < 7 and col < 7 and row >0 and col >0:
                if (self.board[row+1][col].getChar() != self.turn or self.board[row-1][col].getChar() != self.turn or self.board[row][col+1].getChar() != self.turn or self.board[row][col-1].getChar() != self.turn or self.board[row+1][col+1].getChar() != self.turn or self.board[row-1][col-1].getChar() != self.turn or self.board[row-1][col+1].getChar() != self.turn or self.board[row+1][col-1].getChar() != self.turn) and (self.board[row+1][col].getChar() != ' ' or self.board[row-1][col].getChar() != ' ' or self.board[row][col+1].getChar() != ' ' or self.board[row][col-1].getChar() != ' ' or self.board[row+1][col+1].getChar() != ' ' or self.board[row-1][col-1].getChar() != ' ' or self.board[row-1][col+1].getChar() != ' ' or self.board[row+1][col-1].getChar() != ' '):
                    return True
                else:
                    return False
            elif row >=7:
                if col>=7:
                    if (self.board[row-1][col].getChar() != self.turn or self.board[row][col-1].getChar() != self.turn or self.board[row-1][col-1].getChar() != self.turn) and (self.board[row-1][col].getChar() != ' ' or self.board[row][col-1].getChar() != ' ' or self.board[row-1][col-1].getChar() != ' '):    
                        return True
                    return False

                elif col <= 0:
                    if (self.board[row-1][col].getChar() != self.turn or self.board[row][col+1].getChar() != self.turn or  self.board[row-1][col+1].getChar() != self.turn) and (self.board[row-1][col].getChar() != ' ' or self.board[row][col+1].getChar() != ' '  or  self.board[row-1][col+1].getChar() != ' ' ):
                        return True
                    return False

                else:
                    if (self.board[row-1][col].getChar() != self.turn or self.board[row][col+1].getChar() != self.turn or self.board[row][col-1].getChar() != self.turn or self.board[row-1][col-1].getChar() != self.turn or self.board[row-1][col+1].getChar() != self.turn) and (self.board[row-1][col].getChar() != " " or self.board[row][col+1].getChar() != " " or self.board[row][col-1].getChar() != " " or self.board[row-1][col-1].getChar() != " " or self.board[row-1][col+1].getChar() != " "):
                        return True
                    return False

            elif row <= 0:
                if col>=7:
                    if (self.board[row+1][col].getChar() != self.turn or self.board[row][col-1].getChar() != self.turn or  self.board[row+1][col-1].getChar() != self.turn) and (self.board[row+1][col].getChar() != " " or self.board[row][col-1].getChar() != " " or  self.board[row+1][col-1].getChar() != " "):
                        return True
                    return False

                elif col <= 0:
                    if (self.board[row+1][col].getChar() != self.turn or self.board[row][col+1].getChar() != self.turn or self.board[row-1][col-1].getChar() != self.turn) and (self.board[row+1][col].getChar() != ' ' or self.board[row][col+1].getChar() != " " or self.board[row-1][col-1].getChar() != ' '):
                        return True
                    return False

                else:
                    if (self.board[row+1][col].getChar() != self.turn or self.board[row][col+1].getChar() != self.turn or self.board[row][col-1].getChar() != self.turn or self.board[row+1][col+1].getChar() != self.turn or self.board[row+1][col-1].getChar() != self.turn) and (self.board[row+1][col].getChar() != ' ' or self.board[row][col+1].getChar() != ' ' or self.board[row][col-1].getChar() != ' ' or self.board[row+1][col+1].getChar() != ' ' or self.board[row+1][col-1].getChar() != ' '):
                        return True
                    return False
            elif col >= 7:
                if (self.board[row+1][col].getChar() != self.turn or self.board[row-1][col].getChar() != self.turn or self.board[row][col-1].getChar() != self.turn or self.board[row-1][col-1].getChar() != self.turn or self.board[row+1][col-1].getChar() != self.turn) and (self.board[row+1][col].getChar() != ' ' or self.board[row-1][col].getChar() !=  ' 'or self.board[row][col-1].getChar() !=  ' ' or self.board[row-1][col-1].getChar() !=  ' ' or self.board[row+1][col-1].getChar() !=  ' '):
                    return True
                return False
            elif col <= 0:    

                if (self.board[row+1][col] != self.turn or self.board[row-1][col].getChar() != self.turn or self.board[row][col+1].getChar() != self.turn or self.board[row+1][col+1].getChar() != self.turn or self.board[row-1][col+1].getChar() != self.turn) and (self.board[row+1][col] != ' ' or self.board[row-1][col].getChar() != ' ' or self.board[row][col+1].getChar() != ' ' or self.board[row+1][col+1].getChar() != ' ' or self.board[row-1][col+1].getChar() != ' '):
                    return True
                return False
            else:
                return False
    def getBoard(self):
        return self.board
    
    def isWinner(self,move):
        b1 = deepcopy(board)
        for i in range(8):
            for j in range(8):
                if self.board[i][j].getChar()==' ':
                    return False
        return False

    def setPiece(self,move,char):
        self.board[move[0]][move[1]].setChar(char)
    def verticle(self,move):
        x = False
        count = 0
        row = move[0]
        col = move[1]
        count1 = 0
        for i in range(1,8):
            if row+i <= 7 :
                if self.board[row+i][col].getChar() == ' ':
                    break
                elif self.board[row+i][col].getChar() != self.turn:
                    count1 += 1
                elif self.board[row+i][col].getChar() ==  self.turn:
                    j = 1
                    if count1 != 0:
                        while j <= count1:
                            if self.board[row+j][col].getChar() != self.turn:
                                self.setPiece([row+j,col],self.turn)
                                x = True
                            else:
                                break   
                            j += 1
                        count += count1
                        break
                    else:
                        break                      
        count2 = 0
        for t in range(1,8):
            if row-t >= 0:
                if self.board[row-t][col].getChar() == ' ':
                    break
                elif self.board[row-t][col].getChar() != self.turn:
                    count2 += 1
                elif self.board[row-t][col].getChar() == self.turn:
                    j = 1
                    if count2 != 0:
                        while j <= count2:
                            if self.board[row-j][col].getChar != self.turn:
                                self.setPiece([row-j,col],self.turn)
                                x = True
                            else:
                                break
                            j += 1
                        count += count2
                        break
                    else:
                        break                      
        return x,count
            
    def horizontal(self,move):
        x = False
        count = 0
        row = move[0]
        col = move[1]
        count1 = 0
        for i in range(1,8):
            if col+i <= 7 :
                if self.board[row][col+i].getChar() == " ":
                    break
                elif self.board[row][col+i].getChar() != self.turn:
                    count1 += 1

                elif self.board[row][col+i].getChar() ==  self.turn:
                    if count1 != 0:
                        j = 1
                        while j <= count1:
                            if self.board[row][col+j].getChar != self.turn:
                                self.setPiece([row,col+j],self.turn)
                                x = True
                            else:
                                break
                            j += 1
                        count += count1
                        break
                    else:
                        break                       
        count2 = 0                    
        for t in range(1,8):
            if col-t >= 0:
                if self.board[row][col-t].getChar() == ' ':
                    break
                elif self.board[row][col-t].getChar() != self.turn:
                    count2 += 1
                elif self.board[row][col-t].getChar() == self.turn:
                    j = 1
                    if count2 != 0:
                        while j <= count2:
                            if self.board[row][col-j].getChar() != self.turn:
                                self.setPiece([row,col-j],self.turn)
                                x = True
                            else:
                                break
                            j += 1
                        count += count2
                        break
                    else:
                        break                        
        return x,count
            
    def diagonal(self,move):
        row = move[0]
        col = move[1]
        count = 0
        x = False
        count3 = 0
        for i in range(1,8):
            if row+i <= 7 and col+i<=7:
                if self.board[row+i][col+i].getChar() == ' ':
                    break
                elif self.board[row+i][col+i].getChar() != self.turn:
                    count3 += 1
                elif self.board[row+i][col+i].getChar() ==  self.turn:
                    if count3 != 0:
                        j = 1
                        while j <= count3:
                            if self.board[row+j][col+j].getChar() != self.turn:
                                self.setPiece([row+j,col+j],self.turn)
                                x = True
                            else:
                                break
                            j += 1
                        count += count3
                        break
                    else:
                        break                      

        count2 = 0            
        for t in range(1,8):
            if row-t >= 0 and col-t >=0:
                if self.board[row-t][col-t].getChar() == ' ':
                    break
                elif self.board[row-t][col-t].getChar() != self.turn:
                    count2+=1
                elif self.board[row-t][col-t].getChar() == self.turn:
                    if count2 != 0:
                        j = 1
                        while j <= count2:
                            if self.board[row-j][col-j].getChar() != self.turn:
                                self.setPiece([row-j,col-j],self.turn)
                                x = True
                            else:
                                break
                            j += 1
                        count += count2
                        break
                    else:
                        break                      

        count1 = 0
        for p in range(1,8):
            if row-p >= 0 and col+p<=7:
                if self.board[row-p][col+p].getChar()== ' ':
                    break
                elif self.board[row-p][col+p].getChar() != self.turn:
                    count1 += 1
                elif self.board[row-p][col+p].getChar() == self.turn:
                    j = 1
                    if count1 != 0:       
                        while j <= count1:
                            if self.board[row-j][col+j].getChar() != self.turn:
                                self.setPiece([row-j,col+j],self.turn)
                                x = True
                            else:
                                break
                            j += 1
                        count += count1
                        break
                    else:
                        break
        count4 = 0
        
        for r in range(1,8):
            if row+r <= 7 and col-r>=0:
                if self.board[row+r][col-r].getChar() == ' ':
                    break
                elif self.board[row+r][col-r].getChar() != self.turn:
                    count4 += 1
                elif self.board[row+r][col-r].getChar() == self.turn:
                    j = 1
                    if count4 != 0:    
                        while j <= count4: 
                            if self.board[row+j][col-j].getChar() != self.turn:
                                self.setPiece([row+j,col-j],self.turn)
                                x = True
                            else:
                                break
                            j += 1
                        count += count4
                        break
                    else:
                        break   
        return x,count
                
    def getCompMove(self):
        t = deepcopy(self)
        max = 0
        tempCoord=[[0,0]]
        for i in range(8):
            for j in range(8):
                p = deepcopy(self.getBoard())
                t.setBoard(p)
                if t.getBoard()[i][j].getChar() == ' ':
                    if t.isWinner==True:
                        tempCoord[0] == [i,j]
                        self.setPiece(tempCoord[0],self.turn)
                        return tempCoord[0]
                    elif t.checkMove([i,j]):
                        z,count3 = t.diagonal([i,j])
                        y,count2 = t.verticle([i,j])
                        x,count1 = t.horizontal([i,j])
                        if x or y or z: 
                            if count1+count2+count3 > max:
                                max = count1 + count2 + count3
                                tempCoord[0] = [i,j]
                            else:
                                continue
                        else:
                            continue
                else:
                    continue

        return tempCoord[0]


    def getPiece(self,move):
        return self.board[move[0]][move[1]]   
 
    def isWinner(self,char):
        b1 = deepcopy(self)
        for i in range(8):
            for j in range(8):
                if b1.board[i][j].getChar()==' ':
                        return False
        return True

    def getTurn(self):
        return self.turn
    def setTurn(self,turn):
        self.turn = turn
    def getMove(self,turn):

        while True:
            print(f'{turn} Where would you like to place your piece')
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


def getFirst(game):
        p = ''
        c = ''
        if game.startswith('l'):
            t = random.randint(0,1)
            if t == 1:
                return 'X',p
            else:
                return "O",p
        elif game.startswith('c'):
            t = random.randint(0,1)
            j = random.randint(0,1)
            if t == 1:
                first = "c"
                second = 'p'
            else:
                first = 'p'
                second = 'c'
            t = random.randint(0,1)
            if t == 1:
                return 'X',first
            else:
                return "O",second
print('would you like to play local or against computer')
game = input().lower()
first,player =getFirst(game)

lis1 = [([])*8 for i in range(8)]
for i in range(8):
    for j in range(8):
        lis1[i].append(piece(' '))

board1 = board(lis1,first)


piece1 = piece("X")
piece2 = piece("X")
piece3 = piece("O")
piece4 = piece("O")

board1.getBoard()


board1.setPiece([3,3],piece1.Char)
board1.setPiece([3,4],piece4.Char)
board1.setPiece([4,3],piece3.Char)
board1.setPiece([4,4],piece2.Char)

if game.startswith('l'):
    while True:
        print('Reversi')
        l = deepcopy(board1)
        drawBoard(l)

        move = board1.getMove(board1.getTurn())

        count = 0
        if board1.checkMove(move):
            x,count= board1.horizontal(move) 
            y,count = board1.verticle(move)
            z,count = board1.diagonal(move)
            if x or y or z:
                board1.setPiece(move,board1.turn)
                if board1.getTurn() == 'O':
                    if board1.isWinner(board1.getTurn()):
                        print(f'Congratulations {board1.getTurn()} has won. Play again?')
                    else:
                        board1.setTurn('X')
                else:
                    if board1.isWinner(board1.getTurn()):
                        print(f'Congratulations {board1.getTurn()} has won. Play again?')
                    else:
                        board1.setTurn('O')
            else:
                print('Not valid')
        else:
                print('Not a valid Move')

        
elif game.startswith('c'):
        while True:
            count = 0

            print('Reversi')


            drawBoard(board1)
            
            if player == 'p':
                print('Players turn')
                move = board1.getMove(board1.getTurn())
                if board1.checkMove(move):
                    z,count = board1.diagonal(move)
                    x,count= board1.horizontal(move) 
                    y,count = board1.verticle(move)
                    
                    if x or y or z:
                        board1.setPiece(move,board1.getTurn())
                        if board1.getTurn() == 'O':
                            if board1.isWinner(board1.getTurn()):
                                print(f'Congratulations {board1.getTurn()} has won. Play again?')
                            else:
                                board1.setTurn('X')
                                player = 'c'
                        else:
                            if board1.isWinner(board1.getTurn()):
                                print(f'Congratulations {board1.getTurn()} has won. Play again?')
                            else:
                                board1.setTurn('O')
                                player = 'c'
                    else:
                        print('Not valid')
                else:
                    print('Not valid move')
            elif player == 'c':
                print('computers turn')
                move = board1.getCompMove()
                z,count3 = board1.diagonal(move)
                x,count1 = board1.horizontal(move)
                y,count2 = board1.verticle(move)

                board1.setPiece(move,board1.turn)
                if board1.getTurn() == 'O':
                    if board1.isWinner(board1.getTurn()):
                        print(f'Congratulations {board1.getTurn()} has won. Play again?')
                    else:
                        board1.setTurn('X')
                        player = 'p'
                else:
                    if board1.isWinner(board1.getTurn()):
                        print(f'Congratulations {board1.getTurn()} has won. Play again?')
                    else:
                        board1.setTurn('O')
                        player = 'p'
