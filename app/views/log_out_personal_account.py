from config import app
from flask import url_for, \
                  redirect
from flask_login import logout_user, \
                        login_required


@app.route('/log_out_personal_account/')
@login_required
def log_out_personal_account():
    logout_user()
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run()
