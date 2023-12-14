from config import app, logger
from flask import render_template


@app.errorhandler(401)
def page_not_found(error):

    logger.error(error)

    context = {
        'title_page': 'Ошибка 401'
    }
    return render_template('mistake_401.html', **context)


@app.errorhandler(404)
def page_not_found(error):

    logger.error(error)

    context = {
        'title_page': 'Ошибка 404'
    }
    return render_template('mistake_404.html', **context)


@app.errorhandler(500)
def page_not_found(error):

    logger.error(error)

    context = {
        'title_page': 'Ошибка 500'
    }
    return render_template('mistake_404.html', **context)


if __name__ == '__main__':
    app.run()
