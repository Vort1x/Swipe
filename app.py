import os
from flask import Flask, render_template
import random

app = Flask(__name__)

@app.route("/")
def index():
    try:
        with open("photos.txt", "r", encoding="utf-8") as f:
            photos = [line.strip() for line in f if line.strip()]
    except FileNotFoundError:
        photos = []

    random.shuffle(photos)
    return render_template("index.html", photos=photos)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=True)
