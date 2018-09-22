import sqlite3

conn = sqlite3.connect(r'data.db')
cur = conn.cursor()
cur.execute('CREATE TABLE IF NOT EXISTS auth (username, salt, saltedhash,id);')
cur.execute('CREATE TABLE IF NOT EXISTS platformLogins (username, salted,id,platformID);')



cur.execute('INSERT INTO auth VALUES ("k","c","b", "123123")')
cur.execute('INSERT INTO platformLogins VALUES ("krish","chowdhary","123123","1")')



conn.commit()
conn.close()