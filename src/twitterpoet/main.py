"""
    This is the website frontend to the TwitterPoemBot

    To run it on a debug server, just type in the following command:
        python main.py
"""
from flask import Flask, session, render_template, request, redirect, url_for
from generate import generatePoem
from models.poems.poem import Poem
from models.poems.poem import db
from models.tweets.get_tweets2 import connect 
from models.tweets.get_tweets2 import get_trending_topics
from models.tweets.send_tweet import sendPoem
import logging
import datetime
app = Flask(__name__)
trending = ""

@app.route("/")
def home_page():
    """This is the home page of the site, containing topics.
    Topics are refreshed every 20 seconds.
    """
    try:   
        diff = datetime.datetime.now() - session["lastUpdateTime"]
        if diff.total_seconds() > 20:
            twitter = connect()
            session["trending"] = get_trending_topics(twitter)
            session["lastUpdateTime"] = datetime.datetime.now()
    except KeyError:
        twitter = connect()
        session["trending"] = get_trending_topics(twitter)
        session["lastUpdateTime"] = datetime.datetime.now()
    return render_template("index.html", trending=session["trending"])

@app.route("/generate", methods=["POST"])
def generate():
    """This function is where the poem generation queries get sent to.  The post request
    should include the following fields:

    format: determines what kind of poem will be generated.  Here is a list of
        types of poems that are accepted through this interface:
        0: Haiku
        1: Couplet
    query: This is the text that's put into the text box.  This usually indicates the
        topic that the user wants the poem to be based off of.
    """
    if request.method == "POST":
        print request.form["query"]
        try:
            if request.form["format"] == "0":
                poem = generatePoem(request.form["query"], 'haiku')
            if request.form["format"] == "1":
                poem = generatePoem(request.form["query"], 'couplet')
            if request.form["format"] == "2":
                poem = generatePoem(request.form["query"], 'limerick')
        except:
            print "there was an error with this query:"
            print request.form
            return redirect(url_for("poem", id=str(-1)))
        p = poem
        p.save()
        print p.id
        return redirect(url_for("poem", id=str(p.id)))

@app.route("/poem/<id>")
def poem(id):
    """This function returns a poem with a given id.  This is mostly so that
    users can share a poem with other users.

    An id of -1 indicates that there was an error.
    """
    if id == -1:
        render_template("poem.html", poemText=["There was an error"])
    print "poem page requested"
    print "id: ", id
    poem = Poem.query.filter_by(id=id).first()
    if poem is None:
        return render_template("poem.html", poemText=["Poem not found."])
    # associate each line with their twitter link
    poemLines = []
    poemLines += [tweet.text for tweet in poem.tweets]
    poemLinks = []
    poemLinks += [tweet.url for tweet in poem.tweets]
    # zip them together
    pt = zip(poemLines, poemLinks)
    return render_template("poem.html", poemText=pt, poemID=id)

@app.route("/sendtweet", methods=["POST"])
def sendtweet():
    print "sending tweet"
    print request.form["id"]
    twitter = connect()
    poem = Poem.query.filter_by(id=request.form["id"]).first()
    if poem is None:
        return render_template("poem.html", poemText=["Poem not found."])
    sendPoem(twitter, poem)
    print "send success"
    return redirect(url_for("poem", id=str(poem.id)))

app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'

if __name__ == "__main__":
    db.create_all()
    app.run()
