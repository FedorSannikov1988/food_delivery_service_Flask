from flask import send_from_directory, \
                  render_template
from .db_api import Meal
from config import app


@app.route('/media/<path:filename>')
def media(filename):
    return send_from_directory('media', filename)


@app.route('/')
def index():

    meal = Meal.query.all()

    context = {
        'title_pag': 'Главная страница',
        'meal': meal
    }
    return render_template('index.html', **context)


if __name__ == '__main__':
    app.run()
