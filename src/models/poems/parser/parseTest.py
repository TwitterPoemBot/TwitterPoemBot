#test cases for rhyme checker
import unittest
from parseLines import parse
from cStringIO import StringIO

class TestParseFunctions(unittest.TestCase):

    def test_parse(self):
        line1 = "hello i am dog"
        output = parse(line1)
        self.assertEqual(output, {'phone':'AO1G', 'line':'hello i am dog', 'syllables':6})
		
	def test_parse_nonalpha(self):
		line1 = "hello i am dog!"
        output = parse(line1)
        self.assertEqual(output, {'phone':'AO1G', 'line':'hello i am dog', 'syllables':6})
	
	def test_bad_input(self):
		line1 = "hello i am dg"
		output = parse(line1)
		self.assertEqual(output, {})


if __name__ == '__main__':
    unittest.main()
