from config import app
from flask import render_template
from app.db_api import get_all_categories_meal


@app.route('/')
def index():

    context = {
        'title_page': 'Главная страница',
        'all_categories_meal': get_all_categories_meal()
    }
    return render_template('index.html', **context)


if __name__ == '__main__':
    app.run()
