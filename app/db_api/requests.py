from .models import db, \
                    Meal, \
                    Users, \
                    CategoriesMeal
from sqlalchemy import asc
from typing import Optional
from datetime import datetime


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
                         date_birth: datetime.date,
                         telephone: str,
                         email: str,
                         default_shipping_address: str,
                         password: str) -> None:
    new_user = Users(name=name,
                     surname=surname,
                     patronymic=patronymic,
                     date_birth=date_birth,
                     telephone=telephone,
                     email=email,
                     default_shipping_address=
                     default_shipping_address)

    new_user.set_password(password=
                          password)

    db.session.add(new_user)
    db.session.commit()


def searching_and_activating_user_account(email: str) -> None:
    user = Users.query.filter_by(email=email).first()

    if user:
        user.status = True
        db.session.commit()


def searching_user_account(email: str) -> Optional[Users]:
    user = Users.query.filter_by(email=email).first()
    return user


def searching_user_account_and_setting_new_password(email: str,
                                                    password: str) -> None:
    user = Users.query.filter_by(email=email).first()
    user.set_password(password=password)
    db.session.commit()


def add_user_photo(email: str,
                   new_path_photo: str) -> str:
    user = Users.query.filter_by(email=email).first()

    path_photo_old: str = user.path_photo

    user.path_photo = new_path_photo
    db.session.commit()

    return path_photo_old


def delete_user_photo(email: str) -> None:
    user = Users.query.filter_by(email=email).first()
    user.path_photo = None
    db.session.commit()


def change_personal_data(email: str,
                         name: str,
                         surname: str,
                         patronymic: str,
                         date_birth: datetime.date) -> None:

    user = Users.query.filter_by(email=email).first()
    user.name = name
    user.surname = surname
    user.patronymic = patronymic
    user.date_birth = date_birth
    db.session.commit()


def change_default_shipping_address(email: str,
                                    new_default_shipping_address: str) -> None:
    user = Users.query.filter_by(email=email).first()

    user.default_shipping_address = new_default_shipping_address
    db.session.commit()


def change_password(email: str,
                    new_password: str) -> None:
    user = Users.query.filter_by(email=email).first()

    user.set_password(password=new_password)
    db.session.commit()


def get_meal(id_meal: int) -> Optional[Meal]:
    return Meal.query.get(id_meal)
