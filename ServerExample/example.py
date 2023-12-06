from flask import Flask, request, redirect
from flask_cors import CORS
from datetime import datetime

app = Flask(__name__)
CORS(app)

orders_list = {}
ORDER_REQUIRED_FIELDS = ["items", "address"]
items_list = ["Пепперони", "Тоскана"]


@app.route("/")
def main_route():
    routes = list(app.url_map.iter_rules())
    return {"routes": [f"{i}, methods: {i.methods}" for i in routes]}


@app.route("/orders")
def get_orders_list():
    return orders_list


@app.route("/orders", methods=["POST"])
def add_order():
    data = request.json
    if not all(field in data for field in ORDER_REQUIRED_FIELDS):
        return {"status": f"Not added. Fields {ORDER_REQUIRED_FIELDS} must be in request"}, 400
    if not all(item in items_list for item in data["items"]):
        return {"status": f"Not added. In the items are things that doesn't exist in this shop"}, 400
    orders_list[str(datetime.now())] = data
    return redirect("/orders")


@app.route("/items")
def get_items():
    return {"items_list": items_list}


@app.route("/items", methods=["POST"])
def add_item():
    data = request.json
    if "items" not in data:
        return {"status": "Items field must be in the request"}, 400
    items_list.extend(data["items"])
    return redirect("/items")


@app.route("/orders/<ident>")
def get_order(ident):
    order = orders_list.get(ident, None)
    if order is None:
        return {"status": "Not found"}, 404
    return {"order_info": order}


@app.route("/orders/<ident>", methods=["DELETE"])
def delete_order(ident):
    if ident not in orders_list:
        return {"status": "Not found"}, 404
    del orders_list[ident]
    return redirect("/orders")


@app.route("/items/<item>", methods=["DELETE"])
def delete_item(item):
    if item not in items_list:
        return {"status": "Not found"}, 404
    items_list.remove(item)
    return redirect("/items")


if __name__ == "__main__":
    app.run()
