import unittest
import sys

sys.path.insert(0, '../')
from models.poems import couplet
from models.tweets.get_tweets2 import connect, get_fewer_tweets_from_hashtag, get_tweet_from_url
from models.poems.parseLines import parse_all, parse
from generate import generatePoem


class TestUrls(unittest.TestCase):

    def test_url_returns_correct_tweet(self):
	''' Tests that tweet matches url '''
	self.assertEqual(get_tweet_from_url(connect(), "https://twitter.com/mrssmallwood/status/454661604014305280"), "Today is #NationalSiblingsDay @andrew_pozzi @beckypozzi @jamespozzi @chrispozzi @RichPozzi aren't we lucky ;)")

    def test_hashtag_urls(self):
	''' Tests that tweet gotten from hashtag search matches url '''
	tweets = get_fewer_tweets_from_hashtag(connect(), "#BatonRougeSlang")
	self.assertEqual(get_tweet_from_url(connect(), tweets[1]), tweets[0])

    def test_parse_tweet_from_url(self):
	''' Tests that tweet from hashtag can be parsed to correct text '''
	tweets = get_fewer_tweets_from_hashtag(connect(), "#musicthatdontmatch")
	parsed_tweets = parse_all(tweets)
	tweet = parsed_tweets[0]
	text = get_tweet_from_url(connect(), tweet['url'])
	self.assertEqual(parse(text)['line'], tweet['line'])

    def test_couplet_urls(self):
	''' Tests that couplet returns poem and corresponding url '''
	couplet = generatePoem("#NationalPetDay", 'couplet')
	lines = couplet.split('\n')
	text0 = get_tweet_from_url(connect(), lines[2])
	text1 = get_tweet_from_url(connect(), lines[3])
	self.assertEqual(parse(text0)['line'], lines[0])
	self.assertEqual(parse(text1)['line'], lines[1])

    def test_haiku_urls(self):
	''' Tests that haiku returns poem and corresponding url '''
	haiku = generatePoem("#NationalPetDay", 'haiku')
	lines = haiku.split('\n')
	text0 = get_tweet_from_url(connect(), lines[3])
	text1 = get_tweet_from_url(connect(), lines[4])
	text2 = get_tweet_from_url(connect(), lines[5])
	self.assertEqual(parse(text0)['line'], lines[0])
	self.assertEqual(parse(text1)['line'], lines[1])
	self.assertEqual(parse(text2)['line'], lines[2])



if __name__ == '__main__':
    unittest.main()