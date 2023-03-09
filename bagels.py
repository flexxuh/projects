import random
def getNums():
    x = random.randint(0,9)
    y = random.randint(0,9)
    z = random.randint(0,9)
    while x == z or y == x or y == z: 
        if x == z:
            x = random.randint(0,9)
        elif y == x:
            y = random.randint(0,9)
        elif y == z:
            z = random.randint(0,9)
    secretNum = [x,y,z]
    return secretNum

def getGuess(numGuess):
    while True:
        print(f'\nGuess #{numGuess}')
        guess = input()
        if isNum(guess):
            return guess
def isNum(guess):
    if not guess.isdigit():
        print('Please Enter a Number')
        return False
    elif len(guess) > 3:
        print('Please Enter a 3 Digit Number')
        return False
    else:
        return True
def checkGuess(guess,secretNum, numGuess):
    x = 0
    y = []
    if numGuess == 10:
        for i in secretNum:
            y.append(str(i))
        print(f'Aww you lose. The number I was Thinking of was: {"".join(y)}')
        print('Would you like to play again?(yes or no)')
        numGuess = 1
        return input().lower().startswith('y'),numGuess
    else:
        for i in enumerate(guess):
            if int(i[1]) in secretNum:
                ind = secretNum.index(int(i[1]))
                if ind == i[0]:
                    print('Fermi', end=' ')
                    x += 1
                else:
                    print('Pico',end=' ')
                    x += 1
        if x == 0:
            print('Bagels',end='')
            return True,numGuess
        elif x == 3:
            print(f'You win. You got it in {numGuess} guesses!\nWould you like to play again?(yes or no)')
            numGuess = 1
            return input().lower().startswith('y'),numGuess
        elif x >= 1:
            return True,numGuess

print('Welcome to Bagels. I have just thought of a 3 digit number that you must guess')
print('Here are the clues I give\n    Bagels: None of the 3 digits guessed are correct\n    Pico: One of the digits is in the secret number but in the wrong place\n    Fermi: The guess has a correct digit in the correct place')

print('Please guess a 3 digit number')

game = True
numGuess = 1
while game == True:
    if numGuess == 1:
        secretNum = getNums()
    guess = getGuess(numGuess)
    numGuess += 1
    game, numGuess = checkGuess(guess,secretNum,numGuess)