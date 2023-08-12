"""
1. Alter table

* Add a rating column to the movies table
* Add a phone column to the customers table
* Create Indexes 
    - `idx_movies_director` on movies
    - `idx_movie_actors_movie` on movie_actors
    - `idx_movie_actors_actor` on movie_actors
    - `idx_rentals_movie` on rentals
    - `idx_rentals_customer` on rentals

2. Data manipulation

* directors 
    name
    Steven Spielberg
* movies
    title, director_id, release_date, genre, rental_price
    Jurassic Park, 1, 1993-0611, Adventure, 11
* customers
    username, email, phone
    yourname, test@test.com, 666123123
* rentals
        movie_id, customer_id, rental_date, return_date, returned
        1, 1, 2000-01-01, null, 0

3. Queries
* Get the title of a movie filtered by the director with a join
* Get title of a movie
* Get title, client_id, rental_date of that movie filtered by customer name
    HINTS: JOIN (rentals, customers) WHERE  

"""
