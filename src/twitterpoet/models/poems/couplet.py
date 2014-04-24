from random import sample
from poem import Tweet
from poem import Poem

def couplet(corpus, hashtag):
    ''' Generates a Couplet poem given a list of (text, syllable count, rhyme) tuples ''' 

    def get_lines(phone, word, syllables):
        return [line for line in corpus if line != {} and line['phone'] == phone and word.lower() != line['last_word'].lower() and abs(line['syllables'] - syllables)<=1]
    def get_lines2():
        return [line for line in corpus if line != {} and line['phone'] != None and len(get_lines(line['phone'], line['last_word'], line['syllables']))>0]  
    try:
        # Get random sample from 5 or 7 syllable tweets
        first = sample(get_lines2(), 1)
        phone = first[0]
        phone = phone['phone']
        second = first
        word = first[0]['last_word']
        syl = first[0]['syllables']
        if len(get_lines(phone, word, syl)) > 0:
            while word==second[0]['last_word']:
                second = sample(get_lines(phone, word, syl), 1)
        else:
            raise Exception('Could not construct couplet - not enough tweets found')
    except ValueError as e:
        raise Exception('Could not construct couplet - not enough tweets found') 
    first = first[0]
    second = second[0]
    
    tweets = [Tweet(first['line'].decode('ascii', 'ignore'), first['url'].decode('ascii', 'ignore'), hashtag)]
    tweets += [Tweet(second['line'].decode('ascii', 'ignore'), second['url'].decode('ascii', 'ignore'), hashtag)]
    
    poem = Poem(tweets, hashtag, 'couplet')
    
    return poem
