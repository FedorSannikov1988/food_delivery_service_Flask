from config import app
from flask import render_template


@app.errorhandler(401)
def page_not_found(error):
    print(error)
    context = {
        'title_page': 'Ошибка 401'
    }
    return render_template('mistake_401.html', **context)


@app.errorhandler(404)
def page_not_found(error):
    print(error)
    context = {
        'title_page': 'Ошибка 404'
    }
    return render_template('mistake_404.html', **context)


if __name__ == '__main__':
    app.run()
