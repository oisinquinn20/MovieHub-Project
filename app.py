import json
from flask import Flask, jsonify, make_response

app = Flask (__name__)

movies = []

with open("data/imdb_top_100_movies_with_location.json", "r", encoding="utf-8") as f:
    movies = json.load(f)

@app.route("/api/v1.0/movies", methods=["GET"])
def get_all_movies():
    return make_response(jsonify(movies), 200)

if __name__ == "__main__":
    app.run(debug=True)