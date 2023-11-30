from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()


class Meal(db.Model):

    __tablename__ = 'meal'

    id = db.Column(db.Integer, primary_key=True)
    file_path_image = db.Column(db.String, nullable=True)
    title = db.Column(db.String, unique=True, nullable=False)
    category = db.Column(db.String, nullable=False)
    description = db.Column(db.String,  nullable=False)
    proteins = db.Column(db.Float, nullable=True)
    fats = db.Column(db.Float, nullable=True)
    carbohydrates = db.Column(db.Float, nullable=True)
    calories = db.Column(db.Float, nullable=True)
    weight = db.Column(db.String, nullable=False)
    cost = db.Column(db.Float, nullable=False)

    def __repr__(self):
        return f'Meal({self.title})'
