import duckdb

conn= duckdb.connect('testdb.db')

cur= conn.cursor()

cur.execute("CREATE TABLE IF NOT EXISTS food (id INT, name TEXT);")
cur.execute("INSERT INTO food (id, name) VALUES (1, 'Apple');")

conn.commit()

cur.close()
conn.close()