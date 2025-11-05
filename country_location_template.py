import json
import os

# Load movies and extract unique countries
with open("data/imdb_top_100_movies.json", "r", encoding="utf-8") as f:
    movies = json.load(f)

countries = set()
for m in movies:
    for c in m.get("Country", "").split("|"):
        c = c.strip()
        if c:
            countries.add(c)

# Load current template
template_path = "data/country_data_template.json"
if os.path.exists(template_path):
    with open(template_path, "r", encoding="utf-8") as f:
        country_data = json.load(f)
else:
    country_data = {}

# Add any new countries to the template
new_entries = 0
for c in sorted(countries):
    if c not in country_data:
        country_data[c] = {
            "Continent": "TODO",
            "lat": None,
            "lon": None
        }
        new_entries += 1

# Save the updated template
with open(template_path, "w", encoding="utf-8") as f:
    json.dump(country_data, f, ensure_ascii=False, indent=4)

print(f"Updated {template_path}")
print(f"Added {new_entries} new countries")
