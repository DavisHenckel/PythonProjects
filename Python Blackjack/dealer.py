import card

class Dealer:
    def __init__(self):
        self.dealerHand = []

    def addToHand(self, cardToAdd):
        self.dealerHand.append(cardToAdd)

    def printHand(self):
        print('DEALER HAND')
        print ('--------')
        for each in self.dealerHand:
            print(each)
        print ('--------')
