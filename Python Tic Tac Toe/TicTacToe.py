import string

def printBlankBoard():
    print(" ' ' | ' ' | ' ' ")
    print("__________________")
    print(" ' ' | ' ' | ' ' ")
    print("__________________")
    print(" ' ' | ' ' | ' ' ")

def printActiveBoard(board):
    for i in range(9):
        print (board[i])

def playerInput():
    userInput = input("Enter a location (1-9 on the numpad respectively)")

def winCondition(board):
    print ('Hello')

#Main
testBoard = { '#', 'X', '0', 'X', 'X', 'X', 'X', 'X', 'X'}
printActiveBoard(testBoard)
