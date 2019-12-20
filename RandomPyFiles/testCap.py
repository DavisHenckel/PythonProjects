import unittest
import cap

class TestCap(unittest.TestCase):
    def testOneWord(self):
        text = 'python'
        result = cap.myFunc(text)
        self.assertEqual(result,'Python')

    def testMultipleWords(self):
        text = 'monty python'
        result = cap.myFunc(text)
        self.assertEqual(result,'Monty Python')

if __name__ == "__main__":
    unittest.main()