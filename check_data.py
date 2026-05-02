import sqlite3
import pandas as pd

conn = sqlite3.connect("data/jobs.db")

df = pd.read_sql("SELECT * FROM jobs LIMIT 5", conn)

print(df)

conn.close()