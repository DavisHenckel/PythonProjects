class Card:

    def __init__ (self, suit, value):
        self.suit = suit
        self.value = value
    
    def __str__(self):
        return('{} of {}'.format(self.value, self.suit))

    #Compares a card for equality
    def isCardEqual(self, card1): 
        if self.value == card1.value and self.suit == card1.suit:
            return True
        else:
            return False