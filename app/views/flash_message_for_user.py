"""
Module for notifying the user via flash.
"""

from config import app
from flask import render_template


@app.route('/flash_message_for_user/')
def flash_message_for_user():
    """
    Route for displaying a flash message to the user.

    :return: Response -> the rendered template for displaying the
    flash message
    """

    context = {
        'title_page': 'Оповещение пользователя'
    }
    return render_template('flash_message_for_user.html', **context)


if __name__ == '__main__':
    app.run()
