from config import app
from flask import flash, \
                  request, \
                  render_template
from app.mail import sent_mail
from app.utilities import WorkingWithToken, \
                          WorkingWithTimeInsideApp
from app.db_api import searching_user_account
from app.forms import ForgetPasswordEnteringEmail


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


if __name__ == '__main__':
    app.run()
