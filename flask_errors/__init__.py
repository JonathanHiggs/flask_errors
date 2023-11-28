"""
flask_errors
"""

__author__ = 'jhiggs'
__version__ = '1.0.1'

from flask import Blueprint, Flask, Response, render_template, current_app


def not_found_error(error) -> Response:
    """ Renders 404 - not found error """
    return render_template(
        'errors/404.html',
        home_endpoint=current_app.extensions['flask-errors'].home_endpoint)


def internal_error(error) -> Response:
    """ Renders 500 - internal server error """
    return render_template(
        'errors/500.html',
        home_endpoint=current_app.extensions['flask-errors'].home_endpoint)


class Errors:
    def __init__(self, app: Flask = None, home_endpoint: str = None):
        self._app = app
        self._home_endpoint = home_endpoint

        if self._app is not None:
            self._init_app(self._app)

    def _init_app(self, app: Flask):
        self._app = app

        blueprint = Blueprint('errors', __name__, template_folder='templates')

        blueprint.app_errorhandler(404)(not_found_error)
        blueprint.app_errorhandler(404)(internal_error)

        app.register_blueprint(blueprint)

        if app.extensions is None:
            app.extensions = dict()

        app.extensions['flask-errors'] = self

    def init_app(self, app: Flask):
        """ Initialize errors module with Flask application """
        if self.app is not None:
            raise RuntimeWarning('Errors already initialized')

        self._init_app(app)
