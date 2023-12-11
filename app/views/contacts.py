from config import app
from flask import render_template


@app.route('/contacts/')
def contacts():

    context = {
        'title_page': 'Контакты'
    }
    return render_template('сontacts.html', **context)


if __name__ == '__main__':
    app.run()
