from config import app
from flask import render_template


@app.route('/flash_message_for_user/')
def flash_message_for_user():

    context = {
        'title_page': 'Оповещение пользователя'
    }
    return render_template('flash_message_for_user.html', **context)


if __name__ == '__main__':
    app.run()
