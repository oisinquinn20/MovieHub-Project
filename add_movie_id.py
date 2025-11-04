import uuid 
import json
import shutil
import os

# Create a backup file to be safe and add ids to movies 

# File paths
original_path = "data/imdb_top_100_movies_with_location.json"
backup_path = "data/imdb_top_100_movies_with_location_backup.json"

# Create a backup of the original file
if os.path.exists(original_path):
    shutil.copyfile(original_path, backup_path)
    print(f"Backup created at: {backup_path}")
else:
    print(f"Original file not found at: {original_path}")
    exit()

# Load movies from original file
with open(original_path, "r", encoding="utf-8") as f:
    movies = json.load(f)

# Add random ids using uuid4
for m in movies:
    if "id" not in m:
        m["id"] = str(uuid.uuid4())

# Save updated movies back to original file
with open(original_path, "w", encoding="utf-8") as f:
    json.dump(movies, f, ensure_ascii=False, indent=4)

print(f"ID added for {len(movies)} movies")



