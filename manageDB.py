import sqlite3

conn = sqlite3.connect(r'data.db')
cur = conn.cursor()
cur.execute('CREATE TABLE IF NOT EXISTS auth (username, password,id);')

cur.execute('INSERT INTO auth VALUES ("k","c","123123")')
conn.commit()
conn.close()