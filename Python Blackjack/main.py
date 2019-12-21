import deck
import player
import dealer

import random
from os import system, name
from time import sleep

def clear():
    
    if name == 'nt': #Windows systems
        _= system('cls')
    else: #Unix Systems including MacOS
        _= system('clear')


def buildGame(aPlayer, aDealer, gameDeck):
    aPlayer.clearHand()
    aDealer.clearHand()
    gameDeck.shuffleDeck()
    aDealer.addToHand(gameDeck.getCard(0))
    aDealer.addToHand(gameDeck.getCard(1))
    aPlayer.addToHand(gameDeck.getCard(2))
    aPlayer.addToHand(gameDeck.getCard(3))

#Returns the bet after starting the game
def startRound(deck, theDealer, theVictim):
    clear()
    if theVictim.chipBalance == 0:
        print('You\'re out of money. Better luck next time.')
        return -1
    print("Welcome to the casino {}\nEvery player starts with 500 chips. Here is what you have currently:\n{}".format(theVictim.playerName, theVictim))
    sleep(3)
    buildGame(theVictim, theDealer, deck)
    theBet = 0
    while(True):
        theBet = int(input("Please place your bet\n"))
        result = theVictim.placeBet(theBet)
        if result == False:
            continue #retry at the next iteration
        else:
            break #bet was successfully made, break out of the loop 

    sleep(2)
    clear()
    print("Lets start the round!")
    sleep(1)
    theVictim.printHand()
    sleep(1)
    theDealer.printHiddenHand()
    print("Your hand's total value is: {}".format(theVictim.totalHandValue()))
    print("The dealer's hand's value is at least: {}".format(theDealer.visualHandValue()))
    return theBet

#Returns True if the round is over, False if not.
def checkWinHit(theVictim, theDealer, theBet):
    if theVictim.totalHandValue() == 21:
        print('BLACKJACK! YOU WIN!')
        sleep(2)
        theVictim.printHand()
        theVictim.increaseMoney(theBet * 2)
        print (theVictim)
        sleep(1)
        return True

    elif theVictim.totalHandValue() > 21:       
        theDealer.printVisibleHand()
        theVictim.printHand()
        sleep(2)
        print('BUST! YOU LOSE!') 
        print (theVictim)
        sleep(1)
        return True

    elif theDealer.totalHandValue() > 21: 
        theDealer.printVisibleHand()
        theVictim.printHand()
        theVictim.increaseMoney(theBet * 2)  
        sleep(2)
        print ('THE DEALER IS OVER 21, YOU WIN THIS TIME...')
        print (theVictim)
        sleep(1)
        return True
    return False

def checkWinStand(theVictim, theDealer, theBet):
    distanceDealer = abs(theDealer.totalHandValue() - 21)
    distancePlayer = abs(theVictim.totalHandValue() - 21)
    if theDealer.totalHandValue() > 21:
        theDealer.printVisibleHand()
        theVictim.increaseMoney(theBet * 2)
        sleep(2)
        print('DEALER IS OVER 21. YOU WIN THIS TIME...')
        print (theVictim)
        sleep(1)
    else:
        if distanceDealer > distancePlayer:
            theDealer.printVisibleHand()
            theVictim.printHand()
            theVictim.increaseMoney(theBet * 2)
            sleep(2)
            print('YOU ARE CLOSER TO 21, YOU WIN THIS TIME...')
            print (theVictim)
            sleep(1)
        else:
            theDealer.printVisibleHand()
            theVictim.printHand()
            sleep(2)
            print('YOU LOSE! THE DEALER IS CLOSER TO 21')
            print (theVictim)
            sleep(1)

#Returns True if the player wantst to play again, False if not.
def playAgain():
    while(True):
        anInput = input('Would you like to play another hand? (y/n)\n').lower()
        if(anInput == 'n'):
            return False
        elif(anInput == 'y'):
            return True
        else:
            print('Please enter \'y\' or \'n\'')
            continue

#Returns hit or stand depending on what the player wants to do
def hOrS():
    while (True):
        playerMove = input('Would you like to hit or stand\n').lower()
        if(playerMove == 'hit'):
            return 'hit'
        elif(playerMove == 'stand'):
            return 'stand'
        else:
            print('Please enter hit or stand')
            continue

if __name__ == "__main__":
    gameDeck = deck.Deck() #Create the deck that will be used throughout the game
    clear()
    print('----------------------------------------------------------------------------------------------')
    print('Hello\nWelcome to the worlds greatest game of blackjack. What is your name?')
    print('----------------------------------------------------------------------------------------------')
    userName = input()
    clear()
    theDealer = dealer.Dealer() #Create the dealer
    theVictim = player.Player(userName) #Create the player
    counter = 0 #keeps track of which card index to add
    while(True):
        theBet = startRound(gameDeck, theDealer, theVictim) #Start the game and assign the bet value
        if(theBet == -1):
            break
        if(theVictim.totalHandValue() ==  21):
            checkWinHit(theVictim, theDealer, theBet)
        playerMove = hOrS()
        clear()
        if (playerMove == 'hit'):
            theVictim.addToHand(gameDeck.getCard(counter + 4)) #Add a card to the players hand
            counter += 1 #Increment counter
            print('Your hand\'s total value is: {}'.format(theVictim.totalHandValue()))
            theDealer.addToHand(gameDeck.getCard(counter + 4)) #Add a card to the dealers hand
            counter += 1 #Increment counter
            isRoundOver = checkWinHit(theVictim, theDealer, theBet)
            if isRoundOver == True:
                again = playAgain()
                if(again == True):
                    continue
                else:
                    break

        elif (playerMove == 'stand'):
            theDealer.addToHand(gameDeck.getCard(counter + 4))
            counter += 1
            checkWinStand(theVictim, theDealer, theBet)
            again = playAgain()
            if(again == True):
                continue
            else:
                break

    print("Thanks for playing!")

        


    
    