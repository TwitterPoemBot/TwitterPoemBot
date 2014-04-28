from random import sample
from poem import Tweet, Poem, engine, db
from sqlalchemy.sql import text

def couplet(hashtag):
    ''' Generates a Couplet poem given a list of (text, syllable count, rhyme) tuples ''' 

    q = text('''SELECT * FROM tweet LEFT JOIN tweets ON tweet.id = tweets.tweet_id 
            WHERE tweets.tweet_id IS NULL AND tweet.hashtag = :h''')
    tweets = engine.connect().execute(q, h=hashtag).fetchall()
    corpus = [{'line':t.text, 'syllables':t.syllables, 'phone':t.phone, 'id':t.id, 'last_word':t.last_word} \
                for t in tweets]

    def get_lines(phone, word, syllables):
        # q = text('''SELECT * FROM tweet LEFT JOIN tweets ON tweet.id = tweets.tweet_id 
        #     WHERE tweets.tweet_id IS NULL AND tweet.hashtag = :h AND tweet.phone = :p''')
        # tweets = engine.connect().execute(q, h=hashtag, s=sylla_count).fetchall()
        # return tweets
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
            raise ValueError('Could not construct couplet - not enough tweets found')
    except ValueError as e:
        raise ValueError('Could not construct couplet - not enough tweets found') 
    first = first[0]
    second = second[0]
    
    # tweets = [Tweet(first['line'].decode('ascii', 'ignore'), first['url'].decode('ascii', 'ignore'), hashtag)]
    # tweets += [Tweet(second['line'].decode('ascii', 'ignore'), second['url'].decode('ascii', 'ignore'), hashtag)]
    tweets = [first, second]
    tweets = [db.session.query(Tweet).get(t['id']) for t in tweets]
    
    poem = Poem(tweets, hashtag, 'couplet')
    
    return poem
