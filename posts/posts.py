from flask import Blueprint, render_template, request
from models import Product, Category
from app import db
from flask_paginate import Pagination


posts = Blueprint("posts", __name__, template_folder='templates', static_folder='static')

ROWS_PER_PAGE = 3

@posts.route('/')
def home():
    page = request.args.get('page', 1, type= int ) 
    product = db.session.query(Product, Category).join(Category).paginate(page=page, per_page=ROWS_PER_PAGE)
    return render_template('posts/store.html', products=product)