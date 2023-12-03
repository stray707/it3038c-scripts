# A heavily modified version of Lab 12's Flask site. I didn't want to use a form for a blog, so instead I utilized POST-ing instead.

from flask import Flask, render_template, request, redirect, url_for
from blog_container import BlogContainer, Blogpost
import datetime

app = Flask(__name__)
app.config.from_object(__name__)

blog_container = BlogContainer('postlist.json')  # Initializes BlogContainer and stored post list

@app.route('/')
def hello():
    return render_template("home.html")

@app.route('/blog')
def blog():
    return render_template("blog.html", posts=blog_container.posts)  # Use correct attribute name

@app.route('/education')
def education():
    return render_template("education.html")

@app.route('/projects')
def projects():
    return render_template("projects.html")

@app.route('/archives')
def archives():
    return render_template("archives.html")

# Handler of newpost.py. Activated by POST, reads the payload, and adds a new post.
@app.route('/create_post', methods=['POST'])
def create_post():
    title = request.form['title']
    text_content = request.form['text_content']

    # Blog_container.py doesn't need to ask the user what time it is, it can just pull from the user's machine.
    current_date = datetime.datetime.now().strftime("%B %d, %Y %H:%M")

    # Create a post instance
    new_post = Blogpost(title, current_date, text_content)

    # Used by blog_container.py
    blog_container.add_post(new_post)
    return redirect(url_for('blog'))
