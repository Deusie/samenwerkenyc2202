from flask import Flask, render_template
from bestandjeJesse import *

app = Flask(__name__)

@app.route("/")
def index():    
    return render_template("index.html")

@app.route("/jesse")
def methodeEen():
    terug = eenmethodeinbestand1()
    return "methodeeen"+terug

@app.route("/twee")
def methodeTwee():
    terug = methodeMetReadFile()
    return "methodeEen "+terug

# @app.route("/metinput/<username>")
# def hello_world(username):
#     return f"<p>Hello,{username} World!</p>"