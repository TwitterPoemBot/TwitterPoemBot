import haiku
from parseLines import parse
import unittest

class TestHaiku(unittest.TestCase):

    def test_valid(self):
        corpus = [parse('5 syllable line(1)'), 
              parse('5 syllable line(2)'),
              parse('a seven syllable line'),
              parse('some filler')]
        poem = haiku.haiku(corpus)
        print poem
        poem = poem.split('\n')
        self.assertTrue((poem[0] == '5 syllable line(1)' and poem[2] == '5 syllable line(2)')
                     or (poem[2] == '5 syllable line(1)' and poem[0] == '5 syllable line(2)'))
        self.assertTrue(poem[1] == 'a seven syllable line')

    def test_invalid(self):
        ''' Tests insufficient amount of appropriate tweets '''
        corpus = [('a tweet', 2, 0), 
              ('just some stupid text', 5, 0),
              ('a frog jumps into the pond', 7, 0)]
        self.assertRaises(Exception, haiku.haiku, corpus)

if __name__ == '__main__':
    unittest.main()
