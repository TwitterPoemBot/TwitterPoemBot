import limerick
from parseLines import parse
import unittest, logging, sys

class TestHaiku(unittest.TestCase):

    def test_valid(self):
        corpus = [parse('The limerick packs laughs anatomical'), 
              parse('Into space that is quite economical'),
              parse("But the good ones I've seen"),
              parse("So seldom are clean"),
              parse('And the clean ones so seldom are comical')]
        poem = limerick.limerick(corpus)
        print poem
        poem = poem.split('\n')
        self.assertTrue(poem[0] == "The limerick packs laughs anatomical")
        self.assertTrue(poem[1] == "Into space that is quite economical")
        self.assertTrue(poem[2] == "But the good ones I've seen")
        self.assertTrue(poem[3] == "So seldom are clean")
        self.assertTrue(poem[4] == "And the clean ones so seldom are comical")

    # def test_invalid(self):
    #     ''' Tests insufficient amount of appropriate tweets '''
    #     corpus = [('a tweet', 2, 0), 
    #           ('just some stupid text', 5, 0),
    #           ('a frog jumps into the pond', 7, 0)]
    #     self.assertRaises(Exception, haiku.haiku, corpus)

    # def test_valid1(self):
    #     corpus = [parse('5 syllable line'), 
    #           parse('5 syllable lines'),
    #           parse('a seven syllable line!'),
    #           parse('some filler words')]
    #     poem = haiku.haiku(corpus)
    #     poem = poem.split('\n')
    #     self.assertTrue((poem[0] == '5 syllable line' and poem[2] == '5 syllable lines')
    #                  or (poem[2] == '5 syllable line' and poem[0] == '5 syllable lines'))
    #     self.assertTrue(poem[1] == 'a seven syllable line!')

if __name__ == '__main__':
    logging.basicConfig(stream=sys.stderr, level=logging.INFO)
    unittest.main()
