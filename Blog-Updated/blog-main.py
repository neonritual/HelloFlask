from flask import Flask, render_template
import requests

app = Flask(__name__)

blog_url = "https://api.npoint.io/52e2bb22204d12fb4116"

@app.route("/")
def clean_blog():
    all_blogs = requests.get(blog_url).json()
    return render_template("index.html", posts=all_blogs)

@app.route("/about")
def about_me():
    return render_template("about.html")

@app.route("/contact")
def contact_me():
    return render_template("contact.html")

@app.route('/blog/<int:blog_num>')
def get_post(blog_num):
    all_blogs = requests.get(blog_url).json()
    requested_post = []
    for post in all_blogs:
        if post["id"] == blog_num:
            requested_post = post
    return render_template("post.html", post=requested_post, num=blog_num)


if __name__ == "__main__":
    app.run(debug=True)
