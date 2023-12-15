"""
Module for creating an index view and everything related to it.
"""
from config import app
from flask import render_template
from app.db_api import get_all_categories_meal


@app.route('/')
def index():
    """
    Route for the main page of the delivery service menu.

    :return: Response -> the rendered template for the main page
    """

    context = {
        'title_page': 'Главная страница - Меню службы доставки',
        'all_categories_meal': get_all_categories_meal()
    }
    return render_template('index.html', **context)


if __name__ == '__main__':
    app.run()
