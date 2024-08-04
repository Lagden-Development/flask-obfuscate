"""
Flask-Obfuscate
===============

A Flask extension that obfuscates HTML responses to help protect your HTML content.

This module provides the `Obfuscate` class, which can be used to initialize the obfuscation
middleware for a Flask application.

Usage:
    from flask_obfuscate import Obfuscate

    app = Flask(__name__)
    obfuscate = Obfuscate(app)

    @app.route('/')
    def index():
        return '<div>Hello, World!</div>'

    if __name__ == '__main__':
        app.run(debug=True)

Copyright (c) 2024 Zachariah Michael Lagden
"""

from .obfuscate import Obfuscate
