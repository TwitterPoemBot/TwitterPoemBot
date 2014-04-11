"""
	This is the website frontend to the TwitterPoemBot

	To run it on a debug server, just type in the following command:
		python main.py
"""
from flask import Flask, session, render_template, request, redirect, url_for
from generate import generatePoem
from models.poems.poem import Poem
from models.poems.poem import db
from twitter import getTwitter
from models.tweets.get_tweets2 import get_trending_topics
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
            twitter = getTwitter()
            session["trending"] = get_trending_topics(twitter)
            session["lastUpdateTime"] = datetime.datetime.now()
    except KeyError:
        twitter = getTwitter()
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
                poemText = generatePoem(request.form["query"], 'haiku').decode('ascii', 'ignore')
            if request.form["format"] == "1":
                poemText = generatePoem(request.form["query"], 'couplet').decode('ascii', 'ignore')
            if request.form["format"] == "2":
                poemText = generatePoem(request.form["query"], 'limerick').decode('ascii', 'ignore')
        except:
            print "there was an error with this query:"
            print request.form
            return redirect(url_for("poem", id=str(-1)))
        p = Poem(poemText)
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
    print "poem: ", poem
    if poem is None:
        return render_template("poem.html", poemText=["Poem not found."])
    # associate each line with their twitter link
    lines = poem.poemText.split("\n")
    print len(lines)
    poem = lines[:len(lines)/2]
    links = [("http://" + x) for x in lines[len(lines)/2:]]
    # zip them together
    pt = zip(poem, links)
    return render_template("poem.html", poemText=pt)


app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'

if __name__ == "__main__":
    db.create_all()
    app.run()
