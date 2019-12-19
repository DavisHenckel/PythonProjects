from os import system
from time import sleep
import random

def chooseFirst():
    return random.choice([1, 2])
#clears terminal output
def clear():
    system('cls')

#Prints the Current State of the game
def printActiveBoard(board):
    for j in range(3): #Nested for loop to run 9 times
        #1st Row
        for i in range(3):
            if (j == 0):
                print(board[i], end = '')
                if(i == 2):
                    print('') 
                    print('---------')
                    continue
                print(' | ', end = '')

            #2nd Row
            if (j == 1):
                print(board[i+3], end = '')
                if(i == 2):
                    print('')
                    print('---------')        
                    continue
                print(' | ', end = '')

            #3rd Row
            if (j == 2):
                print(board[i+6], end = '')
                if(i == 2):
                    print('')
                    continue
                print(' | ', end = '')

def isMoveValid(board, location):
    if(board[location] == ' '):
        return True
    return False

#Returns 1 if an invalid move is attempted to be made returns 0 if a valid move has been made
def playerInput(board, playerTurn):
    userInput = input("Enter a location (1-9 on the numpad)")
    charToInsert = 'X'
    if(playerTurn == 1):
        charToInsert = 'O'
    if(userInput == '1'):
        if (isMoveValid(board, 6) == True):
            board[6] = charToInsert
            return 0
        print('Cannot play there, that location is occupied')
        return 1 
    elif(userInput == '2'):
        if (isMoveValid(board, 7) == True):
            board[7] = charToInsert
            return 0
        print('Cannot play there, that location is occupied')
        return 1
    elif(userInput == '3'):
        if (isMoveValid(board, 8) == True):
            board[8] = charToInsert
            return 0
        print('Cannot play there, that location is occupied')
        return 1
    elif(userInput == '4'):
        if (isMoveValid(board, 3) == True):
            board[3] = charToInsert
            return 0 
        print('Cannot play there, that location is occupied')
        return 1 
    elif(userInput == '5'):
        if (isMoveValid(board, 4) == True):
            board[4] = charToInsert
            return 0
        print('Cannot play there, that location is occupied')
        return 1
    elif(userInput == '6'):
        if (isMoveValid(board, 5) == True):
            board[5] = charToInsert
            return 0 
        print('Cannot play there, that location is occupied')
        return 1
    elif(userInput == '7'):
        if (isMoveValid(board, 0) == True):
            board[0] = charToInsert
            return 0 
        print('Cannot play there, that location is occupied')
        return 1
    elif(userInput == '8'):
        if (isMoveValid(board, 1) == True):
            board[1] = charToInsert
            return 0 
        print('Cannot play there, that location is occupied')
        return 1
    elif(userInput == '9'):
        if (isMoveValid(board, 2) == True):
            board[2] = charToInsert
            return 0 
        print('Cannot play there, that location is occupied')
        return 1
    else:
        print('Invalid Input. Please enter 1-9')
        return 1

def isGameOver(board): #0 indicates game is active. 1 indicates game is  over.
    #Checking if cats game
    notFull = 0 # notFull set to false
    for i in range(9):
        if (board[i] == ' '): #If there is 1 empty space, notFull is true
            notFull = 1
    if (notFull == 0):
        print('Cats Game :(')
        return 1

    #Checking Horizontal
    if(board[0] == board[1] and board[0] == board[2] and board[0] != ' '):
        print('{} wins! Game Over!'.format(board[1]))
        return 1
    elif(board[3] == board[4] and board[3] == board[5] and board[3] != ' '):
        print('{} wins! Game Over!'.format(board[3]))
        return 1
    elif(board[6] == board[7] and board[6] == board[8] and board[6] != ' '):
        print('{} wins! Game Over!'.format(board[6]))
        return 1

    #Checking Vertical
    elif(board[0] == board[3] and board[0] == board[6] and board[6] != ' '):
        print('{} wins! Game Over!'.format(board[0]))
        return 1
    elif(board[1] == board[4] and board[1] == board[7] and board[1] != ' '):
        print('{} wins! Game Over!'.format(board[1]))
        return 1
    elif(board[2] == board[5] and board[2] == board[8] and board[2] != ' '):
        print('{} wins! Game Over!'.format(board[2]))
        return 1
    
    #Checking Diagonal
    elif(board[0] == board[4] and board[0] == board[8] and board[0] != ' '):
        print('{} wins! Game Over!'.format(board[0]))
        return 1
    elif(board[6] == board[4] and board[6] == board[2] and board[6] != ' '):
        print('{} wins! Game Over!'.format(board[6]))
        return 1
    else:
        return 0

#Main
def main():
    userInput = ''
    while (userInput != '2'):
        theBoard = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
        print ('Welcome to Tic-Tac-Toe!')
        print ('1. New Game')
        print ('2. Exit')
        userInput = input()

        if (userInput == '1'):
            print('Starting a new game')
            printActiveBoard(theBoard)
            playerChar = 0
            goesFirst = chooseFirst() #Pick who goes first
            userInput = input('Player 1, choose X or O\n')
            while (userInput != 'X' and userInput != 'O'):
                userInput = input('Please choose X or O\n')
            if (userInput == 'X'):
                print ('Player 1 is X, Player 2 is O')
                playerChar = 0 #First move is X
                print('Player {} goes first'.format(goesFirst))
                if(goesFirst == 2): #if player 2 is going first, set the first move to be the opposite of player 1
                    playerChar = 1 
            elif (userInput == 'O'):
                print ('Player 1 is O, Player 2 is X')
                playerChar = 1 #First move is O
                print('Player {} goes first'.format(goesFirst))
                if(goesFirst == 2): #if player 2 is going first, set the first move to be the opposite of player 1
                    playerChar = 0    

        elif (userInput == '2'):
            print('Exiting')
            exit(0)

        while (isGameOver(theBoard) == 0): #Play until the game is over
            checkVal = playerInput(theBoard, playerChar)
            printActiveBoard(theBoard)
            if(checkVal == 0): #Checks return value of player input to see if a valid move was made, if not, then the user goes again
                if(playerChar == 0): #Switches between placing O and X on the board
                    playerChar = 1
                    continue
                playerChar = 0

        userInput = input('Would you like to play again? (y/n)')
        if(userInput == 'n' or userInput == 'N'):
            userInput = '2' #assign userInput 2 so it exits upon the next iteration

main()
