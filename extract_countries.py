import json

with open("data/imdb_top_100_movies.json", "r", encoding="utf-8") as f:
    movies = json.load(f)

# Use a set to store unique countries
countries = set()

for m in movies:
    country_field = m.get("Country", "")
    # Split in case there are multiple (e.g., "United States|United Kingdom")
    for c in country_field.split("|"):
        c = c.strip()
        if c:
            countries.add(c)

# Sort alphabetically
sorted_countries = sorted(list(countries))

# Print list
print("Unique countries found:")
for c in sorted_countries:
    print("-", c)

# Optionally, save to a text file
with open("data/unique_countries.txt", "w", encoding="utf-8") as out:
    for c in sorted_countries:
        out.write(c + "\n")

print(f"\nTotal unique countries: {len(sorted_countries)}")
print("List saved to data/unique_countries.txt")