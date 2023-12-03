from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()


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
    category_meal_name = db.Column(db.String, db.ForeignKey('сategories_meal.category_meal_name'), nullable=False)
    description = db.Column(db.String,  nullable=True)
    proteins = db.Column(db.Float, nullable=True)
    fats = db.Column(db.Float, nullable=True)
    carbohydrates = db.Column(db.Float, nullable=True)
    calories = db.Column(db.Float, nullable=True)
    weight = db.Column(db.String, nullable=False)
    cost = db.Column(db.Float, nullable=False)

    def __repr__(self):
        return f'Meal({self.title})'
