"""
This module is responsible for redirecting to receive
from outside the application.
By outside, I mean finding sources (files not in the
application directory)
"""
from config import app
from flask import Response, \
                  send_from_directory


@app.route('/media/<path:filename>')
def media(filename) -> Response:
    """
    Route to serve media files.

    Description:
    This route serves media files from the 'media' directory.
    The filename is provided as a path parameter.
    The file is retrieved from the 'media' directory and returned
    as a response.

    :param filename: str -> the name of the file to be served
    :return: Response -> the file to be downloaded
    """
    return send_from_directory('media', filename)


@app.route('/user_photos/<path:filename>')
def user_photos(filename) -> Response:
    """
    Route to serve user photos.

    Description:
    This route serves user photos from the 'user_photos' directory.
    The filename is provided as a path parameter.
    The file is retrieved from the 'user_photos' directory and
    returned as a response.

    :param filename: str -> the name of the file to be served
    :return: Response -> the file to be downloaded
    """
    return send_from_directory('user_photos', filename)


if __name__ == '__main__':
    app.run()
