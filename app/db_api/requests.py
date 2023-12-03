from .models import Meal, CategoriesMeal
from sqlalchemy import asc


def search_for_categories_meal_by_name(search_category_name: str) -> tuple:
    return CategoriesMeal.query.filter_by(category_meal_name=
                                          search_category_name).first()


def search_for_meal_by_title(search_title: str) -> tuple:
    return Meal.query.filter_by(title=search_title).first()


def get_all_categories_meal() -> tuple:
    return CategoriesMeal.query.filter_by().order_by(asc(CategoriesMeal.display_order_category)).all()
