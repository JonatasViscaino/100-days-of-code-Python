from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import EmailField, PasswordField, SubmitField
from wtforms import validators
from flask_bootstrap import Bootstrap5


# Creating Form Class
class MyForm(FlaskForm):
    email = EmailField(label='Email:', validators=[validators.Email()])
    password = PasswordField(label='Password:', validators=[validators.Length(min=8), validators.InputRequired()])
    submit = SubmitField(label='Log In')


app = Flask(__name__)
app.secret_key = 'mysecret'
bootstrap = Bootstrap5(app)


@app.route("/")
def home():
    return render_template('index.html')


@app.route("/login", methods=["GET", "POST"])
def login():
    form = MyForm()
    if form.validate_on_submit():
        if form.email.data == "admin@email.com" and form.password.data == "12345678":
            return render_template('success.html')
        else:
            return render_template('denied.html')
    return render_template('login.html', form=form)


if __name__ == '__main__':
    app.run(debug=True)
