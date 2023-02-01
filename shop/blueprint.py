from flask import Blueprint, render_template


shop = Blueprint("shop", __name__, template_folder='templates', static_folder='static')

@shop.route('/')
def home():
    return render_template('shop/store.html')
