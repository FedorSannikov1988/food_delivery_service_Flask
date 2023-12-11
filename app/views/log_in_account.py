from config import app
from flask import flash, \
                  url_for, \
                  request, \
                  redirect, \
                  render_template
from app.forms import UserLogIn
from flask_login import login_user
from app.db_api import searching_user_account


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


if __name__ == '__main__':
    app.run()
