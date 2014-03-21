#test cases for rhyme checker
import unittest
from cStringIO import StringIO
import sys

sys.path.insert(0, '../') # temporary hack
from models.poems.parseLines import parse

class TestParseFunctions(unittest.TestCase):

    def test_parse(self):
        line1 = "hello i am dog"
        output = parse(line1)
        self.assertEqual(output, {'phone':'AO1G', 'line':'hello i am dog', 'syllables':5})
		
	def test_parse_nonalpha(self):
		line1 = "hello i am dog!"
        output = parse(line1)
        self.assertEqual(output, {'phone':'AO1G', 'line':'hello i am dog', 'syllables':5})
	
	def test_bad_input(self):
		line1 = "hello i am dg"
		output = parse(line1)
		self.assertEqual(output, {})

    def test_emoji(self):
        line = r'dog \xf0\x9f\x98\x9f'
        output = parse(line)
        self.assertEqual(output, {'phone': 'AO1G', 'line': line, 'syllables': 1})

if __name__ == '__main__':
    unittest.main()
