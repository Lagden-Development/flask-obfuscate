import pytest
from flask import Flask, Blueprint
from flask_obfuscate import Obfuscate


@pytest.fixture
def app():
    app = Flask(__name__)
    obfuscate = Obfuscate(app)
    return app


def test_obfuscate(app):
    @app.route("/")
    def index():
        return "<div>Hello, World!</div>"

    with app.test_client() as client:
        response = client.get("/")
        assert response.status_code == 200
        assert "document.write(unescape" in response.get_data(as_text=True)
        assert "<div>Hello, World!</div>" not in response.get_data(as_text=True)


def test_non_html_response(app):
    @app.route("/json")
    def json_route():
        return {"message": "Hello, World!"}

    with app.test_client() as client:
        response = client.get("/json")
        assert response.status_code == 200
        assert response.is_json
        assert response.get_json() == {"message": "Hello, World!"}


def test_large_html_document(app):
    @app.route("/large")
    def large_route():
        large_html = "<div>" + "Hello, World! " * 1000 + "</div>"
        return large_html

    with app.test_client() as client:
        response = client.get("/large")
        assert response.status_code == 200
        assert "document.write(unescape" in response.get_data(as_text=True)
        assert "Hello, World!" not in response.get_data(as_text=True)


def test_special_characters(app):
    @app.route("/special")
    def special_route():
        return "<div>Special characters: <>&'\"</div>"

    with app.test_client() as client:
        response = client.get("/special")
        assert response.status_code == 200
        assert "document.write(unescape" in response.get_data(as_text=True)
        assert "<div>Special characters: <>&'\"</div>" not in response.get_data(
            as_text=True
        )


def test_empty_html(app):
    @app.route("/empty")
    def empty_route():
        return ""

    with app.test_client() as client:
        response = client.get("/empty")
        assert response.status_code == 200
        assert response.get_data(as_text=True) == ""


def test_blueprint_integration(app):
    bp = Blueprint("bp", __name__)

    @bp.route("/bp")
    def bp_route():
        return "<div>Blueprint route</div>"

    app.register_blueprint(bp, url_prefix="/bp")

    with app.test_client() as client:
        response = client.get("/bp/bp")
        assert response.status_code == 200
        assert "document.write(unescape" in response.get_data(as_text=True)
        assert "<div>Blueprint route</div>" not in response.get_data(as_text=True)
