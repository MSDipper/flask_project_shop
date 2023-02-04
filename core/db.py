from app import app
from flask_sqlalchemy import SQLAlchemy


app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres:11@localhost/electro_shop_flask"
db = SQLAlchemy(app)