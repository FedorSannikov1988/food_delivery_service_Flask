from config import app
from flask import render_template


@app.route('/terms_of_delivery/')
def terms_of_delivery():

    context = {
        'title_pag': 'Условия доставки'
    }
    return render_template('terms_of_delivery.html', **context)


if __name__ == '__main__':
    app.run()
