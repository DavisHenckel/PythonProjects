import string

def printBlankBoard():
    print("  |  |  ")
    print("________")
    print("  |  |  ")
    print("________")
    print("  |  |  ")

def printActiveBoard(board):
    
    for j in range(3): #Nested for loop to run 9 times
        for i in range(3):
            print(board[i], end = '')
            if (board[i] == ' '):
                print(board[i], end = '')
            if(i == 2):
                print('')
                if (j < 2): #if we are on the last line, do not print the underline
                    print(' __________')
                continue
            print(' | ', end = '')


def playerInput():
    userInput = input("Enter a location (1-9 on the numpad respectively)")

def winCondition(board):
    print ('Hello')

#Main
testBoard = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
printActiveBoard(testBoard)
