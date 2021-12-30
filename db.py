import sqlite3

conn = sqlite3.connect("books.sqlite")

cursor = conn.cursor()

sql_query = """ 
    CREATE TABLE books (
        id int AUTO_INCREMENT PRIMARY KEY,
        author varchar(255) NOT NULL,
        title varchar(255) NOt NULL
    )
    """

cursor.execute(sql_query)