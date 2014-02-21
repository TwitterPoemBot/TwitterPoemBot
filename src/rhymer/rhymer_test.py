import unittest
from rhyme_checker import Rhymer
from cStringIO import StringIO

class TestRhymerFunctions(unittest.TestCase):

    def setUp(self):
        self.rhymer = Rhymer()

    def test_rhyme(self):
        word1 = "call"
        word2 = "ball"
        output = self.rhymer.rhymes(word1, word2)
        self.assertEqual(output, True)

    def test_no_rhyme(self):
        word1 = "call"
        word2 = "one"
        output = self.rhymer.rhymes(word1, word2)
        self.assertEqual(output, False)

    def test_wrong_stress(self):
        word1 = "someone"
        word2 = "one"
        output = self.rhymer.rhymes(word1, word2)
        self.assertEqual(output, False)

    def test_bad_input(self):
        word1 = "sq32e"
        word2 = "one"
        output = self.rhymer.isInDict(word1)
        self.assertEqual(output, False)
        output = self.rhymer.rhymes(word1, word2)
        self.assertEqual(output, False)

if __name__ == '__main__':
    unittest.main()
