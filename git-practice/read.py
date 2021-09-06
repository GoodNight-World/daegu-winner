import sqlite3

conn = sqlite3.connect('topics.db')
result = conn.execute('SELECT * FROM topic')
rows = result.fetchall()
for row in rows:
    print(row)