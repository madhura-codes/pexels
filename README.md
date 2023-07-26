# Pexels

For this exercise, you will be asked to write a simple ETL job using a SQLite database and the open Pexels API. Pexels is a free service where users can upload and download photographs and videos in categories such as Nature and People. The REST API can be used to list resources, using search keys. You will need to create a free Pexels account and retrieve your API key (instructions: https://www.pexels.com/api/documentation/#authorization). The API endpoints and objects you will retrieve are thoroughly documented at the same link. You will be working with the “Photo” resource in this exercise.

Please provide complete Python and SQL code that we can run for each of the steps. Feel free to include in-line comments explaining your code. You can send us a file, or a link to a github repository that we can access containing your code. The total time taken to complete all steps in this exercise should be 2-3 hours at most. Please try to make your code efficient and presentable, as you would when writing production code.


Please use some version of Python 3, and the sqlite3 and requests libraries.

Step 1: Database preparation

Create `photos` and `photo_sources` tables in a SQLite database. The `photos` table must include all of the fields in the “Photos” object except the nested `src` fields. The `photo_sources` table will include the child `src` objects, so make sure there is a key to join between the tables. Please be sure to include DDL statements in your code.

Step 2: Connection class

Create a class with method(s) for connecting to the Pexels API and retrieving a page of results. Following security best practices, DO NOT save your API key in your code! Use an environment variable or other means to retrieve your saved key.

Step 3: ETL

Write a function to retrieve 1000 Photo records (filtered to “nature”) and store them in the SQLite database. When complete, there should be 1000 records in the photos table and 8000 records in the photo_sources table.

Step 4: Queries

Produce SQL queries to determine the top 5 photographers (by # of photos), how many photos have an `average_color` that begins with “#a” or “#A”, and the average width and height of all photos in the table.
