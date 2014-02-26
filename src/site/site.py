from flask import Flask, render_template, request, redirect, url_for
app = Flask(__name__)

@app.route("/")
def home_page():
	return render_template("index.html")

@app.route("/generate", methods=["POST"])
def generate():
	if request.method == "POST":
		print request.form["query"]
		return redirect(url_for("poem", id=1124))

@app.route("/poem/<id>")
def poem(id):
	return render_template("poem.html", id=id)

if __name__ == "__main__":
	app.run(debug=True, port=3000)
