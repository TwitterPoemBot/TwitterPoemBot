import get_tweets2 as getter
import unittest

class TestTweetFunctions(unittest.TestCase): 

    def test_tweets_in_file(self):
	twitter = getter.connect()
	topics = getter.get_trending_topics(twitter)
	self.assertEqual(len(topics), 10)
	getter.get_tweets(twitter, topics)
	tweets = getter.get_tweets_from_file("#RIPSpeakerKnockerz")
	print len(tweets)
	self.assertTrue(len(tweets)>35)

    def test_tweets(self):
	twitter = getter.connect()
	topics = getter.get_tweets_from_hashtag(twitter, "#Community")
    	self.assertTrue(len(topics)>2000)
    	self.assertTrue(len(set(topics))>1000)

    def test_trending(self):
	twitter = getter.connect()
	hashs = getter.get_trending_topics(twitter)
	self.assertTrue(len(hash)==10)

if __name__ == '__main__':
	unittest.main()
