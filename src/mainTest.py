import main, unittest, logging, sys

class TestGenerate(unittest.TestCase):

    def test_valid(self):
        self.assertTrue(poem[1] == 'a seven syllable line')

    def test_invalid_poem_type(self):
        self.assertRaises(Exception, generate, 'test')

if __name__ == '__main__':
    logging.basicConfig(stream=sys.stderr, level=logging.INFO)
    unittest.main()
