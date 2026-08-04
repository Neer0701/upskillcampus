import sqlite3

conn = sqlite3.connect("urls.db")

cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS urls(
id INTEGER PRIMARY KEY AUTOINCREMENT,
original TEXT NOT NULL,
short TEXT UNIQUE NOT NULL
)
""")

conn.commit()
conn.close()