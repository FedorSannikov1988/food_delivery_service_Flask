from config import app
from flask import request, \
                  render_template
from flask_login import current_user, \
                        login_required
from app.db_api import add_user_photo, \
                       delete_user_photo
from app.utilities import WorkingWithFiles
from werkzeug.utils import secure_filename


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

                path_old_photo = \
                    WorkingWithFiles.generating_path_file_in_folder__user_photos(name_file=
                                                                                 name_old_photo)

                WorkingWithFiles(path_to_file=path_old_photo).delete_file()

            path_new_photo = \
                WorkingWithFiles.generating_path_file_in_folder__user_photos(name_file=
                                                                             file_name)
            file.save(path_new_photo)

        if user_photo_to_delete:
            delete_user_photo(email=current_user.email)

    context = {
        'title_pag': 'Личный кабинет',
        'date_birth': current_user.date_birth.strftime('%d.%m.%Y')
    }
    return render_template('personal_account.html', **context)


if __name__ == '__main__':
    app.run()
