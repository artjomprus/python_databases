import sqlite3


# First step - Create a connection
def create_connection(db_file: str) -> sqlite3.Connection | None:
    """Crete a connection to the SQLite database specified by db_file."""
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except Exception as e:
        print(e)
    return conn


# Second step - execute with a cursor
def create_tables(conn: sqlite3.Connection) -> None:
    """Create the tables of the Book database."""
    c = conn.cursor()

    c.execute(
        """CREATE TABLE IF NOT EXISTS authors (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL
        )
        """
    )

    c.execute(
        """CREATE TABLE IF NOT EXISTS books (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL,
        author_id INTEGER NOT NULL,
        genre_id INTEGER NOT NULL,
        FOREIGN KEY (author_id) REFERENCES authors (id),
        FOREIGN KEY (genre_id) REFERENCES genres (id)
        )
        """
    )

    c.execute(
        """CREATE TABLE IF NOT EXISTS genres (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL
        )
        """
    )

    conn.commit()


def insert_data(conn: sqlite3.Connection) -> None:
    """Insert data into the authors and books tables."""
    c = conn.cursor()

    c.execute("INSERT INTO authors (name) VALUES ('Stephen King')")
    c.execute("INSERT INTO authors (name) VALUES ('Tom Clancy')")
    c.execute("INSERT INTO authors (name) VALUES ('John Grishom')")

    c.execute(
        "INSERT INTO books (title, author_id, genre_id) VALUES ('The Shining', 1, 1)"
    )
    c.execute(
        "INSERT INTO books (title, author_id, genre_id) VALUES ('Patriot Games', 2, 2)"
    )
    c.execute(
        "INSERT INTO books (title, author_id, genre_id) VALUES ('The Firm', 3, 2)"
    )

    c.execute("INSERT INTO genres (name) VALUES ('Horror')")
    c.execute("INSERT INTO genres (name) VALUES ('Thriller')")

    conn.commit()


def main():
    """Create the SQLite database and insert data into it."""
    db_file: str = "books.sqlite"
    conn = create_connection(db_file)
    create_tables(conn)
    insert_data(conn)


if __name__ == "__main__":
    main()
