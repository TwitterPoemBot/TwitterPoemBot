import haiku, unittest, logging, sys

class TestHaiku(unittest.TestCase):

    def test_valid(self):
        corpus = [{'line': '5 syllable line(1)', 'syllables':5}, 
              {'line':'5 syllable line(2)', 'syllables':5},
              {'line':'a seven syllable line', 'syllables':7},
              {'line':'some filler', 'syllables':3}]
        poem = haiku.haiku(corpus)
        print poem
        poem = poem.split('\n')
        self.assertTrue((poem[0] == '5 syllable line(1)' and poem[2] == '5 syllable line(2)')
                     or (poem[2] == '5 syllable line(1)' and poem[0] == '5 syllable line(2)'))
        self.assertTrue(poem[1] == 'a seven syllable line')

    def test_invalid(self):
        ''' Tests insufficient amount of appropriate tweets '''
        corpus = [{'line':'a tweet', 'syllables':2}, 
              {'line':'just some stupid text', 'syllables':5},
              {'line':'a frog jumps into the pond', 'syllables':7}]
        self.assertRaises(Exception, haiku.haiku, corpus)

if __name__ == '__main__':
    logging.basicConfig(stream=sys.stderr, level=logging.INFO)
    unittest.main()
