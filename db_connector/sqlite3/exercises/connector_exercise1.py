"""
PREREQUISITE: Having the books.sqlite database binary created via db_interactions.py

Add a new table called genres to the database.

The genres table stores the names of the different genres and it has a foreign key
relatioship with the books table.
This means that each book can be assigned one or more generes.

For this exercise also add some new data to the books table including the genre to each book.

Tasks
* Create the genres table / Relationship with the book table (1:1, 1:M, M:M)
* Insert some data into the books table and modify it as well (DDL)

Useful websites to check for this exercise:
https://www.sqlshack.com/learn-sql-types-of-relations/ -> Types of relationships
https://www.geeksforgeeks.org/sql-alter-add-drop-modify/ -> SQL
https://www.geeksforgeeks.org/sql-insert-statement/
https://www.geeksforgeeks.org/sql-create-table/

https://docs.python.org/3/library/sqlite3.html -> sqlite3 docs

"""
