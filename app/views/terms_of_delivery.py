"""
Module for handling terms of delivery in the application.
"""
from config import app
from flask import render_template


@app.route('/terms_of_delivery/')
def terms_of_delivery():
    """
    Route for displaying the terms of delivery.

    :return:
    - Rendered template for the 'terms_of_delivery.html' page with the
    context variables.
    """

    context = {
        'title_page': 'Условия доставки'
    }
    return render_template('terms_of_delivery.html', **context)


if __name__ == '__main__':
    app.run()
