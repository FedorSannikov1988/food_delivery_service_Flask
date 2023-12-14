from config import app
from app.db_api import Meal, \
                       get_meal
from flask import url_for, \
                  session, \
                  redirect, \
                  render_template
from flask_login import current_user


@app.route('/shopping_cart_user/')
def shopping_cart_user():

    if current_user.is_authenticated:

        user_cart = session.get('user_cart')

        purchases: list = []

        full_price: float = 0

        if user_cart:

            for id_food, quantity in user_cart.items():

                meal: Meal = \
                    get_meal(id_meal=int(id_food))

                full_price += meal.cost * quantity

                meal: dict = \
                    {
                        'id': meal.id,
                        'file_path_image': meal.file_path_image,
                        'title': meal.title,
                        'description': meal.description,
                        'weight': meal.weight,
                        'cost': meal.cost,
                        'total_cost': meal.cost * quantity
                    }

                meal.update({'quantity': quantity})

                purchases.append(meal)

        context = {
            'title_page': 'Корзина покупателя',
            'purchases': purchases,
            'full_price': full_price
        }
        return render_template('shopping_cart_user.html', **context)
    else:
        return redirect(url_for('log_in_account'))


@app.context_processor
def inject_number_products_in_user_cart():

    number_products_in_user_cart = None

    if session.get('user_cart'):
        user_cart = session.get('user_cart')
        number_products_in_user_cart = \
            sum(user_cart.values()) if user_cart else 0

    return dict(number_products_in_user_cart=
                number_products_in_user_cart)


@app.route('/add_one_thing_shopping_cart/<where_return>/<int:id_meal>/')
def add_one_thing_shopping_cart(where_return: str, id_meal: int):

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

        return redirect(url_for(where_return, _anchor=anchor_formation))

    else:
        return redirect(url_for('log_in_account'))


@app.route('/subtract_one_thing_shopping_cart/<where_return>/<int:id_meal>/')
def subtract_one_thing_shopping_cart(where_return: str, id_meal: int):

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

        return redirect(url_for(where_return, _anchor=anchor_formation))

    else:
        return redirect(url_for('log_in_account'))


@app.route('/delete_all_thing_shopping_cart/<where_return>/<int:id_meal>/')
def delete_all_thing_shopping_cart(where_return: str, id_meal: int):

    if current_user.is_authenticated:

        str_id_meal: str = str(id_meal)

        if session.get('user_cart'):

            user_cart = session.get('user_cart')

            user_cart.pop(str_id_meal)

            session['user_cart'] = user_cart

        anchor_formation: str = "meal_" + str(id_meal)

        return redirect(url_for(where_return, _anchor=anchor_formation))

    else:
        return redirect(url_for('log_in_account'))


if __name__ == '__main__':
    app.run()
