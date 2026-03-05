# app.py
from flask import Flask, render_template, request, jsonify
from response import get_quote

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/main")
def main():
    return render_template("main.html")


@app.route("/mood/<mood>")
def mood_page(mood: str):
    allowed_moods = ["happy", "sad", "lonely", "tired", "angry", "calm"]
    if mood not in allowed_moods:
        return "Invalid Mood", 404
    return render_template(f"{mood}.html", mood=mood)


@app.route("/submit", methods=["POST"])
def submit():
    data = request.json
    mood = data.get("mood")
    score = int(data.get("score"))
    quote = get_quote(mood, score)
    return jsonify({"quote": quote})


if __name__ == "__main__":
    app.run(debug=True)