"""
This module is necessary to create a presentation
of the content and everything related to it.
"""
from config import app
from flask import render_template


@app.route('/contacts/')
def contacts():
    """
    Route for displaying contact information.

    :retur Response -> the rendered template for displaying
    contact information

    Description:
    This route is used to display contact information on the 'сontacts.html'
    template.
    """

    context = {
        'title_page': 'Контакты'
    }
    return render_template('сontacts.html', **context)


if __name__ == '__main__':
    app.run()
