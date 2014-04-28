import unittest, sys

sys.path.insert(0, '../')
from models.poems import couplet
from models.poems.parseLines import parse
from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from models.poems.poem import Tweet, Poem

class TestCouplet(unittest.TestCase):
    def setUp(self):
      try:
        app = Flask(__name__)
        app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://localhost/test'
        db = SQLAlchemy(app)
        db.drop_all()
        db.create_all()
        print 'adding'
        db.session.add(Tweet('Boy I like the bay', '', 'couplet_test1', 5, 'AO1F', 'bay'))
        db.session.add(Tweet('We will go there today!', '', 'couplet_test1', 6, 'AO1F', 'today'))
        db.session.add(Tweet('some filler', '', 'couplet_test1', 3, '', 'filler'))

        db.session.add(Tweet('Well gosh, I hate the bay', '', 'couplet_test2', 6, 'AO1F', 'bay'))
        db.session.add(Tweet('You must go there today!', '', 'couplet_test2', 6, 'AO1F', 'today'))
        db.session.add(Tweet('some filler', '', 'couplet_test2', 3, '', 'filler'))

        db.session.add(Tweet('some filler', '', 'couplet_test4', 3, 'AO1F', 'filler'))
        db.session.add(Tweet('dumb filler', '', 'couplet_test4', 3, 'AO1F', 'filler'))
        
        db.session.commit()
      except Exception as e:
        print '='*10
        print e
        db.session.rollback()

    def test_one_more_syllable(self):
        ''' Tests that a couplet can be made if the lines are one syllable difference  '''

        poem = couplet.couplet('couplet_test1')
        poem = [t.text for t in poem.tweets]
        print poem
        self.assertTrue((poem[0] == 'Boy I like the bay' and poem[1] == 'We will go there today!')
                     or (poem[1] == 'Boy I like the bay' and poem[0] == 'We will go there today!'))

    def test_same_syllables(self):
        ''' Tests that a couplet can be made with two lines w/ same # syllables  '''

        corpus = [parse('Well gosh, I hate the bay'), 
              parse('You must go there today!'),
              parse('some filler')]
        poem = couplet.couplet('couplet_test2')
        poem = [t.text for t in poem.tweets]
        print poem
        self.assertTrue((poem[0] == 'Well gosh, I hate the bay' and poem[1] == 'You must go there today!')
                     or (poem[1] == 'Well gosh, I hate the bay' and poem[0] == 'You must go there today!'))

    def test_syllable_discrep(self):
        ''' Tests that a couplet cannot be made if there is a difference of more than one syllable  '''

        self.assertRaises(Exception, couplet.couplet, 'couplet_test3')


    def test_invalid(self):
        ''' Tests insufficient amount of appropriate tweets '''
        self.assertRaises(Exception, couplet.couplet, 'couplet_test4')

    def test_same_word(self):
        ''' Tests that couplet can't be made with lines ending in same word '''
        self.assertRaises(Exception, couplet.couplet, 'couplet_test5')

if __name__ == '__main__':
    unittest.main()
