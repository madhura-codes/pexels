import sqlite3
import time
import os
import requests

# Connection class
class PexelsAPIConnection:
    def __init__(self):
        self.api_key = os.environ.get("PEXEL_API_KEY")  # Retrieve the API key from an environment variable

    def get_photos(self, url):
        headers = {"Authorization": self.api_key}
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            return response.json()
        else:
            return None

# Function to perform the transform process
def perform_transform():
    connection = PexelsAPIConnection()

    photos = []
    url = f"https://api.pexels.com/v1/search?query=nature&page=1&per_page=50"
    for page in range (1, 21):                    # 50 photos per page. we need 1000 so we iterate 20 times
        response = connection.get_photos(url=url)
        if response:
            photos.extend(response.get("photos", []))
            url = response.get("next_page")
            #print(url)

    # Connect to the SQLite database
    conn = sqlite3.connect("pexels.db")
    cursor = conn.cursor()

    # Insert data into the photos and photo_sources tables
    for photo in photos:
        # Insert into photos table
        cursor.execute("""
            INSERT INTO photos (id, width, height, url, photographer, photographer_url, photographer_id, avg_color, liked)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, (
            photo["id"],
            photo["width"],
            photo["height"],
            photo["url"],
            photo["photographer"],
            photo["photographer_url"],
            photo["photographer_id"],
            photo["avg_color"],
            photo["liked"]
        ))

        src_keys = []
        src_keys = photo["src"].keys()  # Get all src keys to iterate through src child

        for key in src_keys:
            # Insert into photo sources table
            cursor.execute("""
                INSERT INTO photo_src (photo_id, src_type, src_url)
                VALUES (?, ?, ?)
            """, (
                photo["id"],
                key,
                photo["src"][key]
            ))

    conn.commit()
    conn.close()

    print("ETL process completed successfully.")

# Perform the Transform process
perform_transform()
