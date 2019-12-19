import unittest
import deck

class TestDeck(unittest.TestCase):

    def testDeckSize(self): #Ensures that a deck created has the right size
        correctSize = 52
        testDeck = deck.Deck()
        self.assertEqual(len(testDeck.deck), correctSize)
    
    def testDeckSuits(self): #Ensures that all 4 suits exist in the deck.
        correctSuits = ("Hearts", "Diamonds", "Spades", "Clubs")
        testDeck = deck.Deck()
        #Prior to the Deck being shuffled, Hearts, Diamonds, Spades and Clubs are created sequentially
        self.assertEqual(testDeck.getCard(0).suit, correctSuits[0]) 
        self.assertEqual(testDeck.getCard(15).suit, correctSuits[1])
        self.assertEqual(testDeck.getCard(30).suit, correctSuits[2])
        self.assertEqual(testDeck.getCard(45).suit, correctSuits[3])

if __name__ == "__main__":
    unittest.main()
    