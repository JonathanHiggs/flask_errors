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
from flask import Flask
from flask_errors import Errors

app = Flask(__name__)

errors = Errors()
errors.init_app(app)

app.run()
```
