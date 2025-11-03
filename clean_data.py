import pandas as pd

# Load CSV
csv_path = "data/imdb_top_100_movies.csv"
json_path = "data/imdb_top_100_movies.json"

# Read CSV into pandas DataFrame
df = pd.read_csv(csv_path)

# Convert to JSON
df.to_json(json_path, orient="records", indent=4)

print(f"JSON file saved at: {json_path}")