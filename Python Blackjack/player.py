import card

class Player:
    def __init__(self, playerName):
        self.playerName = playerName
        self.chipBalance = 500
        self.playerHand = []
    
    #Returns true if the bet was made successfully, false if not
    def placeBet(self, amount):
        if amount > self.chipBalance:
            print('Cannot make that bet. You don\'t have enough chips you peasant')
            return False #Returns false if the bet was not successfully made.
        else:
            self.chipBalance -= amount
            print('Bet made. Your chip balance is now {}'.format(self.chipBalance))
            return True
    
    def addToHand(self, cardToAdd):
        self.playerHand.append(cardToAdd)
    
    def printHand(self):
        print('PLAYER HAND')
        print ('--------')
        for each in self.playerHand:
            print(each)
        print ('--------')
    
    def totalHandValue(self):
        totalVal = 0
        for eachCard in self.playerHand:
            totalVal += eachCard.value 
        return totalVal
    
    def increaseMoney(self, amount):
        self.chipBalance += amount

    def __str__(self):
        return('{} has {} chips\n'.format(self.playerName, self.chipBalance))

    def clearHand(self):
        self.playerHand.clear()