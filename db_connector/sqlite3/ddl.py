import sqlite3

conn = sqlite3.connect("movies.sqlite")

cursor = conn.cursor()

# cursor.execute(
#     """
# CREATE TABLE movies(
#             id INTEGER PRIMARY KEY AUTOINCREMENT,
#             title TEXT
# )
# """
# )

# cursor.execute(
#     """
# ALTER TABLE movies ADD COLUMN release_date TEXT
# """
# )

# cursor.execute(
#     """
# DROP TABLE movies
# """
# )

# conn.commit()
# conn.close()


# Netflix copycat
# directors, movies, actors, movie_actors, customers, rentals

# Create directors table
cursor.execute(
    """
CREATE TABLE directors(
        director_id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL
)
"""
)

# Create movies table
cursor.execute(
    """
CREATE TABLE movies(
        movies_id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL,
        director_id INTEGER,
        release_date TEXT,
        genre TEXT,
        rental_price REAL,
        FOREIGN KEY (director_id) REFERENCES directors(director_id)
)
"""
)

# Create actors table
cursor.execute(
    """
CREATE TABLE actors(
        actor_id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL
)
"""
)

# Create movie_actors table M:M
cursor.execute(
    """
CREATE TABLE movie_actors(
        movie_id INTEGER,
        actor_id INTEGER,
        FOREIGN KEY (movie_id) REFERENCES movies(movie_id),
        FOREIGN KEY (actor_id) REFERENCES actors(actor_id)
)
"""
)

# Create customers table
cursor.execute(
    """
CREATE TABLE customers(
        customers_id INTEGER,
        username TEXT NOT NULL,
        email TEXT NOT NULL
)
"""
)

# Create rentals table
cursor.execute(
    """
CREATE TABLE rentals(
        rental_id INTEGER PRIMARY KEY AUTOINCREMENT,
        movie_id INTEGER,
        customer_id INTEGER,
        rental_date TEXT NOT NULL,
        return_date TEXT,
        returned INTEGER,
        FOREIGN KEY (movie_id) REFERENCES movies(movie_id),
        FOREIGN KEY (customer_id) REFERENCES customers(customer_id)
)
"""
)

conn.commit()
conn.close()
