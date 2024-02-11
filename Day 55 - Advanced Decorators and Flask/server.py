from flask import Flask
import random

random_number = random.randint(0, 9)
print(random_number)

app = Flask(__name__)


@app.route("/")
def initial_page():
    global random_number
    random_number = random.randint(0, 9)
    print(random_number)
    return ("<h1>Guess a number between 0 and 9:</h1>"
            "<img src='https://i.giphy.com/3o7aCSPqXE5C6T8tBC.webp' width='480' height='480' frameBorder='0'/>")


@app.route("/<int:number>")
def guess_the_number(number):
    if random_number == number:
        return ("<h1 style='color: green;'>You found me</h1>"
                "<img src='https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif'/>")
    elif number > random_number:
        return ("<h1 style='color: blue;'>Too high, try again!</h1>"
                "<img src='https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif'/>")
    else:
        return ("<h1 style='color: red;'>Too low, try again!</h1>"
                "<img src='https://media4.giphy.com/media/v1.Y2lkPTc5MGI3NjExYmx5eDN1bm9rdXNtbzdxNTRzdHdoank4a2U2cnVmazU4d3RjeThjeCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/L5WQjD4p8IpO0/giphy.gif'/>")


if __name__ == "__main__":
    # Run the app in debug mode to auto-reload
    app.run(debug=True)
