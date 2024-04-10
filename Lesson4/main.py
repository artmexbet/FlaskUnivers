from flask import Flask, render_template, request, redirect
import sqlite3

app = Flask(__name__)


@app.route('/add_item')
def main():
    return render_template("add_item.html")


@app.route('/add_item', methods=['POST'])
def post_main():
    form = request.form
    db = sqlite3.connect('test.db')
    cur = db.cursor()
    cur.execute(f"""INSERT INTO items (title, price) 
    VALUES (?, ?)""", (form["title"], int(form["price"])))
    db.commit()
    return redirect("/add_item")


@app.route("/add_order")
def add_order():
    db = sqlite3.connect('test.db')
    cur = db.cursor()
    d = cur.execute("SELECT * FROM items").fetchall()
    return render_template("add_order.html", data=d)


app.run()
