import sqlite3

conn = sqlite3.connect("phonebook.db")
cur = conn.cursor()

cur.execute("""
CREATE TABLE IF NOT EXISTS Entries (
    Name TEXT,
    Phone TEXT
)
""")

conn.commit()
conn.close()

print("phonebook.db created.")