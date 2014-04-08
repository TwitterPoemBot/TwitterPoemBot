from random import sample
import logging

def haiku(corpus):
    ''' Generates a Haiku poem given a dictionary of (text, syllable count, rhyme) ''' 

    def get_lines(sylla_count):
        ''' Returns all tweets in the corpus with the given number of syllables 
            replace with sql call?'''
        lines = [line for line in corpus if line['syllables'] == sylla_count] 
        linez = [line['line'] for line in corpus if line['syllables'] == sylla_count] 
        logging.info('Lines with ' + str(sylla_count) + ' syllables: ')
        logging.info(linez)
        return lines

    try:
        # Get random sample from 5 or 7 syllable tweets
        five_syllables = sample(get_lines(5), 2)
        seven_syllables = sample(get_lines(7), 1)
    except ValueError as e:
        raise Exception('Could not construct haiku - not enough tweets') 

    poem = [five_syllables[0]['line']]
    poem += [seven_syllables[0]['line']]
    poem += [five_syllables[1]['line']]
    poem += [five_syllables[0]['url']]
    poem += [seven_syllables[0]['url']]
    poem += [five_syllables[1]['url']]
    return '\n'.join(poem)