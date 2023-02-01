from app import app, db
import view
from shop.blueprint import shop


app.register_blueprint(shop, url_prefix='/blog')


if __name__ == "__main__":
    app.run()