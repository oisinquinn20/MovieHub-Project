import json
from flask import Flask, jsonify, make_response

app = Flask (__name__)

movies = []

with open("data/imdb_top_100_movies.json", "r", encoding="utf-8") as f:
    movies = json.load(f)

@app.route("/movies", methods=["GET"])
def get_movies():
    return jsonify(movies), 200

if __name__ == "__main__":
    app.run(debug=True)