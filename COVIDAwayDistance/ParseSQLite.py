import sqlite3

conn = sqlite3.connect('../db.sqlite3')
cur = conn.cursor()

rows = cur.fetchall()
print(rows)
