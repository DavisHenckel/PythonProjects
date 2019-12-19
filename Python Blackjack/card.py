class Card:

    def __init__ (self, suit, value):
        self.suit = suit
        self.value = value
    
    def __str__(self):
        print('{} of {}'.format(self.value, self.suit))