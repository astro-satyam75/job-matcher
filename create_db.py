import sqlite3

conn = sqlite3.connect("data/jobs.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS jobs (
    id INTEGER PRIMARY KEY,
    title TEXT,
    company TEXT,
    location TEXT,
    description TEXT
)
""")

conn.commit()
conn.close()

print("Database created")