import card

class Player:
    def __init__(self, playerName):
        self.playerName = playerName
        self.chipBalance = 500
        self.playerHand = []
    
    def placeBet(self, amount):
        if amount > self.chipBalance:
            print('Cannot make that bet. You don\'t have enough chips you peasant')
        else:
            self.chipBalance -= amount
            print('Bet made. Your chip balance is now {}'.format(self.chipBalance))
    
    def addToHand(self, cardToAdd):
        self.playerHand.append(cardToAdd)
    
    def printHand(self):
        print('PLAYER HAND')
        print ('--------')
        for each in self.playerHand:
            print(each)
        print ('--------')

    def __str__(self):
        return('{} has {} chips\n'.format(self.playerName, self.chipBalance))