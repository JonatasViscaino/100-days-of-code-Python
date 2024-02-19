from flask import Flask, render_template, request, url_for

app = Flask(__name__)


@app.route("/")
def homepage():
    return render_template("index.html")


@app.route("/login", methods=["POST"])
def receive_data():
    name = None
    password = None
    if request.method == "POST":
        name = request.form["name"]
        password = request.form["password"]
        print(name)
        print(password)
    return render_template("response.html", name=name, password=password)


if __name__ == "__main__":
    app.run(debug=True)