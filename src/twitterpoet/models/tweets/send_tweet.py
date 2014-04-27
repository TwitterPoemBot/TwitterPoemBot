from twython import Twython, TwythonRateLimitError
import sys
from time import time

def connect():
    return Twython(app_key="7JpoIKJbcWppGabeAuyGA", app_secret="cVQGxy1fcxJJxJ3avyitZ4wNqAUEWNTIEgjNUDZnA",
                  oauth_token="2329651538-iZ2nEPBSIyl3u5AnU4ppfYEfJflTEeH6Krl8OO5", oauth_token_secret="V6ja2kfgl3aNr28QvOb9VmlbP8e9jxkora82wplPT43Vz")
                  
def sendPoem(twitter, poem):
    text = poem.hashtag
    text += "\n"
    for tweet in poem.tweets:
        text += tweet.url + "\n"
    twitter.update_status(status=text)
