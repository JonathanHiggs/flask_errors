import os
from flask import Flask
from flask_errors import Errors

app = Flask(__name__)

errors = Errors()
errors.init_app(app)
errors.home_endpoint = 'home'

@app.route('/')
def home():
    return """<a href='/not-a-path'>Try this</a>"""

if __name__ == '__main__':
    host = os.environ.get('FLASK_HOST') or 'localhost'
    port = os.environ.get('FLASK_PORT') or '5000'

    app.run(host=host, port=port)
