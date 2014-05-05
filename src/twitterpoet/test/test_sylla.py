import unittest
import sys

sys.path.insert(0, '../')
from models.poems.syllables import sylla

class TestSequenceFunctions(unittest.TestCase):
	def test_words(self):
		''' Tests that the words in the text file have syllables in the dictionary '''
		tc = open('syllable/cases.txt')
		for line in tc:
			# format is: word syllables
			ls = line.split()
			word = ls[0]
			syllables = int(ls[1])
			print "word, syllables: ", word, syllables
			self.assertEqual(sylla.syllables(word), syllables)

	def test_nonwords(self):
		''' Test non-english words '''
		self.assertEqual(sylla.syllables('lol'), 1)
		self.assertEqual(sylla.syllables('haha'), 2)
		self.assertEqual(sylla.syllables('wtf'), 1)

	def test_names(self):
		''' Test names (using the heuristic) '''
		self.assertEqual(sylla.syllables('yuki'), 2)
		self.assertEqual(sylla.syllables('paul'), 1)

if __name__ == '__main__':
	unittest.main()
	
