from config import app, \
                   TIME_TO_ACTIVATE_ACCOUNT_HOURS
from flask import flash, \
                  render_template
from app.utilities import WorkingWithToken, \
                          WorkingWithTimeInsideApp
from app.db_api import searching_and_activating_user_account


@app.route('/activating_user_account/<token>')
def activating_user_account(token: str = ''):

    data: dict = \
        WorkingWithToken().get_data_from_token(token)

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


if __name__ == '__main__':
    app.run()
