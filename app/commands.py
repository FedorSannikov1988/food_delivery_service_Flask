from .db_api import db, Meal, path_for_meal, loading_fixtures, search_for_meal_by_title
from config import app, logger


@app.cli.command("init-db")
def init_db():
    db.create_all()
    print('db init')


@app.cli.command("add-meal-in-db")
def add_meal_in_db():

    all_meal: dict = {}

    try:
        all_meal = loading_fixtures(path_for_file=path_for_meal)

    except FileNotFoundError as file_with_data_not_found_error:
        logger.error(file_with_data_not_found_error)
        print('data file was not found')

    except Exception as all_error_data_downloads:
        logger.error(all_error_data_downloads)
        print('unknown error when loading data from a file')

    for one_meal in all_meal:

        if not search_for_meal_by_title(search_title=one_meal['title']):

            new_meal = Meal(title=one_meal['title'],
                            category=one_meal['category'],
                            file_path_image=one_meal['file_path_image'],
                            description=one_meal['description'],
                            proteins=one_meal['proteins'],
                            fats=one_meal['fats'],
                            carbohydrates=one_meal['carbohydrates'],
                            calories=one_meal['calories'],
                            weight=one_meal['weight'],
                            cost=one_meal['cost'])
            db.session.add(new_meal)
        db.session.commit()

    if all_meal:
        print('add meal in db completed')
