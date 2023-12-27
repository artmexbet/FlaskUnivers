from sqlite3 import connect

db = connect("test.db")
cur = db.cursor()
a = cur.execute("SELECT * FROM items").fetchall()
print(a)
