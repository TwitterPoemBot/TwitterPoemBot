"""
	This is the website frontend to the TwitterPoemBot

	To run it on a debug server, just type in the following command:
		python tpgserver.py
"""
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)
queries = []

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
		queries.append(request.form["query"])
		return redirect(url_for("poem", id=(len(queries)-1)))

@app.route("/poem/<id>")
def poem(id):
	"""This function returns a poem with a given id.  This is mostly so that
	users can share a poem with other users.
	"""
	try:
		index = int(id)
		qry = queries[int(id)]
	except IndexError:
		index = -1
		qry = "query not found"
	except:
		index = -1
		qry = "invalid url"
	return render_template("poem.html", id=index, query=qry)

if __name__ == "__main__":
	app.run(debug=True, port=3000)
