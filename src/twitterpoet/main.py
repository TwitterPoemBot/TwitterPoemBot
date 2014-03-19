"""
	This is the website frontend to the TwitterPoemBot

	To run it on a debug server, just type in the following command:
		python tpgserver.py
"""
from flask import Flask, session, render_template, request, redirect, url_for
from generate import generatePoem

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
        session["poemText"]=generatePoem(request.form["query"]).encode('ascii', 'ignore')
        queries.append(request.form["query"])
        return redirect(url_for("poem"))

@app.route("/poem")
def poem():
	"""This function returns a poem with a given id.  This is mostly so that
	users can share a poem with other users.
	"""
        print session["poemText"]
        return render_template("poem.html", poemText=session["poemText"].split('\n'))

if __name__ == "__main__":
    app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'
    app.run(debug=True, port=3000)
