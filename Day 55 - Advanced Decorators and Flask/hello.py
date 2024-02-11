from flask import Flask

app = Flask(__name__)


def make_bold(function):
    def wrapper(*args, **kwargs):
        html_text = function()
        return f"<b>{html_text}</b>"

    return wrapper


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


@app.route("/bye")
@make_bold
def say_bye():
    return "<p>Bye</p>"


@app.route("/username/<name>/<int:number>")
def greet(name, number):
    return f"<p>Hello {name}, you are {number} years old!</p>"


if __name__ == "__main__":
    # Run the app in debug mode to auto-reload
    app.run(debug=True)
