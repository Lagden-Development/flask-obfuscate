"""
Flask-Obfuscate
===============

A Flask extension that obfuscates HTML responses to help protect your HTML content.

Copyright (c) 2024 Zachariah Michael Lagden
"""

from flask import Flask, Response


class Obfuscate:
    """
    Flask extension for obfuscating HTML responses.

    This class provides a mechanism to obfuscate HTML content returned by Flask routes
    by encoding the HTML in a way that can be decoded and displayed by the browser.

    Attributes:
        app (Flask): The Flask application instance.
    """

    def __init__(self, app: Flask = None) -> None:
        """
        Initialize the Obfuscate extension.

        Args:
            app (Flask, optional): The Flask application instance. Defaults to None.
        """
        if app is not None:
            self.init_app(app)

    def init_app(self, app: Flask) -> None:
        """
        Initialize the Flask application with the obfuscation middleware.

        Args:
            app (Flask): The Flask application instance.
        """

        @app.after_request
        def obfuscate_response(response: Response) -> Response:
            """
            Middleware to obfuscate HTML responses.

            Args:
                response (Response): The Flask response object.

            Returns:
                Response: The modified response with obfuscated HTML content.
            """

            # Check if the response is an HTML document and contains content

            if (
                response.content_type == "text/html; charset=utf-8"
                and response.get_data(as_text=True).strip()
            ):
                response.set_data(self.obfuscate_html(response.get_data(as_text=True)))

            return response

    def obfuscate_html(self, html_str: str) -> str:
        """
        Obfuscate the given HTML string.

        Args:
            html_str (str): The HTML content to obfuscate.

        Returns:
            str: The obfuscated HTML content.
        """

        def hex_from_dec(num: int) -> str:
            """
            Convert a decimal number to a two-digit hexadecimal string.

            Args:
                num (int): The decimal number to convert.

            Returns:
                str: The hexadecimal string.
            """
            if num > 65535:
                raise ValueError("Number out of range for hex conversion")
            first = num // 4096
            temp1 = num - first * 4096
            second = temp1 // 256
            temp2 = temp1 - second * 256
            third = temp2 // 16
            fourth = temp2 - third * 16
            return f"{convert(third)}{convert(fourth)}"

        def convert(num: int) -> str:
            """
            Convert a number to its hexadecimal character equivalent.

            Args:
                num (int): The number to convert (0-15).

            Returns:
                str: The hexadecimal character.
            """
            if num < 10:
                return str(num)
            else:
                return "ABCDEF"[num - 10]

        def obfuscate(text: str) -> str:
            """
            Obfuscate the given text by converting each character to its hexadecimal URL-encoded equivalent.

            Args:
                text (str): The text to obfuscate.

            Returns:
                str: The obfuscated text.
            """
            return "".join(f"%{hex_from_dec(ord(char))}" for char in text)

        obfuscated_text = obfuscate(html_str)
        obfuscated_html = f"<script language=\"javascript\">document.write(unescape('{obfuscated_text}'))</script>"
        return obfuscated_html
