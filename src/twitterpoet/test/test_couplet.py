import unittest
import sys

sys.path.insert(0, '../')
from models.poems import couplet
from models.poems.parseLines import parse

class TestHaiku(unittest.TestCase):

    def test_valid(self):
        corpus = [parse('I like the bay'), 
              parse('We will go there today!'),
              parse('some filler')]
        poem = couplet.couplet(corpus)
        print poem
        poem = poem.split('\n')
        self.assertTrue((poem[0] == 'I like the bay' and poem[1] == 'We will go there today!')
                     or (poem[1] == 'I like the bay' and poem[0] == 'We will go there today!'))

    def test_invalid(self):
        ''' Tests insufficient amount of appropriate tweets '''
        corpus = [('a tweet', 2, 0), 
              ('just some stupid text', 5, 0),
              ('a frog jumps into the pond', 7, 0)]
        self.assertRaises(Exception, couplet.couplet, corpus)

if __name__ == '__main__':
    unittest.main()
