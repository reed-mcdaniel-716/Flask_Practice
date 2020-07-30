import sqlite3
# opening connection to a database file named database.db
connection = sqlite3.connect('database.db')


with open('schema.sql') as f:
    # executescript will execute all statements in f
    connection.executescript(f.read())

# create cursor to execute additional statements
cur = connection.cursor()

# create two new blog posts with qmark style for providing parameters
cur.execute("INSERT INTO posts (title, content) VALUES (?, ?)",('First Post', 'Content for the first post'))

cur.execute("INSERT INTO posts (title, content) VALUES (?, ?)",('Second Post', 'Content for the second post'))

# Save (commit) the changes
connection.commit()
# close connection
connection.close()
