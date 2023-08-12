"""
Exercise 3

Objective: Create a database for managing a library, which includes tables 
for books and authors. Perform specific tasks to manipulate these tables.

TASKS:

1. Create a Database and Tables
    - Create a table name `authors` within the following columns:
    * `author_id`: Integer, Primary Key, Autoincrement
    * `name`: Text, Not NULL

    - Create a table named `books` with the following columns:
    * `book_id`: Integer, Primary Key, Autoincrement
    * title: Text, Not NULL
    * `author_id`: Integer, Foreign Key referencing authors.author_id
    * `published_date`: Text

2. Alter the Schema
    * Add columns genre:text and publisher:text and ISBM: integer

3. Delete a Table
    * Delete the `authors` table.
"""
