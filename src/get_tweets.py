from twython import Twython
import MySQLdb
import re
import json

if __name__ == '__main__':
    twitter = Twython(app_key="7JpoIKJbcWppGabeAuyGA", app_secret="cVQGxy1fcxJJxJ3avyitZ4wNqAUEWNTIEgjNUDZnA",
                  oauth_token="2329651538-iZ2nEPBSIyl3u5AnU4ppfYEfJflTEeH6Krl8OO5",
                  oauth_token_secret="V6ja2kfgl3aNr28QvOb9VmlbP8e9jxkora82wplPT43Vz")


    con = MySQLdb.connect(host='ampolgroup.com', user='tpg', passwd='uiucCS428', db='twitterpoem',
                          use_unicode=True, charset='utf8')


    trends = twitter.get_place_trends(id=23424977)
    results = []
    for trend in trends[0].get('trends',[]):
        topic = trend['name']
        results.append(twitter.search(q=topic, count=50))
    text_file = open("Output.txt", "w")
    for results2 in results:
        for tweet in results2['statuses']:
            hashtag = ""
            for tag in tweet['entities']['hashtags']:
                if hashtag == "":
                    hashtag += tag['text']
                else:
                    hashtag += "," + str(tag['text'])

            x = con.cursor()

            tweetStr = tweet['text'].encode('ascii', 'ignore')

            tweetStr = re.sub(r'\w+:\/{2}[\d\w-]+(\.[\d\w-]+)*(?:(?:\/[^\s/]*))*', '', tweetStr)


            sql = "INSERT INTO twitterpoem.tweets (content, hashtag) VALUES ('" + MySQLdb.escape_string(tweetStr) +\
                  "', '" + MySQLdb.escape_string(hashtag) + "')"

            x.execute(sql)
            con.commit()
            text_file.write( tweet['text'].encode('utf-8')+ '\n' + '\n')
    text_file.close()

    
