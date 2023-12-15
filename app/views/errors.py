"""
This module is necessary for error handling.
It contains all the implemented error handlers
for this application.
"""
from config import app, \
                   logger
from flask import render_template


@app.errorhandler(401)
def page_not_found(error):
    """
    Error handler for handling 401 Unauthorized errors.

    :param error: Exception -> the error object
    :return: Response -> the rendered template for displaying the
    401 error page

    When a 401 Unauthorized error occurs, this error handler will be
    invoked and display the appropriate error page.
    """
    logger.error(error)

    context = {
        'title_page': 'Ошибка 401'
    }
    return render_template('mistake_401.html', **context)


@app.errorhandler(404)
def page_not_found(error):
    """
    Error handler for handling 404 Not Found errors.

    :param error: Exception -> the error object
    :return: Response -> the rendered template for displaying
    the 404 error page.

    When a 404 Not Found error occurs, this error handler will
    be invoked and display the appropriate error page.
    """
    logger.error(error)

    context = {
        'title_page': 'Ошибка 404'
    }
    return render_template('mistake_404.html', **context)


@app.errorhandler(500)
def page_not_found(error):
    """
    Error handler for handling 500 Internal Server Error errors.

    :param error: Exception -> the error object
    :return: Response -> the rendered template for displaying the 500
    error page

    When a 500 Internal Server Error occurs, this error handler will
    be invoked and display the appropriate error page.
    """
    logger.error(error)

    context = {
        'title_page': 'Ошибка 500'
    }
    return render_template('mistake_404.html', **context)


if __name__ == '__main__':
    app.run()
