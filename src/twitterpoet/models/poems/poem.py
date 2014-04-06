from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']= 'mysql://root:password@localhost/twitterpoem'
db = SQLAlchemy(app)

"""This is a model to allow poems to be saved in the db"""
class Poem(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    poemText = db.Column(db.String(300))

    """construtor for Poem"""
    def __init__(self, poemText):
        self.poemText = poemText

    def __repr__(self):
        return '<Poem %r>' % self.poemText

    """Saves a poem to the db"""
    def save(self):
        db.session.add(self)
        db.session.commit()
