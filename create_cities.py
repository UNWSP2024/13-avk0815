import sqlite3

conn = sqlite3.connect("cities.db")
cur = conn.cursor()

cur.execute("""
CREATE TABLE IF NOT EXISTS Cities (
    CityID INTEGER PRIMARY KEY,
    CityName TEXT,
    Population REAL
)
""")

cur.execute("INSERT INTO Cities (CityName, Population) VALUES ('Minneapolis', 429954)")
cur.execute("INSERT INTO Cities (CityName, Population) VALUES ('St Paul', 311527)")

conn.commit()
conn.close()

print("cities.db created.")