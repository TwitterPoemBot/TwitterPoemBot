from twython import Twython


if __name__ == '__main__':

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
        print "Output.txt has 500 new tweets!"
    def get_tweets_from_file(s):
	tweets = []
	with open("Output.txt", "r") as f:
	    lines = f.readlines()
	for line in lines:
	    if s.lower() in line.lower():
		tweets.append(line)
	return tweets
	    
    twitter = connect()
    topics = get_trending_topics(twitter)
    get_tweets(twitter, topics)
