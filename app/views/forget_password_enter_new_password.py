from config import app, \
                   DURATION_PASSWORD_RECOVERY_LINK_MINUTES
from flask import flash, \
                  request, \
                  render_template
from app.utilities import WorkingWithToken, \
                          WorkingWithTimeInsideApp
from app.forms import ForgetPasswordEnterNewPassword
from app.db_api import searching_user_account_and_setting_new_password


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
        'title_page': 'Забыли пароль - ввод нового пароля',
        'show_form': show_form,
        'token': token
    }
    return render_template('forget_password_enter_new_password.html', form=form, **context)


if __name__ == '__main__':
    app.run()
