from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from sqlalchemy.schema import UniqueConstraint
from sqlalchemy import create_engine
import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://tpg:uiucCS428@ampolgroup.com/twitterpoem'
# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://localhost/test'
db = SQLAlchemy(app)
engine = create_engine('mysql://tpg:uiucCS428@ampolgroup.com/twitterpoem', echo=True) #echo=True for debugging
# engine = create_engine('mysql://localhost/test', echo=True) #echo=True for debugging

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
    likes = db.Column(db.Integer)
    dislikes = db.Column(db.Integer)
    date = db.Column(db.DateTime)

    def __init__(self, tweets, hashtag, type):
        """construtor for Poem

        poemText: should be a string that represents the poem's text
        """
        self.tweets = tweets
        self.hashtag = hashtag
        self.likes = 0
        self.dislikes = 0
        self.type = type
        self.date = datetime.datetime.now()

    #def __repr__(self):
    #    return '<Poem %r>' % self.poemText

    def save(self):
        """Saves a poem to the db"""
        db.session.add(self)
        # for tweet in self.tweets:
            
        db.session.commit()
        return self.id

    def like():
        self.likes += 1

    def dislike():
        self.dislikes += 1

class Tweet(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    url = db.Column(db.String(140))
    text = db.Column(db.String(140))
    hashtag = db.Column(db.String(50))
    syllables = db.Column(db.Integer)
    phone = db.Column(db.String(10))
    last_word = db.Column(db.String(50))
    __table_args__ = (UniqueConstraint('text', 'hashtag'), )

    def __init__(self, text, url, hashtag, syllables, phone, last):
        self.text = text
        self.url = url
        self.hashtag = hashtag
        self.syllables = syllables
        self.phone = phone
        self.last_word = last
        # self.used = False

    def save(self):
        db.session.add(self)
        db.session.commit()
        return self.id

