# pylint: disable=missing-function-docstring
# pylint: disable=missing-module-docstring, missing-class-docstring
from src.routes import signal_interpreter_app, parserFactory, SignalNotFoundError
from src.json_parser import JsonParser
from unittest.mock import patch


def test_interpret_signal():
    with patch.object(JsonParser, "get_signal_title", return_value="ECU Reset"):
        with patch.object(parserFactory, "get_parser", return_value=JsonParser):
            signal_interpreter_app.testing = True
            signal_interpreter = signal_interpreter_app.test_client()
            with signal_interpreter as client:
                response = client.post("/", json={"signal": "11"})
                assert response.get_json() == "ECU Reset"
                assert response.status_code == 200


def test_interpret_signal_invalid_key():
    with patch.object(JsonParser, "get_signal_title", side_effect=KeyError):
        with patch.object(parserFactory, "get_parser", return_value=JsonParser):
            signal_interpreter_app.testing = True
            signal_interpreter = signal_interpreter_app.test_client()
            with signal_interpreter as client:
                response = client.post("/", json={"dummy": "99"})
                assert response.get_json() is None
                assert response.status_code == 400


def test_interpret_signal_invalid_identifier():
    with patch.object(JsonParser, "get_signal_title", side_effect=SignalNotFoundError):
        with patch.object(parserFactory, "get_parser", return_value=JsonParser):
            signal_interpreter_app.testing = True
            signal_interpreter = signal_interpreter_app.test_client()
            with signal_interpreter as client:
                response = client.post("/", json={"signal": "99"})
                assert response.get_json() is None
                assert response.status_code == 404
