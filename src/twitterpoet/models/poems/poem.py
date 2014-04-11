from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']= 'mysql://root:password@localhost/twitterpoem'
db = SQLAlchemy(app)

class Poem(db.Model):
	"""This is a model to allow poems to be saved in the db"""
    id = db.Column(db.Integer, primary_key=True)
    poemText = db.Column(db.String(300))

    def __init__(self, poemText):
		"""construtor for Poem
		
		poemText: should be a string that represents the poem's text
		"""
        self.poemText = poemText

    def __repr__(self):
        return '<Poem %r>' % self.poemText

    def save(self):
		"""Saves a poem to the db"""
        db.session.add(self)
        db.session.commit()
        return self.id
