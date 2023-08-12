import sqlite3

conn = sqlite3.connect("movies.sqlite")
cursor = conn.cursor()

cursor.execute("ALTER TABLE movies ADD COLUMN rating REAL")
cursor.execute("ALTER TABLE customers ADD COLUMN phone TEXT")

cursor.execute("CREATE INDEX idx_movies_director ON movies(director_id)")
cursor.execute("CREATE INDEX idx_movie_actors_movie ON movie_actors(movie_id)")
cursor.execute("CREATE INDEX idx_movie_actors_actor ON movie_actors(actor_id)")
cursor.execute("CREATE INDEX idx_rentals_movie ON rentals(movie_id)")
cursor.execute("CREATE INDEX idx_rentals_customer ON rentals(customer_id)")

conn.commit()

cursor.execute("INSERT INTO directors (name) VALUES ('Christopher Nolan')")
cursor.execute(
    "INSERT INTO movies (title, director_id, release_date, genre, rental_price) VALUES ('Inception', 1, '2010-07-8', 'Sci-Fi', 11)"
)
cursor.execute("INSERT INTO customers (username, email, phone) VALUES ('Artjom', 'test@test.com', '666123123')")
cursor.execute("INSERT INTO rentals (movie_id, customer_id, rental_date, return_date, returned) VALUES (1, 1, '2000-01-01', NULL, 0)")

conn.commit()

director_name = 'Christopher Nolan'
cursor.execute(
    "SELECT movies.title FROM movies JOIN directors ON movies.director_id = directors.director_id WHERE directors.name = ?",
    (director_name,)
)
result = cursor.fetchall()
print("Movies directed by", director_name)
for row in result:
    print(row[0])

movie_id = 1
cursor.execute("SELECT title FROM movies WHERE movies_id = ?", (movie_id,))
result = cursor.fetchone()
print("Movie title:", result[0])

customer_name = 'Artjom'
cursor.execute(
    "SELECT movies.title, rentals.customer_id, rentals.rental_date FROM rentals JOIN movies ON rentals.movie_id = movies.movies_id JOIN customers ON rentals.customer_id = customers.customers_id WHERE customers.username = ?",
    (customer_name,)
)
result = cursor.fetchall()
print("Movies rented by", customer_name)
for row in result:
    print("Title:", row[0], "Customer ID:", row[1], "Rental Date:", row[2])

conn.close()
