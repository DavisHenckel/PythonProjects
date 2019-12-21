import card

class Dealer:
    def __init__(self):
        self.dealerHand = []

    def addToHand(self, cardToAdd):
        self.dealerHand.append(cardToAdd)

    def printHiddenHand(self):
        print('DEALER HAND')
        print ('--------')
        print (self.dealerHand[0])
        start = 0 
        while start < len(self.dealerHand) - 1:
            print('*Hidden*')
            start += 1
        print ('--------')
    
    def printVisibleHand(self):
        print('DEALER HAND')
        print ('--------')
        for eachCard in self.dealerHand:
            print (eachCard)
        print ('--------')

    def visualHandValue(self):
        return self.dealerHand[0].value
    
    def totalHandValue(self):
        totalVal = 0
        for eachCard in self.dealerHand:
            totalVal += eachCard.value 
        return totalVal
    
    def clearHand(self):
        self.dealerHand.clear()
        
