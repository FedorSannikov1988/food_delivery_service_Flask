from config import app
from flask import url_for, \
                  session, \
                  redirect
from flask_login import current_user


@app.route('/shopping_cart_user/')
def shopping_cart_user():

    if current_user.is_authenticated:
        print('зашол в корзину покупок')
        return redirect(url_for('index'))
    else:
        return redirect(url_for('log_in_account'))


@app.context_processor
def inject_number_products_in_user_cart():

    number_products_in_user_cart = None

    if session.get('user_cart'):
        user_cart = session.get('user_cart')
        number_products_in_user_cart = \
            sum(user_cart.values()) if user_cart else 0

    return dict(number_products_in_user_cart=number_products_in_user_cart)


@app.route('/clear_session/')
def clear_session():
    session.clear()
    return redirect(url_for('index'))


@app.route('/add_one_thing_shopping_cart/<int:id_meal>/')
def add_one_thing_shopping_cart(id_meal):

    if current_user.is_authenticated:

        str_id_meal: str = str(id_meal)

        if session.get('user_cart'):

            user_cart = session.get('user_cart')

            if user_cart.get(str_id_meal):
                user_cart[str_id_meal] += 1
            else:
                user_cart.update({str_id_meal: 1})

            session['user_cart'] = user_cart

        else:
            session['user_cart'] = {str_id_meal: 1}

        anchor_formation: str = "meal_" + str(id_meal)

        return redirect(url_for('index', _anchor=anchor_formation))

    else:
        return redirect(url_for('log_in_account'))


@app.route('/subtract_one_thing_shopping_cart/<int:id_meal>/')
def subtract_one_thing_shopping_cart(id_meal):

    if current_user.is_authenticated:

        str_id_meal: str = str(id_meal)

        if session.get('user_cart'):

            user_cart = session.get('user_cart')

            if user_cart.get(str_id_meal) > 1:
                user_cart[str_id_meal] -= 1
            else:
                user_cart.pop(str_id_meal)

            session['user_cart'] = user_cart

        anchor_formation: str = "meal_" + str(id_meal)

        return redirect(url_for('index', _anchor=anchor_formation))

    else:
        return redirect(url_for('log_in_account'))


if __name__ == '__main__':
    app.run()
