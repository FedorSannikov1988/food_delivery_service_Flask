from .models import Meal


def search_for_meal_by_title(search_title: str) -> tuple:
    return Meal.query.filter_by(title=search_title).first()
