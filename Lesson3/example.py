from sqlite3 import connect

db = connect("../Lesson4/test.db")
cur = db.cursor()
a = cur.execute("SELECT * FROM items").fetchall()
print(a)
