from flask import Flask, request, render_template, redirect

app = Flask(__name__)


@app.route("/", methods=['GET'])
def main():
    return render_template("example.html")


@app.route("/form_accepted")
def accepted():
    return "Форма принята"


@app.route("/", methods=['POST'])
def main_form_handler():
    form = request.form
    print(form)
    return redirect("/form_accepted")


if __name__ == "__main__":
    app.run()
