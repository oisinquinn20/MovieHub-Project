import json
import os

with open("data/imdb_top_100_movies.json", "r", encoding="utf-8") as f:
    movies = json.load(f)
    
# Extract unique countries
countries = set()
for m in movies:
    country_field = m.get("Country", "")
    for c in country_field.split("|"):
        c = c.strip()
        if c:
            countries.add(c)

# Location mapping template
country_data = {}
for c in sorted(countries):
    country_data[c] = {
        "Continent": "TODO",
        "lat": None,
        "lon": None
    }

# Save template as JSON file
os.makedirs("data", exist_ok=True)
template_path = "data/country_data_template.json"
with open(template_path, "w", encoding="utf-8") as f:
    json.dump(country_data, f, ensure_ascii=False, indent=4)

print(f"Created {template_path} — fill in Continent, lat, lon for each country.")
