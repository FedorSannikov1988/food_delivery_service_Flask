"""
Database models for the application
"""
from config import db, \
                   login_manager
from datetime import datetime
from flask_login import UserMixin
from werkzeug.security import check_password_hash, \
                              generate_password_hash


class CategoriesMeal(db.Model):
    """
    Model for the food category.

    Attributes:
    - category_meal_name:  unique category that food belongs to
    - display_order_category: the order in which categories are displayed on the main page
    (it is necessary in order to put the "hot positions" in the first place, if necessary)
    - information_about_meals: link to the food table
    """

    __tablename__ = 'сategories_meal'

    category_meal_name = db.Column(db.String, primary_key=True)
    display_order_category = db.Column(db.Integer, unique=True, nullable=False)
    information_about_meals = db.relationship('Meal', backref='сategories_meal')

    def __repr__(self):
        return f'CategoriesMeal({self.category_meal_name})'


class Meal(db.Model):
    """
    A model for representing dishes in a database.

    Attributes:
    - id: the unique identifier of the dish
    - file_path_image: path to the image of the dish
    - title: name of the dish (unique)
    - category_meal_name: name of the category to which the dish belongs
    - description: description of the dish
    - proteins: the protein content of the dish
    - fats: the fat content of the dish
    - carbohydrates: the carbohydrate content of the dish
    - calories: the number of calories in a dish
    - weight: the weight of the dish
    - cost: the cost of the dish
    """

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
    """
    A function to load a user from the database.

    Parameters:
    - user_id: the unique identifier of the user

    Returns:
    - The user object with the specified user_id.
    """
    return Users.query.get(user_id)


class Users(db.Model, UserMixin):
    """
    A model for representing users in a database.

    Attributes:
    - id: the unique identifier of the user
    - path_photo: path to the user's photo
    - name: the user's name
    - surname: the user's surname
    - patronymic: the user's patronymic (optional)
    - date_birth: the user's date of birth
    - telephone: the user's telephone number
    - email: the user's email address (unique)
    - status: the user's status (account activated
    (email address confirmed or not))
    - default_shipping_address: the user's default shipping address
    - password_hash: the hashed password of the user
    - user_orders: the orders associated with the user
    """

    __tablename__ = 'users'

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
    user_orders = db.relationship('Orders', backref='users')

    def set_password(self, password: str) -> None:
        """
        Set the password for the user.

        :param password: the password to be set
        """
        self.password_hash = generate_password_hash(password)

    def check_password(self, password: str):
        """
        Check if the provided password matches the user's password.

        :param password: the password to be checked.
        :return: True if the password matches, False otherwise.
        """
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return f'Users({self.name}, {self.surname}, {self.email})'


class Orders(db.Model):
    """
    A model for representing orders in a database.

    Attributes:
    - id: the unique identifier of the order
    - user_id: the ID of the user who placed the order
    - composition_order: the composition of the order
    - date_and_time_order_creation: the date and time when the order was created
    - date_and_time_delivery: the date and time when the order will be delivered
    - payment_status: the status of payment for the order
    - delivery_status: the status of delivery for the order
    """

    __tablename__ = 'orders'

    def __init__(self,
                 user_id: int,
                 composition_order: str,
                 date_and_time_delivery: datetime):

        self.user_id = user_id
        self.composition_order = composition_order
        self.date_and_time_delivery = date_and_time_delivery

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    composition_order = db.Column(db.String, nullable=False)
    date_and_time_order_creation = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    date_and_time_delivery = db.Column(db.DateTime, nullable=False)
    payment_status = db.Column(db.Boolean, nullable=False, default=False)
    delivery_status = db.Column(db.Boolean, nullable=False, default=False)

    def __repr__(self):
        return f'Orders({self.id}, {self.date_and_time_order_creation})'
