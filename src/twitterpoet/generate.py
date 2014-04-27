from twython import Twython
from models.poems.haiku import haiku
from models.poems.couplet import couplet
from models.poems.limerick import limerick
from models.poems.parseLines import parse_all
from models.tweets.get_tweets2 import get_tweets_from_hashtag, connect
import logging

def generatePoem(hashtag, type):
    ''' Takes in a hashtag and poem type and returns a poem as a string '''
    twitter = connect()

    tweets = get_tweets_from_hashtag(twitter, hashtag)
    parsed_tweets = parse_all(tweets)
    logging.info(len(tweets) + " retrieved.")
    if type == 'haiku':
        return haiku(parsed_tweets, hashtag)
    elif type == 'couplet':
        return couplet(parsed_tweets, hashtag)
    elif type == 'limerick':
        return limerick(parsed_tweets, hashtag)
    else:
        raise Exception('Poem type ' + type + ' not recognized')