import sqlite3

conn = sqlite3.connect("movies.sqlite")
cursor = conn.cursor()


# 1. Create a Database and Tables
cursor.execute(
    """
CREATE TABLE authors(
            author_id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL
)
"""
)

cursor.execute(
    """
CREATE TABLE books(
            book_id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            author_id INTEGER,
            published_date TEXT,
            FOREIGN KEY (author_id) REFERENCES authors(author_id)
)
"""
)

# 2. Alter the Schema
cursor.execute(
    """
ALTER TABLE books ADD COLUMN genre TEXT
"""
)

cursor.execute(
    """
ALTER TABLE books ADD COLUMN publisher TEXT
"""
)

cursor.execute(
    """
ALTER TABLE books ADD COLUMN ISBM INTEGER
"""
)

conn.commit()
conn.close()


authors_drop = input("You want to drop the authors table? <yes/no>")
if authors_drop == "yes":
    # 3. Delete a Table
    conn = sqlite3.connect("movies.sqlite")
    cursor = conn.cursor()

    cursor.execute(
        """
        DROP TABLE authors
        """
    )
    conn.commit()
    conn.close()
else:
    print("Sure I will not delete it :) ")
