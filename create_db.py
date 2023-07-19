import sqlite3

# Function to create tables in the SQLite database
def create_tables():
    conn = sqlite3.connect("pexels.db")
    cursor = conn.cursor()

    # Create the photos table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS photos (
            id INTEGER PRIMARY KEY,
            width INTEGER,
            height INTEGER,
            url TEXT,
            photographer TEXT,
            photographer_url TEXT,
            photographer_id INTEGER,
            avg_color TEXT,
            liked BOOLEAN
        )
    """)

    # Create the photo_sources table. Since the question said the photo sources table should have 8000 rows created the following table structure.
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS photo_src (
            photo_id INTEGER,
            src_type TEXT,
            src_url TEXT,
            FOREIGN KEY (photo_id) REFERENCES photos (id)
        )
    """)

    conn.commit()
    conn.close()

# Create tables in the SQLite database
create_tables()
