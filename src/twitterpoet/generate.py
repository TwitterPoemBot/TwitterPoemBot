from twython import Twython
from models.poems.haiku import haiku
from models.poems.couplet import couplet
from models.poems.limerick import limerick
from models.poems.parseLines import parse_all
from models.tweets.get_tweets2 import get_tweets_from_hashtag, connect, RateLimitException
import logging
from models.poems.poem import Tweet, db, engine
from sqlalchemy import create_engine
from sqlalchemy.sql import *

poem_types = {'haiku': haiku, 'couplet': couplet, 'limerick': limerick}

def load_more_tweets(hashtag, tries=10, count=100):
    ''' Loads a maximum of count * tries number of new recent tweets with the given hashtag into the database '''
    
    twitter = connect()
    tweets = get_tweets_from_hashtag(twitter, hashtag, tries=tries, count=count)
    parsed_tweets = parse_all(tweets, hashtag)
    inserter = Tweet.__table__.insert().prefix_with('IGNORE')
    engine.execute(inserter, parsed_tweets)
    db.session.commit()

def generatePoem(hashtag, type):
    ''' Takes in a hashtag and poem type and returns a poem as a string '''

    hashtag = hashtag.strip()
    if hashtag[0] == '#':
        hashtag = hashtag[1:]

    if type not in poem_types:
        raise Exception('Poem type ' + type + ' not recognized')       

    MAX_TRIES = 2
    for i in range(MAX_TRIES+1):
        try:
            print 'trying to make a poem'
            poem = poem_types[type](hashtag)
            return poem
        except ValueError as e:
            if i >= MAX_TRIES:
                raise e
            load_more_tweets(hashtag)
            
    raise Exception('Could not find enough tweets!')


