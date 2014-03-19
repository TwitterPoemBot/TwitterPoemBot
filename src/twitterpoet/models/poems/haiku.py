from random import sample

def haiku(corpus):
    ''' Generates a Haiku poem given a list of (text, syllable count, rhyme) tuples ''' 

    def get_lines(sylla_count):
        ''' Returns all tweets in the corpus with the given number of syllables 
            replace with sql call?'''
        return [line['line'] for line in corpus if line != {} and line['syllables'] == sylla_count] 

    try:
        # Get random sample from 5 or 7 syllable tweets
        five_syllables = sample(get_lines(5), 2)
        seven_syllables = sample(get_lines(7), 1)
    except ValueError as e:
        raise Exception('Could not construct haiku - not enough tweets found') 

    poem = [five_syllables[0]]
    poem += [seven_syllables[0]]
    poem += [five_syllables[1]]
    return '\n'.join(poem)