from config import app
from flask import render_template, \
                  send_from_directory
from .db_api import get_all_categories_meal


@app.route('/media/<path:filename>')
def media(filename):
    return send_from_directory('media', filename)


@app.route('/')
def index():

    context = {
        'title_pag': 'Главная страница',
        'all_categories_meal': get_all_categories_meal()
    }
    return render_template('index.html', **context)


@app.route('/terms_of_delivery/')
def terms_of_delivery():

    context = {
        'title_pag': 'Условия доставки'
    }
    return render_template('terms_of_delivery.html', **context)


@app.route('/contacts/')
def contacts():

    context = {
        'title_pag': 'Контакты'
    }
    return render_template('сontacts.html', **context)


if __name__ == '__main__':
    app.run()
