import random
HANGMAN_PICS = [
'''
______
|     |
      |
      |
      |
      |
  ____|____  
''',
'''
______
|     |
O     |
      |
      |
      |
  ____|____  
''',
'''
______
|     |
O     |
|     |
      |
      |
  ____|____  
''',
'''
______
|     |
O     |
|     |
|     |
      |
  ____|____
''',
'''
 ______
 |     |
 O     |
 |     |
 |     |
/      |
   ____|____
''',
'''
 _____
 |    |
 O    |
 |    |
 |    |
/ \   |
   ___|____
''',
'''
 ______
 |     |
 O     |
\|     |
 |     |
/ \    |
   ____|____
''',
'''
 ______
 |     |
 O     |
\|/    |
 |     |
/ \    |
   ____|____
''']
words = ['express','combination','provide','examination','expenditure','crevice','increase','dictate','repetition',
'imagine','include','private','perform','achieve','experience','genetic','custody','assault','feminist','meeting','confine','unlawful','curriculum','designer'
,'dependence','reality','understand','salvation','cutting','teacher','ancestor','effective','amputate','crackpot','victory','discount','lecture','exercise','countryside','cultural']
def getRandomWord(wordList):
    wordIndex = random.randint(0, len(wordList)- 1)
    return wordList[wordIndex]

def displayBoard(missedLetters, correctLetters, secretWord):
    print(HANGMAN_PICS[len(missedLetters)])
    print()

    print('Missed letters:', end=' ')
    for letter in missedLetters:
        print(letter, end=' ')
    print()

    blanks ='_'*len(secretWord)

    for i in range(len(secretWord)):
        if secretWord[i] in correctLetters:
            blanks = blanks[:i] + secretWord[i] + blanks[i+1:]

    for letter in blanks:
        print(letter, end=' ')
    print()

def getGuess(alreadyGuessed,guess):
    while True:
        if len(guess) != 1:
            return 'Please enter a single letter.'
        elif guess in alreadyGuessed:
            return 'You have already guessed that letter. Choose again.'
        elif guess not in 'abcdefghijklmnopqrstuvwxyz':
            return 'please enter a LETTER.'
        else:
            return guess

def playAgain():
    print('Do you want to play again? (yes or no)')
    return input().lower().startswith('y')

'''
print('H A N G M A N')
missedLetters = ''
correctLetters = ''
secretWord = getRandomWord(words)
gameIsDone = False

while True:
    displayBoard(missedLetters, correctLetters, secretWord)
    guess = getGuess(missedLetters + correctLetters)

    if guess in secretWord:
        correctLetters = correctLetters+ guess

        foundAllLetters = True
        for i in range(len(secretWord)):
            if secretWord[i] not in correctLetters:
                foundAllLetters = False
        if foundAllLetters:
            print(f'Yes! The secret word is "{secretWord}"! You have won!')
            gameIsDone = True
    else:
        missedLetters = missedLetters + guess

        if len(missedLetters) == len(HANGMAN_PICS) - 1:
            displayBoard(missedLetters, correctLetters, secretWord)
            print('You have run out of guesses!\nAfter '+
                str(len(missedLetters)) + ' missed guesses and ' +
                str(len(correctLetters)) + ' correct guesses, the word was"' + secretWord +'"')
            gameIsDone = True

    if gameIsDone == True:
            if playAgain():
                missedLetters = ''
                correctLetters = ''
                gameIsDone = False
                secretWord = getRandomWord(words)
            else:
                break
                
'''