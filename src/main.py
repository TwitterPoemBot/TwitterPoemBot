from twython import Twython
from twitterpoet.models.poems.haiku import haiku
from twitterpoet.models.poems.limerick import limerick
from twitterpoet.models.poems.couplet import couplet
from twitterpoet.models.poems.parseLines import parse_all
from twitterpoet.models.tweets.get_tweets2 import get_tweets_from_hashtag
import logging

def generate(hashtag, type='haiku'):
    ''' Takes in a hashtag and poem type and returns a poem as a string '''
    if hashtag == '' or hashtag is None:
        raise Exception('Must have a hashtag')

    tweets = get_tweets_from_hashtag(twitter, hashtag)
    parsed_tweets = parse_all(tweets)
    if type == 'haiku':
        return haiku(parsed_tweets)
    if type == 'couplet':
        return couplet(parsed_tweets)
    if type == 'limerick':
        return limerick(parsed_tweets)
    else:
        raise Exception('Poem type ' + type + ' not recognized')

if __name__ == '__main__':
    import sys
    logging.basicConfig(stream=sys.stderr, level=logging.INFO)
    twitter = Twython(app_key="7JpoIKJbcWppGabeAuyGA", app_secret="cVQGxy1fcxJJxJ3avyitZ4wNqAUEWNTIEgjNUDZnA",
                  oauth_token="2329651538-iZ2nEPBSIyl3u5AnU4ppfYEfJflTEeH6Krl8OO5", oauth_token_secret="V6ja2kfgl3aNr28QvOb9VmlbP8e9jxkora82wplPT43Vz")

    # results = get_tweets_from_hashtag(twitter, 'basketball')
    # print results[0]
    # print results
    print generate('basketball', type='limerick')    
    # twitter.update_status(status=poem)
