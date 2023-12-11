from config import app
from flask import send_from_directory


@app.route('/media/<path:filename>')
def media(filename):
    return send_from_directory('media', filename)


@app.route('/user_photos/<path:filename>')
def user_photos(filename):
    return send_from_directory('user_photos', filename)


if __name__ == '__main__':
    app.run()
