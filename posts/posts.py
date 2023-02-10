from flask import Blueprint, render_template
from models import Product


posts = Blueprint("posts", __name__, template_folder='templates', static_folder='static')

@posts.route('/')
def home():
    product = Product.query.all()
    return render_template('posts/store.html', products=product)
