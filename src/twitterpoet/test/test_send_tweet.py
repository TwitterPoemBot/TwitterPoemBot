import unittest
from mock import patch, Mock, MagicMock
from cStringIO import StringIO
import sys

sys.path.insert(0, '../')
from models.poems.poem import Poem
from models.poems.poem import Tweet
from models.tweets.get_tweets2 import sendPoem

class Test(unittest.TestCase):

    def setUp(self):
        self.twitter = MagicMock()

    def test_basic_send(self):
        ''' Tests a basic tweet is sent '''
        tweet1 = Tweet("text 1", "something.something", "corn")
        tweet2 = Tweet("text 2", "somethingelse.something", "corn")
        tweets = [tweet1, tweet2]
        poem = Poem(tweets, "corn", "couplet")
        sendPoem(self.twitter, poem)
        self.assertEqual(poem.hashtag, tweet1.hashtag)
        
    def test_newline_send(self):
        ''' Tests that newlines are appropriately handled '''
        tweet1 = Tweet("text 1\n", "something.something", "corn")
        tweet2 = Tweet("text 2\n", "somethingelse.something", "corn")
        tweets = [tweet1, tweet2]
        poem = Poem(tweets, "corn", "couplet")
        sendPoem(self.twitter, poem)
        self.assertEqual(poem.hashtag, tweet1.hashtag)
        
    def test_empty_send(self):
        ''' Tests that empty strings are properly handled '''
        tweet1 = Tweet("", "something.something", "corn")
        tweet2 = Tweet("", "somethingelse.something", "corn")
        tweets = [tweet1, tweet2]
        poem = Poem(tweets, "corn", "couplet")
        sendPoem(self.twitter, poem)
        self.assertEqual(poem.hashtag, tweet1.hashtag)
        
    def test_same_send(self):
        ''' Tests that identical tweets are properly handled '''
        tweet1 = Tweet("text 1", "something.something", "corn")
        tweet2 = Tweet("text 1", "something.something", "corn")
        tweets = [tweet1, tweet2]
        poem = Poem(tweets, "corn", "couplet")
        sendPoem(self.twitter, poem)
        self.assertEqual(poem.hashtag, tweet1.hashtag)
        
    def test_zero_send(self):
        ''' Tests on an empty list of tweets '''
        tweets = []
        poem = Poem(tweets, "corn", "couplet")
        sendPoem(self.twitter, poem)
