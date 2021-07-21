from flask import Flask, render_template, request
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import DataRequired, Email, Length

app = Flask(__name__)
Bootstrap(app)

app.config['SECRET_KEY'] = "ngy3t5y30ge8rhqes4" #just hanging out here for study ref purposes.

class MyForm(FlaskForm):
    user_email = StringField(label='Email', validators=[DataRequired(), Email()])
    user_pass = PasswordField(label='Password', validators=[DataRequired(), Length(min=4, max=12)])
    submit = SubmitField(label='Log In')



@app.route("/")
def home():
    return render_template('index.html')

@app.route("/login", methods=["GET", "POST"])
def login():
    form = MyForm()
    if form.validate_on_submit():
        if form.user_email.data == "admin@email.com" and form.user_pass.data == "12345678":
            return render_template('success.html')
        else:
            return render_template('denied.html')
    return render_template('login.html', title="Login", form=form)


if __name__ == '__main__':
    app.run(debug=True)