import os


class Configuration(object):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = "postgresql://postgres:11@localhost/electro_shop_flask"
    SECRET_KEY = os.urandom(25)