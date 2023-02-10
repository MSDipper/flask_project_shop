from flask import Blueprint, render_template


posts = Blueprint("posts", __name__, template_folder='templates', static_folder='static')

@posts.route('/')
def home():
    return render_template('posts/store.html')
