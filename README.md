# Flask-Obfuscate

Flask-Obfuscate is a Flask extension that obfuscates HTML responses to help protect your HTML content from easy inspection or copying. This extension processes all HTML responses and converts them into obfuscated JavaScript that writes the HTML content when executed in a browser.

## Features

- Obfuscates HTML responses by converting them to JavaScript
- Easy to integrate into existing Flask applications
- Simple usage with minimal configuration

## Installation

You can install Flask-Obfuscate via pip:

```sh
pip install Flask-Obfuscate
```

## Usage

### Basic Usage

Integrate Flask-Obfuscate into your Flask application with minimal setup:

```python
from flask import Flask
from flask_obfuscate import Obfuscate

app = Flask(__name__)
obfuscate = Obfuscate(app)

@app.route('/')
def index():
    return '<div>Hello, World!</div>'

if __name__ == '__main__':
    app.run(debug=True)
```

### Advanced Usage

You can also initialize Flask-Obfuscate later using the `init_app` method:

```python
from flask import Flask
from flask_obfuscate import Obfuscate

app = Flask(__name__)
obfuscate = Obfuscate()
obfuscate.init_app(app)

@app.route('/')
def index():
    return '<div>Hello, World!</div>'

if __name__ == '__main__':
    app.run(debug=True)
```

## Running Tests

To run the tests, first install the test dependencies:

```sh
pip install pytest
```

Then you can run the tests using pytest:

```sh
pytest tests
```

## Contributing

Contributions are welcome! Please submit a pull request or open an issue to discuss improvements or fixes.

1. Fork the repository.
2. Create a new branch: `git checkout -b my-feature-branch`
3. Make your changes and commit them: `git commit -am 'Add some feature'`
4. Push to the branch: `git push origin my-feature-branch`
5. Submit a pull request.

## License

This project is licensed under the MIT License.

## Acknowledgments

Inspired by the need to protect HTML content in Flask applications.
