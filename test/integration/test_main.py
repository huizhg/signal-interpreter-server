import pytest
from unittest.mock import patch
from src.main import parse_arguments, main, init
from src.routes import signal_interpreter_app
import sys
import os


current_dir = os.path.abspath(__file__)
json_file_path = os.path.join(current_dir,"..", "fixtures/test_basic.json")



@pytest.mark.parametrize("item, expected_result", [
    ("11", "ECU Reset"),
    ("27", "Security Access")

])
@patch.object(signal_interpreter_app, "run")
@patch.object(sys, "argv", ["signal-interpreter-server", "--file_path", json_file_path])
def test_application_with_signal(mock_run, item, expected_result):
    main()
    mock_run.assert_called_once()
    signal_interpreter_app.testing = True
    signal_interpreter = signal_interpreter_app.test_client()
    with signal_interpreter as client:
        my_payload = {"signal": item}
        response = client.post("/", json=my_payload)
        assert response.get_json() == expected_result

