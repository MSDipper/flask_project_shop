from flask import Blueprint, render_template
from models import Product, Category
from app import db


posts = Blueprint("posts", __name__, template_folder='templates', static_folder='static')

@posts.route('/')
def home():
    product = db.session.query(Product, Category).join(Category).all()
    return render_template('posts/store.html', products=product)
