from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/winner!")
def winner():
    return render_template("winner.html")

app.run(host="0.0.0.0", port=80, debug=True)