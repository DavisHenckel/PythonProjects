import deck
import player
import dealer

import random
from os import system, name

def startGame(aPlayer, aDealer, gameDeck):
    gameDeck.shuffleDeck()
    aDealer.addToHand(gameDeck.getCard(0))
    aDealer.addToHand(gameDeck.getCard(1))
    aPlayer.addToHand(gameDeck.getCard(2))
    aPlayer.addToHand(gameDeck.getCard(3))


if __name__ == "__main__":
    system('cls')
    gameDeck = deck.Deck() #create the deck that will be used throughout the game
    print('----------------------------------------------------------------------------------------------')
    userName = input('Hello\nWelcome to the worlds greatest game of blackjack. What is your name?\n----------------------------------------------------------------------------------------------\n')
    system('cls')
    theVictim = player.Player(userName)
    theDealer = dealer.Dealer()
    print("Welcome to the game {}\nEvery player starts with 500 chips. Here is what you are to the system:\n{}".format(theVictim.playerName, theVictim))
    startGame(theVictim, theDealer, gameDeck)
    theVictim.printHand()
    theDealer.printHand()
    
    