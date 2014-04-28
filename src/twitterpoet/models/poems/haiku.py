from random import sample
from poem import Tweet, Poem, engine, db
from sqlalchemy.sql import text
import logging

def haiku(hashtag):
    ''' Generates a Haiku poem given a hashtag ''' 

    def get_lines(sylla_count):
        ''' Returns all tweets with the given number of syllables '''

        # tweets = Tweet.query.filter_by(hashtag=hashtag) \
        #                     .filter_by(syllables=sylla_count) \
        # #                     .filter_by(SELECT t1.ID
        # tweets = Tweet.query.from_statement('SELECT id FROM tweet LEFT JOIN tweets'
        #     ' ON tweet.id = tweets.tweet_id WHERE tweets.tweet_id IS NULL AND tweet.hashtag = ' + '"'+hashtag+'"'
        #     + ' AND tweet.syllables = ' + str(sylla_count)).all()
                # .filter_by(hashtag=hashtag) \
                # .filter_by(syllables=sylla_count).all()
        q = text('''SELECT * FROM tweet LEFT JOIN tweets ON tweet.id = tweets.tweet_id 
            WHERE tweets.tweet_id IS NULL AND tweet.hashtag = :h AND tweet.syllables = :s''')
        tweets = engine.connect().execute(q, h=hashtag, s=sylla_count).fetchall()
        print "Haiku: query", q, ": ", str(len(tweets))
        print "hashtag:", hashtag
        return tweets

    try:
        # Get random sample from 5 or 7 syllable tweets
        five_syllables = sample(get_lines(5), 2)
        seven_syllables = sample(get_lines(7), 1)
    except ValueError as e:
        print 'haiku - not enough tweets...'
        raise ValueError('Could not construct haiku - not enough tweets') 

    tweets = [five_syllables[0], seven_syllables[0], five_syllables[1]]
    print [t.id for t in tweets]
    tweets = [db.session.query(Tweet).get(t.id) for t in tweets]
    print tweets
    print '---'
    return Poem(tweets, hashtag, 'haiku')
