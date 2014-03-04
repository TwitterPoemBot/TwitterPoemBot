# from rhyme_checker import Rhymer
# from .syllab import sylla
from random import sample

def haiku(corpus):
    ''' Generates a Haiku poem given a list of (text, syllable count, rhyme) tuples ''' 
    def get_lines(sylla_count):
        return [line[0] for line in corpus if line[1] == sylla_count] 
    # Get corpus, in (line of text, syllable count, rhyme) format
    poem = []

    # Get two 5-syllable lines 
    five_syllables = sample(get_lines(5), 2)
    poem += [five_syllables[0]]

    # Get one 7-syllable line
    seven_syllables = sample(get_lines(7), 1)
    poem += [seven_syllables[0]]

    poem += [five_syllables[1]]
    return '\n'.join(poem)

