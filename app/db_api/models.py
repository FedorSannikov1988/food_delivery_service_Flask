from config import db, \
                   login_manager
from datetime import datetime
from flask_login import UserMixin
from werkzeug.security import check_password_hash, \
                              generate_password_hash


class CategoriesMeal(db.Model):

    __tablename__ = 'сategories_meal'

    category_meal_name = db.Column(db.String, primary_key=True)
    display_order_category = db.Column(db.Integer, unique=True, nullable=False)
    information_about_meals = db.relationship('Meal', backref='сategories_meal')

    def __repr__(self):
        return f'CategoriesMeal({self.category_meal_name})'


class Meal(db.Model):

    __tablename__ = 'meal'

    id = db.Column(db.Integer, primary_key=True)
    file_path_image = db.Column(db.String, nullable=True)
    title = db.Column(db.String, unique=True, nullable=False)
    category_meal_name = db.Column(db.String,
                                   db.ForeignKey('сategories_meal.category_meal_name'),
                                   nullable=False)
    description = db.Column(db.String, nullable=True)
    proteins = db.Column(db.Float, nullable=True)
    fats = db.Column(db.Float, nullable=True)
    carbohydrates = db.Column(db.Float, nullable=True)
    calories = db.Column(db.Float, nullable=True)
    weight = db.Column(db.String, nullable=False)
    cost = db.Column(db.Float, nullable=False)

    def __repr__(self):
        return f'Meal({self.title})'


@login_manager.user_loader
def load_user(user_id):
    return Users.query.get(user_id)


class Users(db.Model, UserMixin):
    def __init__(self,
                 name: str,
                 surname: str,
                 patronymic: str,
                 date_birth: datetime.date,
                 telephone: str,
                 email: str,
                 default_shipping_address: str):

        self.name = name
        self.surname = surname
        self.patronymic = patronymic
        self.date_birth = date_birth
        self.telephone = telephone
        self.email = email
        self.default_shipping_address = default_shipping_address

    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    path_photo = db.Column(db.String, nullable=True)
    name = db.Column(db.String(50), nullable=False)
    surname = db.Column(db.String(50), nullable=False)
    patronymic = db.Column(db.String(50), nullable=True)
    date_birth = db.Column(db.Date, nullable=False)
    telephone = db.Column(db.String(11), nullable=False)
    email = db.Column(db.String(50), unique=True, nullable=False)
    status = db.Column(db.Boolean, default=False)
    default_shipping_address = db.Column(db.String(1000), nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return f'Users({self.name}, {self.surname}, {self.email})'
