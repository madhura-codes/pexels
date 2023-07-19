import sqlite3
# Function to execute an SQL query and fetch results
def execute_query(query):
    conn = sqlite3.connect("pexels.db")
    cursor = conn.cursor()
    cursor.execute(query)
    results = cursor.fetchall()
    conn.close()
    return results

#Photo Table counts
photo_count_query = """
    SELECT COUNT(*) AS photo_count
    FROM photos
"""
photo_counts = execute_query(photo_count_query)[0][0]

# Photo Sources counts
photo_src_count_query = """
    SELECT COUNT(*) AS photo_src_count
    FROM photo_src
"""
photo_src_counts = execute_query(photo_src_count_query)[0][0]

# Top 5 photographers by number of photos
top_photographers_query = """
    SELECT photographer_id, photographer, COUNT(*) AS photo_count
    FROM photos
    GROUP BY 1,2
    ORDER BY photo_count DESC
    LIMIT 5
"""
top_photographers = execute_query(top_photographers_query)

# Number of photos with average_color starting with "#a" or "#A"
color_filter_query = """
    SELECT COUNT(*) AS color_count
    FROM photos
    WHERE avg_color LIKE '#a%' OR avg_color LIKE '#A%'
"""
color_count = execute_query(color_filter_query)[0][0]

# Average width and height of all photos
average_dimensions_query = """
    SELECT AVG(width) AS average_width, AVG(height) AS average_height
    FROM photos
"""
average_dimensions = execute_query(average_dimensions_query)[0]

print("\nNumber of photos in photo table:")
print(photo_counts)

print("\nNumber of photos in photo sources:")
print(photo_src_counts)

print("\nTop 5 photographers:")
for photographer_id, photographer, photo_count in top_photographers:
    print(f"{photographer}: {photo_count} photos")

print("\nNumber of photos with average_color starting with '#a' or '#A':")
print(color_count)

print("\nAverage dimensions of all photos:")
print(f"Width: {average_dimensions[0]}")
print(f"Height: {average_dimensions[1]}")
print("\n")
