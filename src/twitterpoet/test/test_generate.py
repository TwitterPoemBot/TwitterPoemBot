import unittest, logging, sys

sys.path.insert(0, '../')
from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from models.poems import haiku
from models.poems.parseLines import parse
from models.poems.poem import Tweet, Poem, engine
from generate import load_more_tweets
from sqlalchemy.sql import text

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://localhost/test'
db = SQLAlchemy(app)
db.drop_all()
db.create_all()

class TestGenerate(unittest.TestCase):

    def test_add_to_db(self):
        ''' Tests that a given hashtag returns valid tweets and is put in the database '''

        while True:
            hashtag = raw_input('Enter a hashtag (or q to quit): ')
            if hashtag == 'q':
                break
            load_more_tweets(hashtag, 1, 5)
            q = text('''SELECT * FROM tweet WHERE tweet.hashtag=:h''')
            tweets = engine.connect().execute(q, h=hashtag).fetchall()
            self.assertTrue(len(tweets) > 0)
            for t in tweets:
                print t.text
                db.session.query(Tweet).filter(Tweet.id==t.id).delete()
            db.session.commit()


if __name__ == '__main__':
    logging.basicConfig(stream=sys.stderr, level=logging.INFO)
    unittest.main()
