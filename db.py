import sqlite3

conn = sqlite3.connect("test.db")
cursor = conn.cursor()

cursor.execute("CREATE TABLE IF NOT EXISTS users (id INTEGER, username TEXT)")

cursor.execute("INSERT INTO users VALUES (1, 'admin')")
cursor.execute("INSERT INTO users VALUES (2, 'john')")

conn.commit()
conn.close()