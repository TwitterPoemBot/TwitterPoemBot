from twython import Twython
from twitterpoet.models.poems.haiku import haiku
from twitterpoet.models.poems.limerick import limerick
from twitterpoet.models.poems.couplet import couplet
from twitterpoet.models.poems.parseLines import parse_all
from twitterpoet.models.tweets.get_tweets2 import get_tweets_from_hashtag
from twitterpoet.generate import generatePoem
import logging

if __name__ == '__main__':
    import sys
    logging.basicConfig(stream=sys.stderr, level=logging.INFO, filename='latest.log', filemode='w')
    twitter = Twython(app_key="7JpoIKJbcWppGabeAuyGA", app_secret="cVQGxy1fcxJJxJ3avyitZ4wNqAUEWNTIEgjNUDZnA",
                  oauth_token="2329651538-iZ2nEPBSIyl3u5AnU4ppfYEfJflTEeH6Krl8OO5", oauth_token_secret="V6ja2kfgl3aNr28QvOb9VmlbP8e9jxkora82wplPT43Vz")

    # results = get_tweets_from_hashtag(twitter, 'basketball')
    # print results[0]
    # print results
    poem = generatePoem('gameofthrones', type='limerick')    
    print '-----'
    print poem
    if raw_input('Publish to twitter? Y/N').lower() == 'y':
        twitter.update_status(status=poem)
