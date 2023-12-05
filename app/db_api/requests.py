from sqlalchemy import asc
from datetime import datetime
from .models import db, \
                    Meal, \
                    Users, \
                    CategoriesMeal


def search_for_categories_meal_by_name(search_category_name: str) -> tuple:
    return CategoriesMeal.query.filter_by(category_meal_name=
                                          search_category_name).first()


def search_for_meal_by_title(search_title: str) -> tuple:
    return Meal.query.filter_by(title=search_title).first()


def get_all_categories_meal() -> tuple:
    return CategoriesMeal.query.filter_by().order_by(asc(CategoriesMeal.display_order_category)).all()


def add_user_in_database(name: str,
                         surname: str,
                         patronymic: str,
                         date_birth: datetime,
                         email: str,
                         default_shipping_address: str,
                         password: str) -> None:

    new_user = Users(name=name,
                     surname=surname,
                     patronymic=patronymic,
                     date_birth=date_birth,
                     email=email,
                     default_shipping_address=
                     default_shipping_address)

    new_user.set_password(password=password)
    db.session.add(new_user)
    db.session.commit()
