import random
print('Welcome to Tic Tac Toe')

def drawBoard(board):
    print(board[7] + '|' + board[8] + '|' + board[9])
    print('-+-+-')
    print(board[4] + '|' + board[5] + '|' + board[6])
    print('-+-+-')
    print(board[1] + '|' + board[2] + '|' + board[3])
def getUserletter():
    letter = ''
    while not (letter == 'X' or letter == 'O'):
        print('Would you like to be X or O?')
        letter = input().upper()
        if letter == 'X':
            return ['X','O']
        else:
            return ['O','X']
def whoGoesFirst():
    choice = random.randint(0,1)
    if choice == 0:
        return 'Computer'
    else:
        return 'Player'
def makeMove(board, letter, move):
    board[move] = letter

def isWinner(bo,le):
    return ((bo[4]==le and bo[5]== le and bo[6]==le) or
            (bo[1]==le and bo[2]==le and bo[3]==le) or
            (bo[7]==le and bo[8] == le and bo[9] ==le)or
            (bo[1]==le and bo[4]==le and bo[7]==le)or
            (bo[2]==le and bo[5]==le and bo[8]==le)or
            (bo[3]==le and bo[6]==le and bo[9]==le)or
            (bo[1]==le and bo[5]==le and bo[9]==le)or
            (bo[3]==le and bo[5]==le and bo[7]==le))
def getBoardCopy(board):
    boardCopy = []
    for i in board:
        boardCopy.append(i)
    return boardCopy

def isSpaceFree(board, move):
    return board[move] == ' '

def getPlayerMove(board):
    move = ' '
    while move not in '1 2 3 4 5 6 7 8 9'.split() or not isSpaceFree(board, int(move)):
        print('Enter a number between 1-9')
        move = input()
    return int(move)

def chooseRandomMoveFromList(board, movesList):
    possibleMoves = []
    for i in movesList:
        if isSpaceFree(board, i):
            possibleMoves.append(i)
    if len(possibleMoves) != 0:
        return random.choice(possibleMoves)
    else:
        return None

def getComputerMove(board, computerLetter):
    if computerLetter == 'X':
        playerLetter = 'O'
    else:
        playerLetter = 'X'

    for i in range(1, 10):
        boardCopy = getBoardCopy(board)
        if isSpaceFree(boardCopy, i):
            makeMove(boardCopy, computerLetter, i)
            if isWinner(boardCopy, computerLetter):
                return i
    for i in range(1, 10):
        boardCopy = getBoardCopy(board)
        if isSpaceFree(boardCopy, i):
            makeMove(boardCopy, playerLetter, i)
            if isWinner(boardCopy, playerLetter):
                return i
    move = chooseRandomMoveFromList(board,[1,3,7,9])
    if move != None:
        return move
    if isSpaceFree(board, 5):
        return 5
    return chooseRandomMoveFromList([2, 4, 6, 8])

def isBoardFull(board):
    for i in range(1,10):
        if isSpaceFree(board, i):
            return False
    return True


while True:
    theBoard = [' '] * 10
    playerLetter, computerLetter = getUserletter()
    turn = whoGoesFirst()
    print(f'the {turn} will go first')
    gameIsPlaying = True
    while gameIsPlaying:
        if turn == 'Player':
            drawBoard(theBoard)
            move = getPlayerMove(theBoard)
            makeMove(theBoard, playerLetter, move)

            if isWinner(theBoard, playerLetter):
                drawBoard(theBoard)
                print('Hooray! You have won the game!')
                gameIsPlaying = False
            else:
                if isBoardFull(theBoard):
                    drawBoard(theBoard)
                    print('Aww it was a Tie!')
                    break
                else:
                    turn = 'Computer'
        else:
            move = getComputerMove(theBoard, computerLetter)
            makeMove(theBoard, computerLetter, move)

            if isWinner(theBoard, computerLetter):
                drawBoard(theBoard)
                print('Unfortunatly, the computer has beat you :/')
                gameIsPlaying = False
            else:
                if isBoardFull(theBoard):
                    drawBoard(theBoard)
                    print('Aww it was a Tie!')
                    break
                else:
                    turn = 'Player'
    print('Do you want to play again? (yes or no)')
    if not input().lower().startswith('y'):
        break
            