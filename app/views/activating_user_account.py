"""
This module is used to create views when activating a user account.
"""
from config import app, \
                   TIME_TO_ACTIVATE_ACCOUNT_HOURS
from flask import flash, \
                  render_template
from app.utilities import WorkingWithToken, \
                          WorkingWithTimeInsideApp
from app.db_api import searching_and_activating_user_account


@app.route('/activating_user_account/<token>')
def activating_user_account(token: str = ''):
    """
    Route for activating a user account.

    Description:
    This route is used to activate a user account based on the provided
    activation token.
    The token is extracted from the URL path parameter.
    The function retrieves the necessary data from the token using the
    `WorkingWithToken` class.
    The data includes the user's ID, destiny, and date and time of registration.
    If the required data is present, the function checks if the registration
    date and time are valid and if the destiny is 'user_registration'.
    If the conditions are met, the function calls the
    `searching_and_activating_user_account` function to activate the
    user account.
    A success flash message is displayed to the user.
    If the conditions are not met, an error flash message is displayed
    based on the specific condition that failed.
    If the required data is not present, an error flash message is displayed
    indicating that the activation link has expired.
    The function renders the 'flash_message_for_user.html' template with the
    appropriate context.

    :param token: str (optional) -> the activation token
    :return: Response -> Rendered template for displaying a flash
    message to the user.
    """

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
        'title_page': 'Активация аккаунта'
    }
    return render_template('flash_message_for_user.html', **context)


if __name__ == '__main__':
    app.run()
