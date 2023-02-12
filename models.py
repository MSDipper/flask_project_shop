from app import db, app
from datetime import datetime
from flask_image_alchemy.fields import StdImageField


class Users(db.Model):
    """ Пользователи """
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(150), nullable=False)
    password = db.Column(db.String(100), nullable=False)
    time = db.Column(db.DateTime, default=datetime.utcnow)
    users = db.relationship('Product', backref='users', lazy=True)
    
    def __repr__(self):
        return self.name


class Category(db.Model):
    """ Категории """
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    slug = db.Column(db.String(100), unique=True, nullable=False)
    categories = db.relationship('Product', backref='category', lazy=True)
    
        
    def __repr__(self):
        return self.name


class Brand(db.Model):
    """ Бренд """
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150), nullable=False)
    slug = db.Column(db.String(150), unique=True, nullable=False)
    brands = db.relationship('Product', backref='brands', lazy=True)
    
        
    def __repr__(self):
        return self.name 


class Product(db.Model):
    """ Товар """
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(150), nullable=False)
    slug = db.Column(db.String(150), unique=True, nullable=False)
    photo = db.Column(db.String(150), unique=True, nullable=False)
    price = db.Column(db.Numeric, nullable=False)
    old_price = db.Column(db.Numeric, nullable=True)
    sale = db.Column(db.Numeric, nullable=False)
    size = db.Column(db.Integer, nullable=True)
    color = db.Column(db.String(100), nullable=True)
    freshness = db.Column(db.String(100), nullable=True)
    stock = db.Column(db.Boolean, default=True)
    create_at = db.Column(db.DateTime, default=datetime.utcnow)
    description = db.Column(db.Text, nullable=True)
    details = db.Column(db.Text, nullable=True)
    publish = db.Column(db.Boolean, default=True)
    reviews = db.relationship('Reviews', backref='product', lazy=True)
    ratings = db.relationship('Rating', backref='product', lazy=True)
    category_id = db.Column(db.Integer, db.ForeignKey('category.id'),
        nullable=False)
    brand_id = db.Column(db.Integer, db.ForeignKey('brand.id'),
        nullable=False)
    users_id = db.Column(db.Integer, db.ForeignKey('users.id'),
        nullable=False)
    
    def __repr__(self):
        return f"{self.title}"
    
    


class RatingStar(db.Model):
    """ Звезды рейтинга """
    id = db.Column(db.Integer, primary_key=True)
    value = db.Column(db.Integer, default=0)


    def __repr__(self):
        return f"{self.value}"
    

class Rating(db.Model):
    """ Рейтинг """
    id = db.Column(db.Integer, primary_key=True)
    star = db.Column(db.String(50), nullable=False)
    product_id = db.Column(db.Integer, db.ForeignKey('product.id'),
        nullable=False)
    
    
    def __repr__(self):
        return f"{self.star}"
    

class Reviews(db.Model):
    """ Отзывы """
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), nullable=False)
    name = db.Column(db.String(100), nullable=False)
    message = db.Column(db.Text, nullable=False)
    product_id = db.Column(db.Integer, db.ForeignKey('product.id'),
        nullable=False)
    
    
    def __repr__(self):
        return f"{self.name} - {self.email}"
