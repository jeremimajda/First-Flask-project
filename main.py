from flask import Flask, render_template
import requests as re
import os

app = Flask(__name__)

response = re.get(url="https://api.npoint.io/2e86340e555309571422")
all_posts = response.json()

@app.route('/')
def get_all_posts():
    return render_template("index.html", posts=all_posts)


@app.route('/about')
def about():
    return render_template("about.html")


@app.route('/contact')
def contact():
    return render_template("contact.html")


@app.route('/post/<int:blog_id>')
def post(blog_id):
    return render_template("post.html", posts=all_posts, id=blog_id)


if __name__ == "__main__":
    app.run(debug=True)