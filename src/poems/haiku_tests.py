import haiku
import unittest

class TestHaiku(unittest.TestCase):

    def test_valid(self):
        corpus = [('An old silent pond', 5, 7), 
              ('just some stupid text', 5, 8),
              ('a frog jumps into the pond', 7, '?')]
        poem = haiku.haiku(corpus)
        print poem

    def test_invalid(self):
        return

if __name__ == '__main__':
    unittest.main()
