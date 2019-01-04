# Flask Errors

Flask extension that adds error handlers to your app

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Installing

Clone the repo and install Flask-Errors with `pip`:

```bash
git clone ssh://github.com/JonathanHiggs/flask_errors
cd flask_errors
pip install .
```

### Example

An example of a simple flask app with the extension installed:

```python
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
```

The templates for errors extend from `base.html` and require an `app_content` block
