from config import app
from flask import request,\
                  render_template, \
                  send_from_directory
from .forms import UserRegistration
from .db_api import add_user_in_database, \
                    get_all_categories_meal


@app.route('/media/<path:filename>')
def media(filename):
    return send_from_directory('media', filename)


@app.route('/')
def index():

    context = {
        'title_pag': 'Главная страница',
        'all_categories_meal': get_all_categories_meal()
    }
    return render_template('index.html', **context)


@app.route('/terms_of_delivery/')
def terms_of_delivery():

    context = {
        'title_pag': 'Условия доставки'
    }
    return render_template('terms_of_delivery.html', **context)


@app.route('/contacts/')
def contacts():

    context = {
        'title_pag': 'Контакты'
    }
    return render_template('сontacts.html', **context)


@app.route('/user_registration/', methods=['GET', 'POST'])
def user_registration():

    form = UserRegistration()

    if request.method == 'POST' and form.validate():

        name = form.name.data
        surname = form.surname.data
        patronymic = form.patronymic.data
        date_birth = form.date_birth.data
        email = form.email.data
        default_shipping_address = form.default_shipping_address.data
        password = form.password.data

        print("***")
        print(name)
        print(surname)
        print(patronymic)
        print(date_birth)
        print(email)
        print(default_shipping_address)
        print(password)
        print("***")

        add_user_in_database(name=name,
                             surname=surname,
                             patronymic=patronymic,
                             date_birth=date_birth,
                             email=email,
                             password=password,
                             default_shipping_address=
                             default_shipping_address)

    context = {
        'title_pag': 'Регистрация пользователя'
    }
    return render_template('user_registration.html',
                           form=form,
                           **context)


if __name__ == '__main__':
    app.run()
