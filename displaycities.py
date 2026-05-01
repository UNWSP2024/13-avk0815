import sqlite3

conn = sqlite3.connect("cities.db")
cur = conn.cursor()

cur.execute("SELECT * FROM Cities")

for row in cur.fetchall():
    print(row)

conn.close()