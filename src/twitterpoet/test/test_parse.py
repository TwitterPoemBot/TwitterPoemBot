#test cases for rhyme checker
import unittest
from cStringIO import StringIO
import sys, logging

sys.path.insert(0, '../')
from models.poems.parseLines import parse, parse_all, is_english

class TestParseFunctions(unittest.TestCase):

    def test_parse(self):
        ''' Test basic text is parsed correctly '''
        line1 = "hello i am dog"
        output = parse(line1)
        self.assertEqual(output['line'], 'hello i am dog')
        self.assertEqual(output['last_word'], 'dog')
        self.assertEqual(output['phone'], 'AO1G')
        self.assertEqual(output['syllables'], 5)
		
	def test_parse_nonalpha(self):
        ''' Tests that non-alphanumeric characters are ignored '''
		line1 = "hello i am dog!"
        output = parse(line1)
        self.assertEqual(output['line'], 'hello i am dog')
        self.assertEqual(output['last_word'], 'dog')
        self.assertEqual(output['phone'], 'AO1G')
        self.assertEqual(output['syllables'], 5)

	def test_bad_input(self):
        ''' Tests that nonenglish words are ignored '''
		line1 = "hello i am dg"
		output = parse(line1)
		self.assertEqual(output, {})

    def test_emoji(self):
        ''' Tests that emoji are ignored '''
        line = r'dog \xf0\x9f\x98\x9f'
        output = parse(line)
        print output
        self.assertEqual(output, {'phone': 'AO1G', 'line': 'dog', 'syllables': 1, 'url':'', 'last_word':'dog'})

    def test_parse_all(self):
        ''' Tests that multiple lines are properly handled '''
        lines = ['dog', 'url1']
        output = parse_all(lines)
        print output
        self.assertEqual(output, [{'line':'dog', 'phone': 'AO1G', 'syllables':1, 'url':'url1', 'last_word':'dog'}])

    def test_is_english_false(self):
        ''' Tests that a non-english line is handled '''
        line = '\xe6\x88\x90\xe5\x8a\x9f hi'
        self.assertFalse(is_english(line))

    def test_is_english_true(self):
        ''' Tests the is_english function '''
        line = 'hello \xf0'
        self.assertTrue(is_english(line))

if __name__ == '__main__':
    logging.basicConfig(stream=sys.stderr, level=logging.INFO)
    unittest.main()
