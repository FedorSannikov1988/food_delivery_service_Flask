from config import app, \
                   LOWER_AGE_YEARS, \
                   UPPER_AGE_YEARS
from flask import flash, \
                  url_for, \
                  request, \
                  redirect, \
                  render_template
from app.mail import sent_mail
from app.forms import UserRegistration
from app.db_api import add_user_in_database
from app.utilities import WorkingWithToken, \
                          WorkingWithTimeInsideApp
from sqlalchemy.exc import IntegrityError


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
        'title_page': 'Регистрация пользователя'
    }
    return render_template('user_registration.html', form=form, **context)


if __name__ == '__main__':
    app.run()
