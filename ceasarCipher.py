SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
MAX_KEY = len(SYMBOLS)

def getMove():
    x = True
    while x == True:
        print('Would you like to encrypt or decrypt?')
        res = input().lower()
        if res.startswith('e'):
            x = False
            print('Enter phrase to be encrypted')
            phrase = input()
            print('enter key to encrypt by')
            key = int(input())
            print(encrypt(phrase, key))
            print('Would you like to continue?')
            if input().lower().startswith('y'):
                x = True

        elif res.startswith('d'):
            x = False
            print('Enter phrase to be decrypted')
            phrase = input()
            print('enter key to decrypt by')
            key = int(input())
            print(decrypt(phrase,key))
            print('Would you like to continue?')
            if input().lower().startswith('y'):
                x = True  

        elif res.startswith('b'):
            x = False
            print('Enter phrase to be deciphered')
            phrase = input()
            for key in range(MAX_KEY):
                print(decrypt(phrase, key))
        else:
            print('not a valid response. Try again')


def encrypt(phrase,key):
    encrypted = ''
    for i in phrase:
        if i == ' ':
            encrypted += ' '
        else:
            start = SYMBOLS.find(i)
            if (start + key) < MAX_KEY:
                end = SYMBOLS[start + key]
                encrypted += end
            else:
                x = MAX_KEY - start
                ind = key - x
                end = SYMBOLS[ind]
                encrypted += end
    return encrypted
def decrypt(phrase,key):
    decrypted = ''
    for i in phrase:
        if i == ' ':
            decrypted += ' '
        else:
            start = SYMBOLS.find(i)
            if (start - key) >= 0:
                end = SYMBOLS[start - key]
                decrypted += end
            else:
                x = start - key
                ind = x + MAX_KEY
                end = SYMBOLS[ind]
                decrypted += end
    return decrypted


getMove()