"""
	This is the website frontend to the TwitterPoemBot

	To run it on a debug server, just type in the following command:
		python main.py
"""
from flask import Flask, session, render_template, request, redirect, url_for
from generate import generatePoem
from models.poems.poem import Poem
from models.poems.poem import db
import logging
app = Flask(__name__)
queries = []
poemText = ""

@app.route("/")
def home_page():
    """This is the home page of the site, containing a search bar"""
    return render_template("index.html")

@app.route("/generate", methods=["POST"])
def generate():
    """This function is where the poem queries get sent to.  In the future,
    it will request a poem from our generator.
    """
    if request.method == "POST":
        print request.form["query"]
        poemText = ""
        if request.form["format"] == "0":
            poemText = generatePoem(request.form["query"], 'haiku').decode('ascii', 'ignore')
        if request.form["format"] == "1":
            poemText = generatePoem(request.form["query"], 'couplet').decode('ascii', 'ignore')
        p = Poem(poemText)
        p.save()
        print p.id
        queries.append(request.form["query"])
        return redirect(url_for("poem", id=str(p.id)))

@app.route("/poem/<id>")
def poem(id):
    """This function returns a poem with a given id.  This is mostly so that
    users can share a poem with other users.
    """
	# we probably shoudln't be using sessions for this stuff!
    print "poem page requested"
    print "id: ", id
    poem = Poem.query.filter_by(id=id).first()
    print "poem: ", poem
    if poem is None:
        return render_template("poem.html", poemText=["Invalid Poem!"])
    # associate each line with their twitter link
    lines = poem.poemText.split("\n")
    poems = lines[:len(lines)/2]
    links = ["http://" + x for x in lines[len(lines)/2:]]
    # zip them together
    pt = zip(poems, links)
    return render_template("poem.html", poemText=pt)


app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'

if __name__ == "__main__":
    db.create_all()
    app.run()
