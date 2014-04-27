from random import sample
from poem import Tweet
from poem import Poem
import logging

def haiku(corpus, hashtag):
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

    tweets = [Tweet(five_syllables[0]['line'].decode('ascii', 'ignore'), five_syllables[0]['url'].decode('ascii', 'ignore'), hashtag)]
    tweets += [Tweet(seven_syllables[0]['line'].decode('ascii', 'ignore'), seven_syllables[0]['url'].decode('ascii', 'ignore'), hashtag)]
    tweets += [Tweet(five_syllables[1]['line'].decode('ascii', 'ignore'), five_syllables[1]['url'].decode('ascii', 'ignore'), hashtag)]
    
    poem = Poem(tweets, hashtag, 'haiku')

    return poem
