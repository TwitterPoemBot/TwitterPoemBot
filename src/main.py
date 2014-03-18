__author__ = 'Mike'
from twython import Twython
from twitterpoet.models.poems.haiku import haiku
from twitterpoet.models.poems.parseLines import parse
from twitterpoet.models.tweets.get_tweets2 import get_tweets_from_hashtag


if __name__ == '__main__':
    twitter = Twython(app_key="7JpoIKJbcWppGabeAuyGA", app_secret="cVQGxy1fcxJJxJ3avyitZ4wNqAUEWNTIEgjNUDZnA",
                  oauth_token="2329651538-iZ2nEPBSIyl3u5AnU4ppfYEfJflTEeH6Krl8OO5", oauth_token_secret="V6ja2kfgl3aNr28QvOb9VmlbP8e9jxkora82wplPT43Vz")

    results = get_tweets_from_hashtag(twitter, 'basketball')
    print results[0]

    line1 = "five syllable line"
    line2 = "a seven syllable line"
    line3 = "five syllable line"
    poem = haiku([parse(line1), parse(line2), parse(line3)])
    print poem
    #twitter.update_status(status=poem)
