from flask import Flask, render_template as rd

app = Flask(__name__)
@app.route("/")
def index():
    return rd("index.html")