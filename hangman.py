import random
men = [
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
______
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
''',
'''
 ______
 |     |
[O     |
\|/    |
 |     |
/ \    |
   ____|____
''',
'''
 ______
 |     |
[O]    |
\|/    |
 |     |
/ \    |
   ____|____
''']
words = ['express','combination','provide','examination','expenditure','crevice','increase','dictate','repetition',
'imagine','include','private','perform','achieve','experience','genetic','custody','assault','feminist','meeting','confine','unlawful','curriculum','designer'
,'dependence','reality','understand','salvation','cutting',
'teacher','ancestor','effective','amputate','crackpot','victory','discount','lecture','exercise','countryside','cultural']
def secretWord(wordsList):
    l = random.randint(0,len(wordsList))
    return wordsList[l]
def blanks(chosen):
    blank = '_ ' * len(chosen)
    return blank
def display_board(miss_letters):
    print(men[len(miss_letters)])
def getGuess(miss_letters):
    print('Guess a letter')
    guess = input().lower()
    if len(guess) > 1:
        print('Please enter A single letter')
    elif guess not in 'abcdefghijklmnopqrstuvwxyz':
        print('Please enter a letter')
    elif guess in miss_letters:
        print('you already guessed that letter. Try again')
    else:
        return guess
def check_guess(guess,letters,miss_letters,blank):
    if guess in letters:
        for i in enumerate(letters):
            if i[1] == guess:
                blank[i[0]*2] = guess
    else:
        if isinstance(guess, str):
            miss_letters.append(guess) 
def play_again():
    print('Would you like to play again (yes or no)')
    return input().lower().startswith('y')
def game(chosen,miss_letters,blank,letters):
    difficulty = 'x'
    while difficulty not in 'EMH':
        print('Enter a difficulty: E - Easy, M - Medium, H - Hard')
        difficulty = input().upper()
    if difficulty == 'M':
        del men[8]
        del men[7]
        difficulty = 'x'
    if difficulty == 'H':
        del men[8]
        del men[7]
        del men[5]
        del men[3]
        difficulty = 'x'
    if difficulty =='E':
        difficulty ='X'
    while '_' in blank:
        print(miss_letters)
        if len(miss_letters) < len(men):
            display_board(miss_letters)
            print(''.join(blank))
            guess = getGuess(miss_letters)
            check_guess(guess,letters,miss_letters,blank)
        else:
            print(f'You lose. Secret word was:{chosen}')
            if play_again():
                miss_letters = []
                chosen = secretWord(words)
                letters = list(chosen)
                blank = list(blanks(chosen))
            else:
                exit()
    print(f'Good job. you win\nSecret word was {chosen}')      
print('H A N G M A N')
chosen = secretWord(words)

letters = list(chosen)
miss_letters = []
blank = list(blanks(chosen))

game(chosen,miss_letters,blank,letters)
if play_again():
    miss_letters = []
    chosen = secretWord(words)
    letters = list(chosen)
    blank = list(blanks(chosen))
    game(chosen,miss_letters,blank,letters)
else:
    exit()

