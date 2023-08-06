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


def fetch_books(
    conn: sqlite3.Connection | None, word: str, filter_by: str | None = None
) -> list | None:
    """Fetch books by author or genre.

    Parameters
    ----------
    conn : sqlite3.Connection
        The connection object to the SQLite database.
    filter_by : str
        The filter to use. Can be "author" or "genre".

    Returns
    -------
    List
        Books that match the filter.
    """

    column = filter_by

    if column:
        try:
            query = f"""SELECT title
            FROM books
            WHERE {column+"_id"} IN (
                SELECT id
                FROM {column+"s"}
                WHERE {column+"_id"} = {word}
            )
            """  # Second exercise modifications in here
            c = conn.cursor()
            c.execute(query)
            books = [row for row in c.fetchall()]
            return books

        except Exception as e:
            raise ValueError(f"Invalid filter_by value: {e}")

    raise ValueError("A filter of either 'author' or 'genre' is necessary.")


def main():
    db_file: str = "books.sqlite"
    conn = create_connection(db_file)

    books_author = fetch_books(conn=conn, word="3", filter_by="author")

    for book in books_author:
        print(f"Title by author: {book}")

    books_genre = fetch_books(conn=conn, word="2", filter_by="genre")

    for book in books_genre:
        print(f"Title by genre: {book}")


if __name__ == "__main__":
    main()
