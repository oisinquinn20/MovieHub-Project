import json

# Helper functions to validate movies

#Ensure most basic fields are present
def validate_movie_fields(movie):
    required_fields = ["Title", "Year", "Genre(s)", "Director"]
    for field in required_fields:
        if field not in movie:
            return f"Missing required field: {field}"
    return None

# Ensure Unique titles
def is_duplicate_title(title, movies):
    return any(m["Title"].lower() == title.lower() for m in movies)

def assign_rank(movies):
    return max((m.get("Rank", 0) for m in movies), default=0) + 1

# Ensuring countries are correctly split if neccessary
def parse_countries(country_str):
    if not country_str:
        return [], []
    countries = [c.strip() for c in country_str.split("|") if c.strip()]
    locations = [
        {"Country": c, "Continent": "Unknown", "lat": None, "lon": None}
        for c in countries
    ]
    return countries, locations

# Save new movie added to the dataset
def save_movies_to_file(movies, path="data/imdb_top_100_movies_with_location.json"):
    with open(path, "w", encoding="utf-8") as f:
        json.dump(movies, f, ensure_ascii=False, indent=4)

# Get movie by unique id
def find_movie_by_id(movie_id, movies):
    return next((m for m in movies if m["id"] == movie_id), None)
