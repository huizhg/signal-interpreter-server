import pytest
from unittest.mock import patch
from src.main import parse_arguments, main, init
from src.routes import signal_interpreter_app
import sys
import os

current_dir = os.path.abspath(os.path.dirname(__file__))
json_file_path = os.path.join(current_dir, "fixtures", "test_basic.json")


@pytest.mark.parametrize("payload, expected_status_code, expected_response", [
    ({"signal": "11"}, 200, "ECU Reset"),
    ({"signal": "99"}, 404, None),
    ({"DUMMY": "27"}, 400, None)
])
@patch.object(signal_interpreter_app, "run")
@patch.object(sys, "argv", ["signal-interpreter-server", "--file_path", json_file_path])
def test_application_with_signal(mock_run, payload, expected_status_code, expected_response):
    main()
    mock_run()
    signal_interpreter_app.testing = True
    signal_interpreter = signal_interpreter_app.test_client()
    with signal_interpreter as client:
        response = client.post("/", json=payload)
        assert response.get_json() == expected_response
        assert response.status_code == expected_status_code

