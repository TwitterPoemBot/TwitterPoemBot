import unittest
import sys

sys.path.insert(0, '../')
from models.poems import couplet
from models.poems.parseLines import parse

class TestCouplet(unittest.TestCase):

    def test_one_more_syllable(self):
        ''' Tests that a couplet can be made if the lines are one syllable difference  '''

        corpus = [parse('Boy I like the bay'), 
              parse('We will go there today!'),
              parse('some filler')]
        poem = couplet.couplet(corpus)
        print poem
        poem = poem.split('\n')
        self.assertTrue((poem[0] == 'Boy I like the bay' and poem[1] == 'We will go there today!')
                     or (poem[1] == 'Boy I like the bay' and poem[0] == 'We will go there today!'))

    def test_same_syllables(self):
        ''' Tests that a couplet can be made with two lines w/ same # syllables  '''

        corpus = [parse('Well gosh, I hate the bay'), 
              parse('You must go there today!'),
              parse('some filler')]
        poem = couplet.couplet(corpus)
        print poem
        poem = poem.split('\n')
        self.assertTrue((poem[0] == 'Well gosh, I hate the bay' and poem[1] == 'You must go there today!')
                     or (poem[1] == 'Well gosh, I hate the bay' and poem[0] == 'You must go there today!'))

    def test_syllable_discrep(self):
        ''' Tests that a couplet cannot be made if there is a difference of more than one syllable  '''

        corpus = [parse('I miss the bay'), 
              parse('You may or may not go there today!'),
              parse('some filler')]
        self.assertRaises(Exception, couplet.couplet, corpus)


    def test_invalid(self):
        ''' Tests insufficient amount of appropriate tweets '''
        corpus = [parse('a tweet'),
              parse('just some stupid text'),
              parse('a frog jumps into the pond')]
        self.assertRaises(Exception, couplet.couplet, corpus)

    def test_same_word(self):
        ''' Tests that couplet can't be made with lines ending in same word '''
        corpus = [parse('Say, I want a poem!'),
        parse('A really lazy POEM!')]
        self.assertRaises(Exception, couplet.couplet, corpus)

if __name__ == '__main__':
    unittest.main()
