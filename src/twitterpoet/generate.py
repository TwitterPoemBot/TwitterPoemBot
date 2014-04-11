from twython import Twython
from models.poems.haiku import haiku
from models.poems.couplet import couplet
from models.poems.limerick import limerick
from models.poems.parseLines import parse_all
from models.tweets.get_tweets2 import get_tweets_from_hashtag
import logging

def generatePoem(hashtag, type):
    ''' Takes in a hashtag and poem type and returns a poem as a string '''
    twitter = Twython(app_key="7JpoIKJbcWppGabeAuyGA", app_secret="cVQGxy1fcxJJxJ3avyitZ4wNqAUEWNTIEgjNUDZnA",oauth_token="2329651538-iZ2nEPBSIyl3u5AnU4ppfYEfJflTEeH6Krl8OO5", oauth_token_secret="V6ja2kfgl3aNr28QvOb9VmlbP8e9jxkora82wplPT43Vz")

    tweets = get_tweets_from_hashtag(twitter, hashtag)
    parsed_tweets = parse_all(tweets)

    if type == 'haiku':
        return haiku(parsed_tweets)
    elif type == 'couplet':
        return couplet(parsed_tweets)
    elif type == 'limerick':
        return limerick(parsed_tweets)
    else:
        raise Exception('Poem type ' + type + ' not recognized')
