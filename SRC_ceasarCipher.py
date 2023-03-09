SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
MAX_KEY_SIZE = len(SYMBOLS)

def getMode():
    while True:
        print('Do you wish to encrypt or decrypt a message')
        mode = input().lower()
        if mode in ['encrypt','e','decrypt','d','brute','b']:
            return mode
        else:
            print('Enter either "encrypt" or "e" or "decrypt" or "d')

def getMessage():
    print('Enter your message:')
    return input()

def getKey():
    key = 0
    while True:
        print(f'Enter the key number (1-{MAX_KEY_SIZE})')
        key = int(input())
        if (key >= 1 and key <= MAX_KEY_SIZE):
            return key
        
def getTranslatedMessage(mode,message,key):
    if mode[0] != 'b':
        if mode[0] == 'd':
            key = -key
        translated = ''
        for symbol in message:
            symbolIndex = SYMBOLS.find(symbol)
            if symbolIndex == -1:
                translated += symbol
            else:
                symbolIndex += key
                if symbolIndex >= len(SYMBOLS):
                    symbolIndex -= len(SYMBOLS)
                elif symbolIndex < 0:
                    symbolIndex += len(SYMBOLS)
                translated += SYMBOLS[symbolIndex]
        return translated
    else:
        for key in range(MAX_KEY_SIZE):
            print(getTranslatedMessage('d',message,key))
key = 0
mode = getMode()
message = getMessage()
if mode[0] != 'b':
    key = getKey()
print('Your translated text is:')
print(getTranslatedMessage(mode,message,key))