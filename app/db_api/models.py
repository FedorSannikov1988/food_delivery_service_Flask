from flask_login import UserMixin
from config import db, login_manager
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
    description = db.Column(db.String,  nullable=True)
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
    #return db.session.query(User).get(user_id)
    return Users.query.get(user_id)


class Users(db.Model, UserMixin):

    __tablename__ = 'users'

    #id_user = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    surname = db.Column(db.String(50), nullable=False)
    patronymic = db.Column(db.String(50), nullable=True)
    date_birth = db.Column(db.Date, nullable=False)
    #email = db.Column(db.String(50), unique=True, nullable=False)
    email = db.Column(db.String(50), primary_key=True)
    default_shipping_address = db.Column(db.String(1000), nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return f'Users({self.name}, {self.surname}, {self.email})'
