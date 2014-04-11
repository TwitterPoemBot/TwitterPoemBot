import unittest, logging, sys
sys.path.insert(0, '../')
from models.poems.limerick import limerick
from models.poems.parseLines import parse, parse_all

class TestLimerick(unittest.TestCase):

    def test_valid(self):
        corpus = [parse('The limerick packs laughs anatomical'), 
              parse('Into space that is quite economical'),
              parse("But the good ones I've seen"),
              parse("So seldom are clean"),
              parse('And the clean ones so seldom are comical')]
        poem = limerick(corpus)
        print poem
        poem = poem.split('\n')
        self.assertTrue(poem[0] == "The limerick packs laughs anatomical")
        self.assertTrue(poem[1] == "Into space that is quite economical")
        self.assertTrue(poem[2] == "But the good ones I've seen")
        self.assertTrue(poem[3] == "So seldom are clean")
        self.assertTrue(poem[4] == "And the clean ones so seldom are comical")

    def test_invalid(self):
        ''' Tests insufficient amount of appropriate tweets '''
        corpus = [parse('a lone tweet')]
        self.assertRaises(Exception, limerick, corpus)

    def test_invalid_duplicates(self):
        ''' no duplicates '''
        corpus = [parse('The limerick packs laughs anatomical'), 
              parse('Into space that is quite anatomical'),
              parse("But the good ones I've seen"),
              parse("So seldom are clean"),
              parse('And the clean ones so seldom are comical')]
        self.assertRaises(Exception, limerick, corpus)

    def test_invalid_nonenglish(self):
        ''' no non-english lines '''
        corpus = [parse('The limerick \xe3\x81\x93\xe3\x82\x93\xe2\x80'), 
              parse('Into space that is quite anatomical'),
              parse("But the good ones I've seen"),
              parse("So seldom are clean"),
              parse('And the clean ones so seldom are comical')]
        self.assertRaises(Exception, limerick, corpus)

    def test_valid_variance(self):
        ''' Limerick should choose lines that have similar syllable counts '''
        corpus = [parse('The limerick packs laughs anatomical'), 
              parse('Into space that is quite economical'),
              parse("But the good ones I've seen"),
              parse("So seldom are clean"),
              parse('And the clean ones so seldom are comical'),
              parse('One two three four'),
              parse('one two three four five six')]
        poem = limerick(corpus)
        poem = poem.split('\n')
        self.assertTrue(poem[0] == "The limerick packs laughs anatomical")
        self.assertTrue(poem[1] == "Into space that is quite economical")
        self.assertTrue(poem[2] == "But the good ones I've seen")
        self.assertTrue(poem[3] == "So seldom are clean")
        self.assertTrue(poem[4] == "And the clean ones so seldom are comical")

    def test_urls(self):
        corpus = parse_all(['The limerick packs laughs anatomical', 'url1',
            'Into space that is quite economical', 'url2',
            "But the good ones I've seen", 'url3',
            'So seldom are clean', 'url4',
            'And the clean ones so seldom are comical', 'url5'])
        poem = limerick(corpus).split('\n')
        self.assertTrue(poem[5] == 'url1')
        self.assertTrue(poem[6] == 'url2')
        self.assertTrue(poem[7] == 'url3')
        self.assertTrue(poem[8] == 'url4')
        self.assertTrue(poem[9] == 'url5')


    

if __name__ == '__main__':
    logging.basicConfig(stream=sys.stderr, level=logging.INFO)
    unittest.main()
