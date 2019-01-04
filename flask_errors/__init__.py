__author__ = 'jhiggs'
__version__ = '1.0.0'

from flask import Blueprint, render_template, current_app


errors_blueprint = Blueprint('errors', __name__, template_folder='templates')


@errors_blueprint.app_errorhandler(404)
def not_found_error(error):
    """Renders 404 - not found error"""
    return render_template(
        'errors/404.html',
        home_endpoint=current_app.extensions['flask-errors'].home_endpoint)

@errors_blueprint.app_errorhandler(500)
def internal_error(error):
    """Renders 500 - internal server error"""
    return render_template(
        'errors/500.html',
        home_endpoint=current_app.extensions['flask-errors'].home_endpoint)

class Errors:
    def __init__(self, app=None, home_endpoint=None):
        self.app = app
        self.home_endpoint = home_endpoint

        if self.app is not None:
            self.init_app(self.app)

    def init_app(self, app):
        global errors_blueprint
        self.app = app
        self.app.register_blueprint(errors_blueprint)
        self.app.extensions['flask-errors'] = self
