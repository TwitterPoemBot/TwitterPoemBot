from twython import Twython, TwythonRateLimitError
import sys
from time import time

def connect():
    return Twython(app_key="7JpoIKJbcWppGabeAuyGA", app_secret="cVQGxy1fcxJJxJ3avyitZ4wNqAUEWNTIEgjNUDZnA",
                  oauth_token="2329651538-iZ2nEPBSIyl3u5AnU4ppfYEfJflTEeH6Krl8OO5", oauth_token_secret="V6ja2kfgl3aNr28QvOb9VmlbP8e9jxkora82wplPT43Vz")

def get_trending_topics(twitter):
    trends = twitter.get_place_trends(id=23424977)
    topics = []
    for trend in trends[0].get('trends',[]):
        topics.append(trend['name'])
    return topics

def get_tweets(twitter, topics):
    results = []
    for topic in topics:    
        results.append(twitter.search(q=topic, count=50))
    text_file = open("Output.txt", "w")
    for results2 in results:
        for tweet in results2['statuses']:
            text_file.write( tweet['text'].encode('utf-8')+ '\n' + '\n')
    text_file.close()

def get_tweets_from_file(s):
    tweets = []
    with open("Output.txt", "r") as f:
        lines = f.readlines()
    for line in lines:
        if s.lower() in line.lower():
            tweets.append(line)
    return tweets

def get_tweets_from_hashtag(twitter, hashtag):
    max_id = float("inf")
    tweets = []
    for n in range(1,21):
        results = []
        try:
            results.append(twitter.search(q=hashtag, count=100, max_id=max_id))
            for results2 in results:
                for tweet in results2['statuses']:
                    tweets.append(tweet['text'].encode('utf-8'))
                    tweets.append("twitter.com/TwttPoet/status/"+tweet['id_str'].encode('utf-8'))
                    max_id = tweet['id']
        except TwythonRateLimitError as e:
            seconds = str(float(twitter.get_lastfunction_header('x-rate-limit-reset'))-time()+5)
            raise Exception('you hit the rate limit! Try again in '+seconds+' seconds.')
    return tweets

def get_fewer_tweets_from_hashtag(twitter, hashtag):
    max_id = float("inf")
    tweets = []
    for n in range(1,3):
        results = []
        results.append(twitter.search(q=hashtag, count=100, max_id=max_id))
        for results2 in results:
            for tweet in results2['statuses']:
                tweets.append(tweet['text'].encode('utf-8'))
                tweets.append("twitter.com/TwttPoet/status/"+tweet['id_str'].encode('utf-8'))
                max_id = tweet['id']
    return tweets

def get_tweet_from_url(twitter, url):
    index = url.index("status/")
    num = url[7+index:]
    return twitter.show_status(id=num)['text'].encode('utf-8')
