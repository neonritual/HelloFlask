from flask import Flask, render_template
import random
import datetime
import requests

app = Flask(__name__)

@app.route('/')
def home():
    random_number = random.randint(1, 100)
    year = datetime.date.today().year
    return render_template("/index.html", randnum=random_number, current_year=year)

@app.route('/<username>/')
def name_stats(username):
    gender_response = requests.get(f"https://api.genderize.io?name={username}").json()
    gender = gender_response["gender"]

    age_response = requests.get(f"https://api.agify.io?name={username}").json()
    age = age_response["age"]

    return render_template("/name.html", user_name=username, user_gender=gender, user_age=age)

@app.route('/blog')
def get_blog():
    blog_url = "https://api.npoint.io/ed99320662742443cc5b"
    all_blogs = requests.get(blog_url).json()
    return render_template("blog.html", posts=all_blogs)


if __name__ == "__main__":
    app.run(debug=True)