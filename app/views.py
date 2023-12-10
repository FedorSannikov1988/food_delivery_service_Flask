from config import app, \
                   LOWER_AGE_YEARS, \
                   UPPER_AGE_YEARS, \
                   TIME_TO_ACTIVATE_ACCOUNT_HOURS, \
                   DURATION_PASSWORD_RECOVERY_LINK_MINUTES
from flask import flash, \
                  url_for, \
                  request, \
                  redirect, \
                  render_template, \
                  send_from_directory
from .mail import sent_mail
from .forms import UserLogIn, \
                   UserRegistration, \
                   ForgetPasswordEnteringEmail, \
                   ForgetPasswordEnterNewPassword
from flask_login import login_user, \
                        logout_user, \
                        current_user, \
                        login_required
from .utilities import WorkingWithToken, \
                       WorkingWithTimeInsideApp
from .db_api import add_user_in_database, \
                    searching_user_account,\
                    get_all_categories_meal, \
                    searching_and_activating_user_account, \
                    searching_user_account_and_setting_new_password
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
        telephone = form.telephone.data
        default_shipping_address = form.default_shipping_address.data
        password = form.password.data

        try:

            if WorkingWithTimeInsideApp().checking_user_age(date_birth=
                                                            date_birth):

                add_user_in_database(name=name,
                                     surname=surname,
                                     patronymic=patronymic,
                                     date_birth=date_birth,
                                     telephone=telephone,
                                     email=email,
                                     password=password,
                                     default_shipping_address=
                                     default_shipping_address)

                server_address = request.host_url
                timestamp: str = WorkingWithTimeInsideApp().get_data_and_time()
                token = WorkingWithToken().get_token(data={'destiny': 'user_registration',
                                                           'id_user': email,
                                                           'date_and_time': timestamp})

                title_email: str = f"Активация аккаунта на {server_address}"
                text_email: str = f"\n\n Для активация аккаунта перейдите по ссылке: " \
                                  f"{server_address}activating_user_account/{token}"

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

    data: dict = WorkingWithToken().get_data_from_token(token)

    destiny: str = \
        data.get('destiny')

    id_user: str = \
        data.get('id_user')

    date_and_time_registration_user: str = \
        data.get('date_and_time')

    if id_user and \
            destiny and \
            date_and_time_registration_user:

        if WorkingWithTimeInsideApp().\
                checking_date_and_time_registration_user(
            date_and_time_registration_user=
            date_and_time_registration_user
        ) and destiny == 'user_registration':

            searching_and_activating_user_account(email=id_user)
            text: str = \
                f'Ваша учетная запись активирована !'
            flash(text, 'success')

        elif WorkingWithTimeInsideApp().\
                checking_date_and_time_registration_user(
            date_and_time_registration_user=
            date_and_time_registration_user
        ) and destiny != 'user_registration':

            text: str = \
                f'Ваша ссылка не валидна.'
            flash(text, 'error')

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

        email: str = form.email.data
        password: str = form.password.data
        remember: bool = form.remember.data

        user = searching_user_account(email=email)

        if user and user.check_password(password=password):
            if user.status:
                login_user(user, remember=remember)
                return redirect(url_for('personal_account'))
            else:
                text: str = \
                    f'Ваша учетная запись не активирована.'
                flash(text, 'error')
        elif not user.check_password(password=password):
            text: str = \
                f'Неверный пароль'
            flash(text, 'error')
        else:
            text: str = \
                f'Неверное имя пользователя или пароль'
            flash(text, 'error')
            return redirect(url_for('log_in_account'))

    context = {
        'title_pag': 'Вход в личный кабинет'
    }
    return render_template('log_in_account.html', form=form, **context)


@app.route('/personal_account/')
@login_required
def personal_account():

    context = {
        'title_pag': ' Личный кабинет',
        'date_birth': current_user.date_birth.strftime('%d.%m.%Y')
    }
    return render_template('personal_account.html', **context)


@app.route('/log_out_personal_account/')
@login_required
def log_out_personal_account():
    logout_user()
    return redirect(url_for('index'))


@app.route('/forget_password_enter_email/', methods=['GET', 'POST'])
def forget_password_enter_email():

    form = ForgetPasswordEnteringEmail()

    if request.method == 'POST' and form.validate():

        email = form.email.data
        user = searching_user_account(email=email)

        if user and user.status:

            server_address = request.host_url
            timestamp: str = WorkingWithTimeInsideApp().get_data_and_time()
            token = WorkingWithToken().get_token(data={'destiny': 'password_recovery',
                                                       'id_user': email,
                                                       'date_and_time': timestamp})

            title_email: str = f"Востановление пароля на {server_address}"
            text_email: str = f"\n\n Для восстановления пароля перейдите по ссылке: " \
                              f"{server_address}forget_password_enter_new_password/{token}"

            sent_mail(address=email,
                      heading=title_email,
                      text=text_email)

            text: str = \
                f'На вашу почту отправлена ссылка для смены пароля.'
            flash(text, 'success')
        elif user and not user.status:

            text: str = \
                f'Ваша учетная запись не активирована.'
            flash(text, 'error')

        else:
            text: str = \
                f'Данной учетной записи не найдено'
            flash(text, 'error')

    context = {
        'title_pag': 'Забыли пароль - ввод электронной почты'
    }
    return render_template('forget_password_enter_email.html', form=form, **context)


@app.route('/forget_password_enter_new_password/<token>', methods=['GET', 'POST'])
def forget_password_enter_new_password(token: str = ' '):

    show_form: bool = False
    form = ForgetPasswordEnterNewPassword()

    data: dict = WorkingWithToken().get_data_from_token(token)

    destiny: str = \
        data.get('destiny')

    id_user: str = \
        data.get('id_user')

    date_and_time_receipt_request: str = \
        data.get('date_and_time')

    if id_user and \
            destiny and \
            date_and_time_receipt_request:

        if destiny != 'password_recovery':

            text: str = \
                f'Ваша ссылка не валидна.'
            flash(text, 'error')

        elif WorkingWithTimeInsideApp(). \
                checking_time_password_recovery_request(
            time_receipt_request=
            date_and_time_receipt_request
        ) and destiny == 'password_recovery':

            show_form = True

        else:

            text: str = \
                f'Ваша ссылка для восстановления пароля просрочена.' \
                f'Ссылка актуальна {DURATION_PASSWORD_RECOVERY_LINK_MINUTES} минут.'
            flash(text, 'error')
    else:
        text: str = \
            f'Ваша ссылка не валидна.'
        flash(text, 'error')

    if request.method == 'POST' and form.validate():
        password = form.password.data

        try:
            searching_user_account_and_setting_new_password(email=id_user,
                                                            password=password)
            text: str = \
                f'Ваш пароль изминен'
            flash(text, 'success')

        except Exception:
            text: str = \
                f'Произошла неизвесная ошибка. Ваш пароль изминить не получилось.'
            flash(text, 'error')

    context = {
        'title_pag': 'Забыли пароль - ввод нового пароля',
        'show_form': show_form,
        'token': token
    }
    return render_template('forget_password_enter_new_password.html', form=form, **context)


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
