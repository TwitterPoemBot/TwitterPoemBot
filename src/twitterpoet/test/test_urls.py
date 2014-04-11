import unittest
import sys

sys.path.insert(0, '../')
from models.poems import couplet
from models.tweets.get_tweets2 import connect, get_fewer_tweets_from_hashtag, get_tweet_from_url
from models.poems.parseLines import parse_all, parse



class TestUrls(unittest.TestCase):

    def test(self):
	self.assertEqual(get_tweet_from_url(connect(), "https://twitter.com/mrssmallwood/status/454661604014305280"), "Today is #NationalSiblingsDay @andrew_pozzi @beckypozzi @jamespozzi @chrispozzi @RichPozzi aren't we lucky ;)")

    def test2(self):
	tweets = get_fewer_tweets_from_hashtag(connect(), "#BatonRougeSlang")
	self.assertEqual(get_tweet_from_url(connect(), tweets[1]), tweets[0])

    def test3(self):
	tweets = get_fewer_tweets_from_hashtag(connect(), "#musicthatdontmatch")
	parsed_tweets = parse_all(tweets)
	tweet = parsed_tweets[0]
	text = get_tweet_from_url(connect(), tweet['url'])
	self.assertEqual(parse(text)['line'], tweet['line'])	

if __name__ == '__main__':
    unittest.main()