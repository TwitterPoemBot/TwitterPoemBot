"""
	This is the website frontend to the TwitterPoemBot

	To run it on a debug server, just type in the following command:
		python tpgserver.py
"""
from flask import Flask, render_template, request, redirect, url_for
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
        poemText=generatePoem(request.form["query"])
        queries.append(request.form["query"])
        return redirect(url_for("poem", poemText=poemText))

@app.route("/poem/<poemText>")
def poem(poemText):
	"""This function returns a poem with a given id.  This is mostly so that
	users can share a poem with other users.
	"""
        print poemText
        return render_template("poem.html", poemText=poemText)

if __name__ == "__main__":
	app.run(debug=True, port=3000)
