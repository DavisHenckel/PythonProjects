import string

def printBlankBoard():
    print("  |  |  ")
    print("________")
    print("  |  |  ")
    print("________")
    print("  |  |  ")

def printActiveBoard(board):
    for j in range(3): #Nested for loop to run 9 times
        #1st Row
        for i in range(3):
            if (j == 0):
                print(board[i], end = '')
                if(i == 2):
                    print('') 
                    print('__________')
                    continue
                print(' | ', end = '')

            #2nd Row
            if (j == 1):
                print(board[i+3], end = '')
                if(i == 2):
                    print('')
                    print('__________')        
                    continue
                print(' | ', end = '')

            #3rd Row
            if (j == 2):
                print(board[i+6], end = '')
                if(i == 2):
                    print('')
                    continue
                print(' | ', end = '')


def playerInput(board):
    userInput = input("Enter a location (1-9 on the numpad)")
    print('adding', userInput)

def isGameOver(board): #0 indicates game is over. 1 indicates game is not over
    if(1 == 0):
        return 1
    else:
        return 0

def clearBoard(board):
    for i in range(9):
        board[i] = ' '
        return board
#Main
testBoard = [' ', ' ', 'X', ' ', ' ', ' ', 'O', ' ', ' ']
print ('Welcome to Tic-Tac-Toe!')
print ('1. New Game')
print ('2. Exit')
userInput = input()

if (userInput == '1'):
    print('Starting a new game')
    clearBoard(testBoard)
    printActiveBoard(testBoard)
    userInput = input('Player 1, choose X or O\n')
    while (userInput != 'X' and userInput != 'O'):
        userInput = input('Please choose X or O\n')
    if (userInput == 'X'):
        print ('Player 1 is X, Player 2 is O')
    elif (userInput == 'O'):
        print ('Player 1 is O, Player 2 is X')    

elif (userInput == '2'):
    print('Exiting')
    exit(0)

while (isGameOver(testBoard) == 0):
    playerInput(testBoard)

