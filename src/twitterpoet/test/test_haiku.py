import unittest, logging, sys

sys.path.insert(0, '../')
from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from models.poems import haiku
from models.poems.parseLines import parse
from models.poems.poem import Tweet, Poem

class TestHaiku(unittest.TestCase):
    def setUp(self):
      try:
        app = Flask(__name__)
        app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://localhost/test'
        db = SQLAlchemy(app)
        db.drop_all()
        db.create_all()
        db.session.add(Tweet('5 syllable line(1)', '', 'haiku_test1', 5, '', ''))
        db.session.add(Tweet('5 syllable line(2)', '', 'haiku_test1', 5, '', ''))
        db.session.add(Tweet('a seven syllable line', '', 'haiku_test1', 7, '', ''))

        db.session.add(Tweet('line1', '', 'haiku_test2', 2, '', ''))
        db.session.add(Tweet('line2', '', 'haiku_test2', 5, '', ''))
        db.session.add(Tweet('line3', '', 'haiku_test2', 7, '', ''))
        
        db.session.add(Tweet('5 syllable line', '', 'haiku_test3', 5, '', ''))
        db.session.add(Tweet('5 syllable lines', '', 'haiku_test3', 5, '', ''))
        db.session.add(Tweet('a seven syllable line', '', 'haiku_test3', 7, '', ''))
        db.session.add(Tweet('some filler words', '', 'haiku_test3', 3, '', ''))

        db.session.commit()
      except Exception as e:
        db.session.rollback()

    def test_valid(self):
        ''' Test a valid amount of tweets '''
        poem = haiku.haiku("haiku_test1")
        poem = [t.text for t in poem.tweets]
        print poem
        self.assertTrue((poem[0] == '5 syllable line(1)' and poem[2] == '5 syllable line(2)')
                     or (poem[2] == '5 syllable line(1)' and poem[0] == '5 syllable line(2)'))
        self.assertTrue(poem[1] == 'a seven syllable line')

    def test_invalid(self):
        ''' Tests insufficient amount of appropriate tweets '''
        corpus = [('a tweet', 2, 0), 
              ('just some stupid text', 5, 0),
              ('a frog jumps into the pond', 7, 0)]
        self.assertRaises(Exception, haiku.haiku, 'haiku_test2')

    def test_valid1(self):
        ''' Test extraneous tweets are ignored '''
        poem = haiku.haiku('haiku_test3')
        print poem
        poem = [t.text for t in poem.tweets]
        self.assertTrue((poem[0] == '5 syllable line' and poem[2] == '5 syllable lines')
                     or (poem[2] == '5 syllable line' and poem[0] == '5 syllable lines'))
        self.assertTrue(poem[1] == 'a seven syllable line')

if __name__ == '__main__':
    logging.basicConfig(stream=sys.stderr, level=logging.INFO)
    unittest.main()
