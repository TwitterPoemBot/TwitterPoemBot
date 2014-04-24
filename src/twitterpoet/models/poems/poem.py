from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']= 'mysql://tpg:uiucCS428@ampolgroup.com/twitterpoem'
db = SQLAlchemy(app)

tweets = db.Table('tweets',
    db.Column('poem_id', db.Integer, db.ForeignKey('poem.id')),
    db.Column('tweet_id', db.Integer, db.ForeignKey('tweet.id'))
)

class Poem(db.Model):
    """This is a model to allow poems to be saved in the db"""
    id = db.Column(db.Integer, primary_key=True)
    hashtag = db.Column(db.String(50))
    type = db.Column(db.String(50))
    tweets = db.relationship('Tweet', secondary=tweets, backref=db.backref('poems', lazy='dynamic'))

    def __init__(self, tweets, hashtag, type):
        """construtor for Poem

        poemText: should be a string that represents the poem's text
        """
        self.tweets = tweets
        self.hashtag = hashtag
        self.type = type

    #def __repr__(self):
    #    return '<Poem %r>' % self.poemText

    def save(self):
        """Saves a poem to the db"""
        db.session.add(self)
        for tweet in self.tweets:
            db.session.add(tweet)
        db.session.commit()
        return self.id
        
class Tweet(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    url = db.Column(db.String(300))
    text = db.Column(db.String(300))
    hashtag = db.Column(db.String(50))
    
    
    def __init__(self, text, url, hashtag):
        self.text = text
        self.url = url
        self.hashtag = hashtag
        
    def save(self):
        db.session.add(self)
        db.session.commit()
        return self.id
