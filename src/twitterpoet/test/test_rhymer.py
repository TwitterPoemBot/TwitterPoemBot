#test cases for rhyme checker
import unittest
from cStringIO import StringIO
import sys

sys.path.insert(0, '../')
from models.poems.rhymer.rhyme_checker import rhymes, isInDict

class TestRhymerFunctions(unittest.TestCase):

    def test_rhyme(self):
        word1 = "call"
        word2 = "ball"
        output = rhymes(word1, word2)
        self.assertEqual(output, True)

    def test_no_rhyme(self):
        word1 = "call"
        word2 = "one"
        output = rhymes(word1, word2)
        self.assertEqual(output, False)

    def test_wrong_stress(self):
        word1 = "someone"
        word2 = "one"
        output = rhymes(word1, word2)
        self.assertEqual(output, False)

    def test_bad_input(self):
        word1 = "sq32e"
        word2 = "one"
        output = isInDict(word1)
        self.assertEqual(output, False)
        output = rhymes(word1, word2)
        self.assertEqual(output, False)

if __name__ == '__main__':
    unittest.main()
