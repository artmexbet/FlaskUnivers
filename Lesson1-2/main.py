from flask import Flask, request

app = Flask(__name__)
orders = {"id": "информация"}


@app.route("/")
@app.route("/main")
def main():
    return "asnfoiamskf"


@app.route("/hello", methods=["POST"])
def hello_func():
    print(request.data)
    data = request.json
    print(data["name"])
    return f"""<h1>Привет, {data["name"]}!</h1>"""


@app.route("/orders/<ident>", methods=["DELETE"])
def delete_order(ident):
    pass


if __name__ == "__main__":
    app.run()
