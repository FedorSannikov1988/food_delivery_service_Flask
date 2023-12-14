import json
from config import app, \
                   logger
from flask import url_for, \
                  session, \
                  redirect
from datetime import datetime
from flask_login import current_user
from app.db_api import create_new_order


@app.route('/process_order/')
def process_order():

    if current_user.is_authenticated:

        if session.get('user_cart'):

            try:

                user_cart: dict = session.get('user_cart')

                session['user_cart'] = {}

                user_cart_json = json.dumps(user_cart)

                create_new_order(user_id=current_user.id,
                                 composition_order=user_cart_json,
                                 date_and_time_delivery=datetime.now())

            except Exception as error:
                logger.error(error)

        return redirect(url_for('personal_account'))

    else:
        return redirect(url_for('index'))


if __name__ == '__main__':
    app.run()
