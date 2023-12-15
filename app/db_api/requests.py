"""
This module is responsible for all database queries.
"""
from .models import db, \
                    Meal, \
                    Users, \
                    Orders, \
                    CategoriesMeal
from sqlalchemy import asc
from typing import Optional
from datetime import datetime


def search_for_categories_meal_by_name(search_category_name: str) -> tuple:
    """
    Search for a category of meal by its name.

    :param search_category_name: str -> search_category_name: the name of the category to search for
    :return: tuple -> tuple containing the first category of meal found with the given name, or None if no category is found.
    """
    return CategoriesMeal.query.filter_by(category_meal_name=
                                          search_category_name).first()


def search_for_meal_by_title(search_title: str) -> tuple:
    """
    Search for a meal by its title.

    :param search_title: str -> search_title: the title of the meal to search for
    :return: tuple -> A tuple containing the first meal found with the given title, or None if no meal is found.
    """
    return Meal.query.filter_by(title=search_title).first()


def get_all_categories_meal() -> tuple:
    """
    Get all categories of meal.

    :return: tuple -> A tuple containing all categories of meal, ordered by their display order.
    """
    return CategoriesMeal.query.filter_by().order_by(asc(CategoriesMeal.display_order_category)).all()


def add_user_in_database(name: str,
                         surname: str,
                         patronymic: str,
                         date_birth: datetime.date,
                         telephone: str,
                         email: str,
                         default_shipping_address: str,
                         password: str) -> None:
    """
    Add a new user to the database.

    :param name: str -> the name of the user
    :param surname: str -> the surname of the user
    :param patronymic: str -> the patronymic of the user
    :param date_birth: datetime.date -> the date of birth of the user
    :param telephone: str -> the telephone number of the user
    :param email: str -> the email address of the user
    :param default_shipping_address: str -> the default shipping address of the user
    :param password: str -> the password of the user
    :return: None
    """

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
    """
    Search for a user account by email and activate it.

    :param email: str -> the email address of the user account to search for
    :return: None
    """

    user = Users.query.filter_by(email=email).first()

    if user:
        user.status = True
        db.session.commit()


def searching_user_account(email: str) -> Optional[Users]:
    """
    Search for a user account by email.

    :param email: str -> the email address of the user account to search for
    :return: Optional[Users] -> user account found with the given email, or None if no user account is found.
    """
    user = Users.query.filter_by(email=email).first()
    return user


def searching_user_account_and_setting_new_password(email: str,
                                                    password: str) -> None:
    """
    Search for a user account by email and set a new password for it.

    :param email: str -> the email address of the user account to search for
    :param password: str -> the new password to set for the user account
    :return: None
    """
    user = Users.query.filter_by(email=email).first()
    user.set_password(password=password)
    db.session.commit()


def add_user_photo(email: str,
                   new_path_photo: str) -> str:
    """
    Add a photo to a user account.

    :param email: str -> the email address of the user account
    :param new_path_photo: str -> the new path to the photo to add
    :return: str -> The old path to the photo that was replaced, or
    None if no photo was previously set.
    """
    user = Users.query.filter_by(email=email).first()

    path_photo_old: str = user.path_photo

    user.path_photo = new_path_photo
    db.session.commit()

    return path_photo_old


def delete_user_photo(email: str) -> None:
    """
    Delete the photo of a user account
    (deletes the name of the photo from the database).

    :param email: str -> email address of the user account
    :return: None
    """
    user = Users.query.filter_by(email=email).first()
    user.path_photo = None
    db.session.commit()


def change_personal_data(email: str,
                         name: str,
                         surname: str,
                         patronymic: str,
                         date_birth: datetime.date) -> None:
    """
    Change the personal data of a user account.

    :param email: str -> email address of the user account
    :param name: str -> new name of the user
    :param surname: str -> new surname of the user
    :param patronymic: str -> new patronymic of the user
    :param date_birth: datetime.date -> new date of birth of the user
    :return: None
    """

    user = Users.query.filter_by(email=email).first()
    user.name = name
    user.surname = surname
    user.patronymic = patronymic
    user.date_birth = date_birth
    db.session.commit()


def change_default_shipping_address(email: str,
                                    new_default_shipping_address: str) -> None:
    """
    Change the default shipping address of a user account.

    :param email: str -> email address of the user account
    :param new_default_shipping_address: str -> new default shipping address
    :return: None
    """

    user = Users.query.filter_by(email=email).first()

    user.default_shipping_address = new_default_shipping_address
    db.session.commit()


def change_password(email: str,
                    new_password: str) -> None:
    """
    Change the password of a user account.

    :param email: str -> email address of the user account
    :param new_password: str -> new password to set for the user account
    :return: None
    """
    user = Users.query.filter_by(email=email).first()

    user.set_password(password=new_password)
    db.session.commit()


def get_meal(id_meal: int) -> Optional[Meal]:
    """
    Get a meal by its ID.

    :param id_meal: int -> ID of the meal to get
    :return: Optional[Meal] -> The meal with the given ID, or None if no meal is found.
    """
    return Meal.query.get(id_meal)


def create_new_order(user_id: int,
                     composition_order: str,
                     date_and_time_delivery: datetime) -> None:
    """
    Create a new order.

    :param user_id: int -> ID of the user placing the order
    :param composition_order: str -> composition of the order
    :param date_and_time_delivery -> date and time of delivery for the order
    :return: None
    """
    new_order = Orders(user_id=user_id,
                       composition_order=composition_order,
                       date_and_time_delivery=date_and_time_delivery)

    db.session.add(new_order)
    db.session.commit()


def get_all_orders_user(user_id: int) -> Optional[list[Orders]]:
    """
    Get all orders placed by a user.

    :param user_id: int -> the ID of the user
    :return: Optional[list[Orders]] -> list of all orders placed by the user, or None if no orders are found.
    """
    return Orders.query.filter_by(user_id=user_id).all()
