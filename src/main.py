__author__ = 'Mike'
from twython import Twython
from models.poems.haiku import haiku
from models.poems.parser.parseLines import parse 


if __name__ == '__main__':
    twitter = Twython(app_key="7JpoIKJbcWppGabeAuyGA", app_secret="cVQGxy1fcxJJxJ3avyitZ4wNqAUEWNTIEgjNUDZnA",
                  oauth_token="2329651538-iZ2nEPBSIyl3u5AnU4ppfYEfJflTEeH6Krl8OO5", oauth_token_secret="V6ja2kfgl3aNr28QvOb9VmlbP8e9jxkora82wplPT43Vz")

    line1 = "five syllable line"
    line2 = "a seven syllable line"
    line3 = "five syllable line"
    poem = haiku([parse(line1), parse(line2), parse(line3)])

    #twitter.update_status(status=poem)
