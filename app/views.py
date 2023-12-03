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


if __name__ == '__main__':
    app.run()
