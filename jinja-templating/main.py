from flask import Flask, render_template
import requests



app = Flask(__name__)

@app.route('/')
def home():
    blog_url = "https://api.npoint.io/ed99320662742443cc5b"
    all_blogs = requests.get(blog_url).json()
    return render_template("index.html", posts=all_blogs)

@app.route('/blog/<int:blog_num>')
def get_post(blog_num):
    blog_url = "https://api.npoint.io/ed99320662742443cc5b"
    all_blogs = requests.get(blog_url).json()
    requested_post = []
    for post in all_blogs:
        if post["id"] == blog_num:
            requested_post = post
    return render_template("post.html", post=post)

if __name__ == "__main__":
    app.run(debug=True)
