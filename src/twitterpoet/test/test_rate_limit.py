import unittest
import sys
from twython import TwythonRateLimitError

sys.path.insert(0, '../')
from models.tweets.get_tweets2 import get_tweets_from_hashtag, connect, get_remaining_api_calls

class TestRateLimit(unittest.TestCase):
    def test_no_exception(self):
        ''' Tests that an exception isn't thrown when the rate limit hasn't been hit '''
        twitter = connect()
        try:
            get_tweets_from_hashtag(twitter, "#WeWereBornForThis")
            global remaining
            remaining = get_remaining_api_calls(twitter)
        
        except:
            self.fail("Exception was thrown where one wasn't expected.")

    def test_throws_exception(self):
        ''' Tests that an exception is thrown when the rate limit has been hit  '''
        twitter = connect()
        print remaining
        for i in range(0,remaining):
            get_tweets_from_hashtag(twitter, "#WeWereBornForThis")
        with self.assertRaises(Exception):
            get_tweets_from_hashtag(twitter, "#WeWereBornForThis")

    def test_exception_format(self):
        ''' Tests that the exception message has the correct format  '''
        twitter = connect()
        try:
            get_tweets_from_hashtag(twitter, "#WeWereBornForThis")
        except Exception as e:
            self.assertTrue("You hit the rate limit! Try again in " in str(e))
            self.assertTrue(" seconds." in str(e))

    def test_exception_less_than_15_minutes(self):
        ''' Tests that an exception says the remaining seconds and that it's less than 15 minutes  '''
        twitter = connect()
        try:
            get_tweets_from_hashtag(twitter, "#WeWereBornForThis")
        except Exception as e:
            s = str(e)
            global num
            num = float(s[s.index("in")+6:s.index("seconds")-1])
            self.assertTrue(num<15*60)

    def test_exception_decreases(self):
        ''' Tests that the exception message decreases  '''
        twitter = connect()
        try:
            get_tweets_from_hashtag(twitter, "#WeWereBornForThis")
        except Exception as e:
            s = str(e)
            self.assertTrue(float(s[s.index("in")+6:s.index("seconds")-1])<num)




if __name__ == '__main__':
    global remaining
    remaining = 0
    unittest.main()
