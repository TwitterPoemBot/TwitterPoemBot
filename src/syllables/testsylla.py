import sylla
import unittest

class TestSequenceFunctions(unittest.TestCase):
	def test_words(self):
		tc = open('cases.txt')
		for line in tc:
			# format is: word syllables
			ls = line.split()
			word = ls[0]
			syllables = int(ls[1])
			print "word, syllables: ", word, syllables
			self.assertEqual(sylla.syllables(word), syllables)

	def test_nonwords(self):
		self.assertEqual(sylla.syllables('lol'), 1)
		self.assertEqual(sylla.syllables('haha'), 2)
		self.assertEqual(sylla.syllables('wtf'), 1)

	def test_names(self):
		self.assertEqual(sylla.syllables('yuki'), 2)
		self.assertEqual(sylla.syllables('paul'), 1)

if __name__ == '__main__':
	unittest.main()
