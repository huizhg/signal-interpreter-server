from src.routes import signal_interpreter_app
from unittest.mock import patch
from src.json_parser import JsonParser


@patch.object(JsonParser, "get_signal_title", return_value="Transfer Data")
def test_interpret_signal(mock_get_signal_title):
    signal_interpreter_app.testing = True
    signal_interpreter = signal_interpreter_app.test_client()
    with signal_interpreter as client:
        my_payload = {"signal": "16"}
        response = client.post("/", json=my_payload)
        assert response.get_json() == "Transfer Data"
