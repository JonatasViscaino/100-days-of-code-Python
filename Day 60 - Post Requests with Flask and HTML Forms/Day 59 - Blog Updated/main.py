from flask import Flask, render_template, request
import smtplib
import requests

# constants
EMAIL = "jonatasmviscaino@gmail.com"
PASS_GMAIL = "XXXX"
app = Flask(__name__)

# Posts for website
posts = requests.get("https://api.npoint.io/f8195dbeee49bffeeffa").json()


# Home Route
@app.route('/')
def get_all_posts():
    return render_template("index.html", posts=posts)

# About Route
@app.route("/about")
def about():
    return render_template("about.html")


# Contact Route and Form Contact
@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        data = request.form
        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(user=EMAIL, password=PASS_GMAIL)
            connection.sendmail(
                from_addr=EMAIL,
                to_addrs=EMAIL,
                msg=f"Subject:Contact from Website!\n\n"
                    f"Name: {data["name"]}\n"
                    f"Email: {data["email"]}\n"
                    f"Phone: {data["phone"]}\n"
                    f"Message: {data["message"]}\n"
            )
        print(data["name"])
        print(data["email"])
        print(data["phone"])
        print(data["message"])
        return render_template("contact.html", msg_sent=True)
    return render_template("contact.html", msg_sent=False)


# Blog Route
@app.route("/post/<int:index>")
def show_post(index):
    requested_post = None
    for blog_post in posts:
        if blog_post["id"] == index:
            requested_post = blog_post
    return render_template("post.html", post=requested_post)


if __name__ == "__main__":
    app.run(debug=True, port=5001)
