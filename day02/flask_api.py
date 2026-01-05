from flask import Flask, jsonify, render_template
import requests

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/verse/<book>/<int:chapter>/<int:verse>", methods=["GET"])
def get_verse_api(book, chapter, verse):
    url = f"https://bible-api.com/{book}%20{chapter}:{verse}"
    response = requests.get(url)
    return jsonify(response.json())

app.run()