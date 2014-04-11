from poem import Poem
import unittest, logging, sys
class TestPoem(unittest.TestCase):
    def test_constructor(self):
        p = Poem("test")
        self.assertTrue(p.poemText == "test")

if __name__ == '__main__':
    logging.basicConfig(stream=sys.stderr, level=logging.INFO)
    unittest.main()
