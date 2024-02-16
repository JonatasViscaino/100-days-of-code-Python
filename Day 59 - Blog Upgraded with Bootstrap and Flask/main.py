from flask import Flask, render_template, url_for
import requests

app = Flask(__name__)

blog_posts = requests.get("https://api.npoint.io/f8195dbeee49bffeeffa").json()
print(blog_posts[0]["image_url"])

@app.route("/")
def home():
    return render_template("index.html", posts=blog_posts)


@app.route("/about")
def get_about():
    return render_template("about.html")


@app.route("/contact")
def get_contact():
    return render_template("contact.html")


@app.route("/post/<int:index>")
def get_post(index):
    requested_post = None
    for blog_post in blog_posts:
        if blog_post["id"] == index:
            requested_post = blog_post
    return render_template("post.html", post=requested_post)


if __name__ == "__main__":
    app.run(debug=True)


