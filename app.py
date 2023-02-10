from flask import Flask, url_for, Markup
from config import Configuration
from flask_sqlalchemy import SQLAlchemy
from flask_admin import Admin, form
from flask_admin.contrib.sqla import ModelView
import os
from flask_admin.contrib import sqla

app = Flask(__name__)
app.config.from_object(Configuration)

db = SQLAlchemy(app)

### Admin 
from models import Users, Category, Brand, Product, RatingStar, Rating, Reviews

admin = Admin(app)

### Images admin panel
file_path = os.path.abspath(os.path.dirname(__name__))

def generation_photo(model, file_data):
    hash_name = f'{model}'
    return hash_name


class StorageAdminModel(sqla.ModelView):
    """ Вывод изображений в админ панеле """
    def _list_thumbnail(view, context, model, name):
        if not model.photo:
            return ''

        url = url_for('static', filename=os.path.join('image/photo/', model.photo))
        if model.photo.split('.')[-1] in ['jpg', 'jpeg', 'png', 'svg', 'gif']:
            return Markup(f'<img src={url} width="100">')

    # передаю функцию _list_thumbnail в поле photo
    column_formatters = {
        'photo': _list_thumbnail
    }

    form_extra_fields = {
        # ImageUploadField Выполняет проверку изображений, создание эскизов, обновление и удаление изображений.
        "photo": form.ImageUploadField('',
                                            # Абсолютный путь к каталогу, в котором будут храниться файлы
                                            base_path=
                                            os.path.join(file_path, 'static/image/photo/'),
                                            # Относительный путь из каталога. Будет добавляться к имени загружаемого файла.
                                            url_relative_path='image/photo/',
                                            namegen=generation_photo,
                                            # Список разрешенных расширений. Если не указано, то будут разрешены форматы gif, jpg, jpeg, png и tiff.
                                            allowed_extensions=['png', 'jpg', 'jpeg', 'svg', 'gif'],
                                        )}
    


    def create_form(self, obj=None):
        return super(StorageAdminModel, self).create_form(obj)

    def edit_form(self, obj=None):
        return super(StorageAdminModel, self).edit_form(obj)

### Admin list
admin.add_view(StorageAdminModel(Product, db.session))
admin.add_view(ModelView(Users, db.session))
admin.add_view(ModelView(Category, db.session))
admin.add_view(ModelView(Brand, db.session))
admin.add_view(ModelView(RatingStar, db.session))
admin.add_view(ModelView(Rating, db.session))
admin.add_view(ModelView(Reviews, db.session))