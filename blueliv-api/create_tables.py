import sqlite3

connection = sqlite3.connect('data.db')

cursor = connection.cursor()

create_table = "CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, username text, password text)"
cursor.execute(create_table)

create_table = "CREATE TABLE IF NOT EXISTS threats (id INTEGER PRIMARY KEY, author text, topic text, post_date text)"
cursor.execute(create_table)

connection.commit()

connection.close()