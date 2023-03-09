import random
def getGuess(num, count):
    if count == 0:
        print('Sorry, You ran out of guesses\nWould you like to play again(yes or no)?')
        if input().lower().startswith('y'):
            num = getNum()
            count = 6
            print(f'Alright {name}, I am thinking of a number between 1 and 20')
            return num, True, count
        else:
            return 1, False, count
    else:
        guess = int(input())
        if guess > num:
            count -= 1
            print(f'Too High! {count} guesses left') 
            return num, True, count
        elif guess < num:
            count -= 1
            print(f'Too low! {count} guesses left')
            return num, True, count  
        else:
            count -=1
            print(f'Correct! The number was {num}\nyou got it in {6-count} attempts\nWould you like to play again(yes or no)?')
            if input().lower().startswith('y'):
                num = getNum()
                count = 6
                print(f'Alright {name}, I am thinking of a number between 1 and 20')
                return num, True, count
            else:
                return 1, False, count
def getNum():
    return random.randint(1,20)
gameIsPlaying = True
print('Hello. Welcome to guess the number\nWhat is your name')
name = input()
num = getNum()
print(f'Alright {name}, I am thinking of a number between 1 and 20')
count = 6
while gameIsPlaying == True:
    num, gameIsPlaying, count = getGuess(num, count)


    

