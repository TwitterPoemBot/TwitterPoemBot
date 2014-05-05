import unittest, logging, sys
sys.path.insert(0, '../')
from models.poems.limerick import limerick
from models.poems.parseLines import parse, parse_all
from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from models.poems.poem import Tweet, Poem, engine
from sqlalchemy.sql import text

class TestLimerick(unittest.TestCase):
    def setUp(self):
      try:
        app = Flask(__name__)
        app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://localhost/test'
        db = SQLAlchemy(app)
        db.drop_all()
        db.create_all()
        db.session.add(Tweet('The limerick packs laughs anatomical', 'url1', 'limerick_test1', 10, 'AO1F', 'anatomical'))
        db.session.add(Tweet('Into space that is quite economical', 'url2', 'limerick_test1', 10, 'AO1F', 'economical'))
        db.session.add(Tweet("But the good ones I've seen", 'url3', 'limerick_test1', 6, 'IY1N', 'seen'))
        db.session.add(Tweet("So seldom are clean", 'url4', 'limerick_test1', 6, 'IY1N', 'clean'))
        db.session.add(Tweet("And the clean ones so seldom are comical", 'url5', 'limerick_test1', 10, 'AO1F', 'comical'))
        
        db.session.commit()
      except Exception as e:
        db.session.rollback()

    def test_valid(self):
        ''' Test a valid amount of tweets '''
        poem = limerick('limerick_test1')
        poem = [t.text for t in poem.tweets]
        self.assertTrue(poem[0] == "The limerick packs laughs anatomical")
        self.assertTrue(poem[1] == "Into space that is quite economical")
        self.assertTrue(poem[2] == "But the good ones I've seen")
        self.assertTrue(poem[3] == "So seldom are clean")
        self.assertTrue(poem[4] == "And the clean ones so seldom are comical")

    def test_invalid(self):
        ''' Tests insufficient amount of appropriate tweets '''
        self.assertRaises(Exception, limerick, 'limerick_test2')

    def test_invalid_duplicates(self):
        ''' Test no duplicates '''
        self.assertRaises(Exception, limerick, 'limerick_test3')

    def test_invalid_nonenglish(self):
        ''' Test no non-english lines '''
        self.assertRaises(Exception, limerick, 'limerick_test4')

    def test_valid_variance(self):
        ''' Limerick should choose lines that have similar syllable counts '''
        poem = limerick('limerick_test1')
        poem = [t.text for t in poem.tweets]
        self.assertTrue(poem[0] == "The limerick packs laughs anatomical")
        self.assertTrue(poem[1] == "Into space that is quite economical")
        self.assertTrue(poem[2] == "But the good ones I've seen")
        self.assertTrue(poem[3] == "So seldom are clean")
        self.assertTrue(poem[4] == "And the clean ones so seldom are comical")

    def test_urls(self):
        ''' Ensure the poems have the correct urls attached '''
        poem = limerick('limerick_test1')
        poem = [t.url for t in poem.tweets]
        self.assertTrue(poem[0] == 'url1')
        self.assertTrue(poem[1] == 'url2')
        self.assertTrue(poem[2] == 'url3')
        self.assertTrue(poem[3] == 'url4')
        self.assertTrue(poem[4] == 'url5')


if __name__ == '__main__':
    logging.basicConfig(stream=sys.stderr, level=logging.INFO)
    unittest.main()
