from config import app, \
                   LOWER_AGE_YEARS, \
                   UPPER_AGE_YEARS, \
                   TIME_TO_ACTIVATE_ACCOUNT_HOURS
from flask import flash, \
                  url_for, \
                  request, \
                  redirect, \
                  render_template, \
                  send_from_directory
from .mail import sent_mail
from .forms import UserLogIn, \
                   UserRegistration
from .utilities import get_token, \
                       get_data_and_time, \
                       checking_user_age, \
                       get_data_from_token, \
                       checking_date_and_time_registration_user
from .db_api import add_user_in_database, \
                    get_all_categories_meal, \
                    searching_and_activating_user_account
from sqlalchemy.exc import IntegrityError


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

        try:

            if checking_user_age(date_birth=date_birth):

                add_user_in_database(name=name,
                                     surname=surname,
                                     patronymic=patronymic,
                                     date_birth=date_birth,
                                     email=email,
                                     password=password,
                                     default_shipping_address=
                                     default_shipping_address)

                server_address = request.host_url
                timestamp: str = get_data_and_time()
                token = get_token(data={'id_user': email,
                                        'date_and_time_registration_user': timestamp})

                title_email: str = f"Активация аккаунта на {server_address}"
                text_email: str = f"\n\n Для активация аккаунта перейдите по ссылке: " \
                                  f"{server_address}/activating_user_account/{token}"

                sent_mail(address=email,
                          heading=title_email,
                          text=text_email)

                text: str = \
                    f'Пользователь {name} {surname} успешно зарегистрирован ! ' \
                    f'Для активации аккаунта перейдите по ссылке отправленно ' \
                    f'в письме на: {email}.'
                flash(text, 'success')

                return redirect(url_for('flash_message_for_user'))

            else:
                text: str = \
                    f'Для регистрации Ваш возраст должен быть в диапазоне ' \
                    f'от {LOWER_AGE_YEARS} до {UPPER_AGE_YEARS} включительно.'
                flash(text, 'error')

                return redirect(url_for('user_registration'))

        except IntegrityError as error:

            error_code = error.orig.args[0]

            if 'UNIQUE' in error_code and 'email' in error_code:

                text: str = \
                    f'Пользователь c электронной почтой {email} уже зарегестрирован.'\
                    f'Электронная почта не должна повторяться у разных пользователей.'
                flash(text, 'error')

        except Exception:

            text: str = \
                f'Пользователь {name} {surname} ' \
                f'c электронной почтой {email} ' \
                f'НЕ зарегистрирован ' \
                f'(произошла неизвестная ошибка) !'
            flash(text, 'error')

    context = {
        'title_pag': 'Регистрация пользователя'
    }
    return render_template('user_registration.html', form=form, **context)


@app.route('/determining_length_string/<text>/')
def determining_length_string(text: str = ''):
    return f'Длинна строки {text} составляет {len(text)} символов'


@app.route('/activating_user_account/<token>')
def activating_user_account(token: str = ''):

    data: dict = get_data_from_token(token)

    id_user: str = \
        data.get('id_user')

    date_and_time_registration_user: str = \
        data.get('date_and_time_registration_user')

    if id_user and \
            date_and_time_registration_user:

        if checking_date_and_time_registration_user(date_and_time_registration_user=
                                                    date_and_time_registration_user):

            searching_and_activating_user_account(email=id_user)
            text: str = \
                f'Ваша учетная запись активирована !'
            flash(text, 'success')

        else:
            text: str = \
                f'Ваша ссылка для активации учетной записи просрочена.' \
                f'Ссылка акуальна только {TIME_TO_ACTIVATE_ACCOUNT_HOURS} часа' \
                f'с момента регистрации. Обратитесь к администратору сайта.'
            flash(text, 'error')

    context = {
        'title_pag': 'Активация аккаунта'
    }
    return render_template('flash_message_for_user.html', **context)


@app.route('/flash_message_for_user/')
def flash_message_for_user():

    context = {
        'title_pag': 'Оповещение пользователя'
    }
    return render_template('flash_message_for_user.html', **context)


@app.route('/log_in_account/', methods=['GET', 'POST'])
def log_in_account():

    form = UserLogIn()

    if request.method == 'POST' and form.validate():

        email = form.email.data
        password = form.password.data

        print(email)
        print(password)

    context = {
        'title_pag': 'Вход в личный кабинет'
    }
    return render_template('log_in_account.html', form=form, **context)


if __name__ == '__main__':
    app.run()
