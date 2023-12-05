from config import db, \
                   app, \
                   logger
from .db_api import Meal, \
                    path_for_meal, \
                    CategoriesMeal, \
                    loading_fixtures,\
                    path_for_categories_meal, \
                    search_for_meal_by_title, \
                    search_for_categories_meal_by_name


@app.cli.command("init-db")
def init_db():
    db.create_all()
    print('db init')


@app.cli.command("add-categories_meal-in-db")
def add_categories_meal_in_db():

    all_categories_meal: dict = {}

    try:
        all_categories_meal = \
            loading_fixtures(path_for_file=path_for_categories_meal)

    except FileNotFoundError as file_with_data_not_found_error:
        logger.error(file_with_data_not_found_error)
        print('data file with food categories was not found')

    except Exception as all_error_data_downloads:
        logger.error(all_error_data_downloads)
        print('unknown error when loading data with food categories from file')

    for one_categories_meal in all_categories_meal:

        if not search_for_categories_meal_by_name(search_category_name=
                                                  one_categories_meal['category_meal_name']):

            new_meal = CategoriesMeal(category_meal_name=
                                      one_categories_meal['category_meal_name'],
                                      display_order_category=
                                      one_categories_meal['display_order_category'])
            db.session.add(new_meal)
        db.session.commit()

    if all_categories_meal:
        print('add categories meal in db completed')


@app.cli.command("add-meal-in-db")
def add_meal_in_db():

    all_meal: dict = {}

    try:
        all_meal = loading_fixtures(path_for_file=path_for_meal)

    except FileNotFoundError as file_with_data_not_found_error:
        logger.error(file_with_data_not_found_error)
        print('data file with all meal was not found')

    except Exception as all_error_data_downloads:
        logger.error(all_error_data_downloads)
        print('unknown error when loading data with meal from file')

    for one_meal in all_meal:

        if not search_for_meal_by_title(search_title=one_meal['title']):

            new_meal = Meal(title=one_meal['title'],
                            category_meal_name=one_meal['category_meal_name'],
                            file_path_image=one_meal.get('file_path_image'),
                            description=one_meal.get('description'),
                            proteins=one_meal.get('proteins'),
                            fats=one_meal.get('fats'),
                            carbohydrates=one_meal.get('carbohydrates'),
                            calories=one_meal.get('calories'),
                            weight=one_meal['weight'],
                            cost=one_meal['cost'])
            db.session.add(new_meal)
        db.session.commit()

    if all_meal:
        print('add meal in db completed')
