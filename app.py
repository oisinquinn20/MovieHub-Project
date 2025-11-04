import json
from flask import Flask, jsonify, make_response, request
from movie_validators import (
    validate_movie_fields,
    is_duplicate_title,
    assign_rank,
    parse_countries,
    save_movies_to_file
)

app = Flask (__name__)

movies = []

with open("data/imdb_top_100_movies_with_location.json", "r", encoding="utf-8") as f:
    movies = json.load(f)


@app.route("/api/v1.0/movies", methods=["GET"])
def get_all_movies():
    return make_response(jsonify(movies), 200)

@app.route("/api/v1.0/movies/<string:title>/review", methods=["POST"])
def add_review(title):
    data = request.get_json()
    review_text = data.get("Review")

    if not review_text:
        return make_response(jsonify({"error": "Review text is required."}), 400)

    movie = next((m for m in movies if m["Title"].lower() == title.lower()), None)
    if not movie:
        return make_response(jsonify({"error": f"Movie '{title}' not found."}), 404)

    movie["Review"] = review_text

    with open("data/imdb_top_100_movies_with_location.json", "w", encoding="utf-8") as f:
        json.dump(movies, f, ensure_ascii=False, indent=4)

    return make_response(jsonify({
        "movie": movie
    }), 200)

@app.route("/api/v1.0/movies", methods = ["POST"])
def create_movie():
    new_movie = request.get_json()

    error = validate_movie_fields(new_movie)
    if error:
        return make_response(jsonify({"error": error}), 400)

    if is_duplicate_title(new_movie["Title"], movies):
        return make_response(jsonify({"error": "Movie already exists."}), 409)


    new_movie["Rank"] = assign_rank(movies)
    new_movie["Country"], new_movie["Location"] = parse_countries(new_movie.get("Country", ""))
    new_movie["Review"] = None

    movies.append(new_movie)
    save_movies_to_file(movies)

    return make_response(jsonify({
        "movie": new_movie
    }), 201)

@app.route("/api/v1.0/movies/<string:title>", methods=["DELETE"])
def delete_movie(title):
    global movies

    # Find the movie by title
    movie = next((m for m in movies if m["Title"].lower() == title.lower()), None)

    if not movie:
        return make_response(jsonify({"error": f"'{title}' not found."}), 404)

    # Remove it from the list
    movies = [m for m in movies if m["Title"].lower() != title.lower()]

    # Save to file
    save_movies_to_file(movies)

    return make_response(jsonify({"message": f"'{title}' deleted successfully."}), 200)

@app.route("/api/v1.0/movies/<string:title>/review", methods=["DELETE"])
def delete_review(title):
    movie = next((m for m in movies if m["Title"].lower() == title.lower()), None)

    if not movie.get("Review"): return make_response(jsonify({"message": f"No review found for '{title}'."}), 200)

    movie["Review"] = None
    save_movies_to_file(movies)

    return make_response(jsonify({
        "message": f"'{title}' Review deleted successfully."
    }), 200)


if __name__ == "__main__":
    app.run(debug=True)