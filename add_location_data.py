import json
import os

# Load country mapping file 
try:
    with open("data/country_data_template.json", "r", encoding="utf-8") as f:
        country_data = json.load(f)
        print(f"Loaded country_data_template.json")
except FileNotFoundError:
    print("country_data_template.json not found. Please run country_location_template.py first.")
    exit()

# Load IMDb dataset

with open("data/imdb_top_100_movies.json", "r", encoding="utf-8") as f:
    movies = json.load(f)
    print(f"Loaded imdb_top_100_movies.json")

# Add location data to movie dataset
for m in movies:
    country_field = m.get("Country", "")
    countries = [c.strip() for c in country_field.split("|") if c.strip()]

    # Replace Country string with a list
    m["Country"] = countries
    m["Location"] = []

    for country in countries:
        if country in country_data:
            loc = {"Country": country, **country_data[country]}
        else:
            loc = {"Country": country, "Continent": "Unknown", "lat": None, "lon": None}
        m["Location"].append(loc)

# Save updated data
base_dir = os.path.dirname(__file__)
output_path = os.path.join(base_dir, "data", "imdb_top_100_movies_with_location.json")

with open(output_path, "w", encoding="utf-8") as f:
    json.dump(movies, f, ensure_ascii=False, indent=4)

print(f"Location data added successfully!")
print(f"Saved new dataset as: {output_path}")

