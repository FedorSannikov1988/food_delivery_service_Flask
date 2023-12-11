from config import app
from flask import flash, \
                  url_for, \
                  request, \
                  redirect, \
                  render_template
from flask_login import current_user, \
                        login_required
from app.db_api import add_user_photo, \
                       change_password, \
                       delete_user_photo, \
                       change_personal_data, \
                       change_default_shipping_address
from werkzeug.utils import secure_filename
from app.utilities import WorkingWithFiles
from app.forms import PersonalAccountChangePassword, \
                      PersonalAccountChangePersonalData, \
                      PersonalAccountChangeDeliveryAddress


@app.route('/personal_account/', methods=['GET', 'POST'])
@login_required
def personal_account():

    if request.method == 'POST':
        file = \
            request.files.get('file')
        user_photo_to_delete = \
            request.form.get('user_photo_to_delete')

        if file:

            file_name = secure_filename(file.filename)
            name_old_photo = \
                add_user_photo(email=current_user.email,
                               new_path_photo=file_name)

            if name_old_photo:

                __delete_user_photo_in_personal_account(name_file_photo=
                                                        name_old_photo)

            path_new_photo = \
                WorkingWithFiles.generating_path_file_in_folder__user_photos(name_file=
                                                                             file_name)
            file.save(path_new_photo)

        if user_photo_to_delete:

            __delete_user_photo_in_personal_account(name_file_photo=
                                                    user_photo_to_delete)

            delete_user_photo(email=current_user.email)

    context = {
        'title_page': 'Личный кабинет',
        'date_birth': current_user.date_birth.strftime('%d.%m.%Y')
    }
    return render_template('personal_account.html', **context)


def __delete_user_photo_in_personal_account(name_file_photo: str) -> None:

    path_user_photo_to_delete = \
        WorkingWithFiles.generating_path_file_in_folder__user_photos(name_file=
                                                                     name_file_photo)

    WorkingWithFiles(path_to_file=path_user_photo_to_delete).delete_file()


@app.route('/personal_account_change_personal_data/', methods=['GET', 'POST'])
@login_required
def personal_account_change_personal_data():

    form = PersonalAccountChangePersonalData()

    if request.method == 'POST' and form.validate():

        name = form.name.data
        surname = form.surname.data
        patronymic = form.patronymic.data
        date_birth = form.date_birth.data

        change_personal_data(email=current_user.email,
                             name=name,
                             surname=surname,
                             patronymic=patronymic,
                             date_birth=date_birth)

        return redirect(url_for('personal_account'))

    context = {
        'title_page': 'Личный кабинет - Изминение персональных данных.'
    }
    return render_template('personal_account_change_personal_data.html', form=form, **context)


@app.route('/personal_account_change_delivery_address/', methods=['GET', 'POST'])
@login_required
def personal_account_change_delivery_address():

    form = PersonalAccountChangeDeliveryAddress()

    if request.method == 'POST' and form.validate():

        new_default_shipping_address = \
            form.default_shipping_address.data

        change_default_shipping_address(
            email=current_user.email,
            new_default_shipping_address=
            new_default_shipping_address)

        return redirect(url_for('personal_account'))

    context = {
        'title_page': 'Личный кабинет - Изминение адреса доставки по умолчанию.'
    }
    return render_template('personal_account_change_delivery_address.html', form=form, **context)


@app.route('/personal_account_change_password/', methods=['GET', 'POST'])
@login_required
def personal_account_change_password():

    form = PersonalAccountChangePassword()

    if request.method == 'POST' and form.validate():

        new_password = \
            form.password.data

        try:

            change_password(
                email=current_user.email,
                new_password=new_password)

            return redirect(url_for('personal_account'))

        except Exception:

            text: str = \
                f'Пароль изменить НЕ получилось. ' \
                f'Произошла неизвестная ошибка.'
            flash(text, 'error')

    context = {
        'title_page': 'Личный кабинет - Изминение пароля.'
    }
    return render_template('personal_account_change_password.html', form=form, **context)


if __name__ == '__main__':
    app.run()
