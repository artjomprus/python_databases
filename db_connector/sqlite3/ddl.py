import sqlite3

conn = sqlite3.connect("movies.sqlite")

cursor = conn.cursor()

cursor.execute(
    """
CREATE TABLE movies(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT
)
"""
)

cursor.execute(
    """
ALTER TABLE movies ADD COLUMN release_date TEXT
"""
)

cursor.execute(
    """
DROP TABLE movies
"""
)

conn.commit()
conn.close()
