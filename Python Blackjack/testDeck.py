import unittest
import deck

'''Unit tests for Deck'''
class TestDeck(unittest.TestCase):

    #Ensures that a deck created has the right size
    def testDeckSize(self): 
        correctSize = 52
        testDeck = deck.Deck()
        self.assertEqual(len(testDeck.deck), correctSize)
    
    #Ensures that all 4 suits exist in the deck.
    def testDeckSuits(self):
        correctSuits = ("Hearts", "Diamonds", "Spades", "Clubs")
        testDeck = deck.Deck()
        #Prior to the Deck being shuffled, Hearts, Diamonds, Spades and Clubs are created sequentially
        self.assertEqual(testDeck.getCard(0).suit, correctSuits[0]) 
        self.assertEqual(testDeck.getCard(15).suit, correctSuits[1])
        self.assertEqual(testDeck.getCard(30).suit, correctSuits[2])
        self.assertEqual(testDeck.getCard(45).suit, correctSuits[3])

    #Ensure there are 13 of each suit in the deck
    def testProperDeck(self): 
        testDeck = deck.Deck()
        numEachSuit = 13
        numHearts = 0
        numDiamonds = 0
        numSpades = 0
        numClubs = 0
        for eachCard in testDeck:
            if testDeck.getCard(eachCard).suit == "Hearts":
                numHearts += 1
            elif testDeck.getCard(eachCard).suit == "Diamonds":
                numDiamonds += 1
            elif testDeck.getCard(eachCard).suit == "Spades":
                numSpades += 1
            elif testDeck.getCard(eachCard).suit == "Clubs":
                numClubs += 1
            else:
                print('Something is wrong. Specifically, a card does not have a valid suit')
        self.assertEqual(numHearts, numEachSuit)
        self.assertEqual(numDiamonds, numEachSuit)
        self.assertEqual(numSpades, numEachSuit)
        self.assertEqual(numClubs, numEachSuit)

    #Ensures there are at least 45 cards have different locations. We will accept 7 cards being in same location
    def testShuffle(self):
        testDeck = deck.Deck()
        deckShuffle = deck.Deck()
        deckShuffle.shuffleDeck()
        numSameCards = 0
        for eachCard in testDeck:
            card1 = testDeck.getCard(eachCard)
            card2 = deckShuffle.getCard(eachCard)
            if(card1.isCardEqual(card2)):
                numSameCards += 1
            else:
                continue
        
        self.assertLess(numSameCards, 7) 


if __name__ == "__main__":
    unittest.main()
    