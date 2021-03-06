import random
import card

suits =('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks =('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values ={'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10,
         'Queen':10, 'King':10, 'Ace':11}

class Deck:

    def __init__(self):
        self.deck = []
        for suit in suits:
            for num in values:
                tempCard = card.Card(suit, values[num])
                self.deck.append(tempCard)
        self.current = 0
        self.end = 51
        return
    
    def __iter__(self): #Defines the iteration and uses __next__ to iterate through the deck
        return self
    
    def __next__(self): #Allows the deck to be iterable
        if self.current > self.end:
            raise StopIteration
        else:
            self.current += 1
            return self.current - 1

    #Returns a card at a given index            
    def getCard(self, index):
        tempCard = self.deck[index]
        return tempCard

    def shuffleDeck(self):
        random.shuffle(self.deck)
        return
    