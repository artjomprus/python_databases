import sqlite3

conn = sqlite3.connect("library.db")
cursor = conn.cursor()

cursor.execute("""
    CREATE TABLE authors (
        author_id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL
    )
""")

cursor.execute("""
    CREATE TABLE books (
        book_id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL,
        author_id INTEGER,
        published_date TEXT,
        FOREIGN KEY (author_id) REFERENCES authors(author_id)
    )
""")

conn.commit()

cursor.execute("""
    ALTER TABLE books
    ADD COLUMN genre TEXT,
    ADD COLUMN publisher TEXT,
    ADD COLUMN ISBM INTEGER
""")

conn.commit()

cursor.execute("DROP TABLE IF EXISTS authors")

conn.commit()

conn.close()
