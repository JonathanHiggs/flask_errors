__author__ = 'jhiggs'
__version__ = '1.0.0'

from flask import Blueprint, render_template


__errors_blueprint = Blueprint('errors', __name__, template_folder='errors')


@__errors_blueprint.app_errorhandler(404)
def not_found_error(error):
    """Renders 404 - not found error"""
    return render_template('errors/404.html')


@__errors_blueprint.app_errorhandler(500)
def internal_error(error):
    """Renders 500 - internal server error"""
    return render_template('errors/500.html')


class Errors:
    def __init__(self, app=None):
        self.app = app
        if self.app is not None:
            self.init_app(self.app)

    def init_app(self, app):
        self.app = app
        self.app.register_blueprint(__errors_blueprint)
