import sqlite3

connection = sqlite3.connect('database.db')


with open('schema.sql') as f:
    connection.executescript(f.read())

cur = connection.cursor()

cur.execute("INSERT INTO user (username, email, pass) VALUES (?, ?, ?)",
            ('fikri', 'mfikrihasani@gmail.com', '12345678')
            )

# cur.execute('''
#     CREATE TABLE IF NOT EXISTS users (
#         id INTEGER PRIMARY KEY AUTOINCREMENT,
#         username TEXT NOT NULL,
#         email TEXT NOT NULL,
#         password TEXT NOT NULL
#     )
# ''')

connection.commit()
connection.close()