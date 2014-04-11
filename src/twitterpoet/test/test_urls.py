import unittest
import sys

sys.path.insert(0, '../')
from models.poems import couplet
from models.poems.parseLines import parse
from models.tweets.get_tweets2 import connect, get_tweets_from_hashtag, get_tweet_from_url


class TestUrls(unittest.TestCase):

    def test(self):
	twitter = connect()
	self.assertEqual(get_tweet_from_url(twitter, "https://twitter.com/mrssmallwood/status/454661604014305280"), "Today is #NationalSiblingsDay @andrew_pozzi @beckypozzi @jamespozzi @chrispozzi @RichPozzi aren't we lucky ;)")

if __name__ == '__main__':
    unittest.main()