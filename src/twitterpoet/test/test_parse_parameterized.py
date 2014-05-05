import unittest
from cStringIO import StringIO
import sys, logging

sys.path.insert(0, '../') 
from models.poems.parseLines import parse, parse_all, is_english

class TestParseFunctions(unittest.TestCase):
    def test_invalid(self):
        ''' Tests that invalid lines are properly ignored '''
        while True:
            line = raw_input(r"Enter invalid line (or 'quit' to quit): ")
            if line == 'quit':
                return
            self.assertEqual(parse(line), {})

    def test_valid(self):
        ''' Tests that valid lines are not ignored '''
        while True:
            line = raw_input(r"Enter valid line (or 'quit' to quit): ")
            if line == 'quit':
                return
            self.assertNotEqual(parse(line), {})

if __name__ == '__main__':
    logging.basicConfig(stream=sys.stderr, level=logging.INFO)
    unittest.main()
