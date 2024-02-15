from flask import Flask, render_template
import requests

blog_posts = requests.get(url="https://api.npoint.io/c790b4d5cab58020d391").json()


app = Flask(__name__)


@app.route('/')
def home():
    return render_template("index.html", all_posts=blog_posts)


@app.route('/post/<int:index>')
def get_post(index):
    requested_post = None
    for blog_post in blog_posts:
        if blog_post["id"] == index:
            requested_post = blog_post
    return render_template("post.html", post=requested_post)


@app.route('/guess/<name>')
def guess_game(name):
    age_url = f"https://api.agify.io/?name={name}"
    response_age = requests.get(url=age_url)
    age = response_age.json()["age"]
    gender_url = f"https://api.genderize.io/?name={name}"
    response_gender = requests.get(url=gender_url)
    gender = response_gender.json()["gender"]
    return render_template("guess_name.html", name=name, age=age, gender=gender)


if __name__ == "__main__":
    app.run(debug=True)

