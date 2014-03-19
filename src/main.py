from twython import Twython
from twitterpoet.models.poems.haiku import haiku
from twitterpoet.models.poems.parseLines import parse
from twitterpoet.models.tweets.get_tweets2 import get_tweets_from_hashtag


def generate(hashtag, type='haiku'):
    ''' Takes in a hashtag and poem type and returns a poem as a string '''
    tweets = get_tweets_from_hashtag(twitter, hashtag)

    # Debug Stuff #
    print len(tweets)
    for tweet in tweets:
        print tweet

    parsed_tweets = [parse(tweet) for tweet in tweets if parse(tweet) != {}]
    if type == 'haiku':
        return haiku(parsed_tweets)
    else:
        raise Exception('Poem type ' + type + ' not recognized')

if __name__ == '__main__':
    twitter = Twython(app_key="7JpoIKJbcWppGabeAuyGA", app_secret="cVQGxy1fcxJJxJ3avyitZ4wNqAUEWNTIEgjNUDZnA",
                  oauth_token="2329651538-iZ2nEPBSIyl3u5AnU4ppfYEfJflTEeH6Krl8OO5", oauth_token_secret="V6ja2kfgl3aNr28QvOb9VmlbP8e9jxkora82wplPT43Vz")

    # results = get_tweets_from_hashtag(twitter, 'basketball')
    # print results[0]
    # print results
    print generate('obama')    
    # twitter.update_status(status=poem)
