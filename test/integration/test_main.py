"""integration test of main function"""
# pylint: disable=missing-function-docstring
# pylint: disable=missing-module-docstring
import os
import sys
import pytest
from unittest.mock import patch
from src.main import main
from src.routes import signal_interpreter_app

CURRENT_DIR = os.path.abspath(os.path.dirname(__file__))

JSON_FILE_PATH = os.path.join(CURRENT_DIR, "fixtures", "test_basic.json")
XML_FILE_PATH = os.path.join(CURRENT_DIR, "fixtures", "test_basic.xml")
YAML_FILE_PATH = os.path.join(CURRENT_DIR, "fixtures", "test_basic.yaml")


@pytest.mark.parametrize("payload, expected_status_code, expected_response", [
    ({"signal": "11"}, 200, "ECU Reset"),
    ({"signal": "99"}, 404, None),
    ({"DUMMY": "27"}, 400, None)
])
@patch.object(signal_interpreter_app, "run")
@patch.object(sys, "argv", ["signal-interpreter-server",
                            "--file_path", JSON_FILE_PATH])
def test_application_with_json_file(mock_run, payload, expected_status_code, expected_response):
    main()
    mock_run()
    signal_interpreter_app.testing = True
    signal_interpreter = signal_interpreter_app.test_client()
    with signal_interpreter as client:
        response = client.post("/", json=payload)
        assert response.get_json() == expected_response
        assert response.status_code == expected_status_code


@pytest.mark.parametrize("payload, expected_status_code, expected_response", [
    ({"signal": "11"}, 200, "ECU Reset"),
    ({"signal": "99"}, 404, None),
    ({"DUMMY": "27"}, 400, None)
])
@patch.object(signal_interpreter_app, "run")
@patch.object(sys, "argv", ["signal-interpreter-server",
                            "--file_path", XML_FILE_PATH])
def test_application_with_xml_file(mock_run, payload, expected_status_code, expected_response):
    main()
    mock_run()
    signal_interpreter_app.testing = True
    signal_interpreter = signal_interpreter_app.test_client()
    with signal_interpreter as client:
        response = client.post("/", json=payload)
        assert response.get_json() == expected_response
        assert response.status_code == expected_status_code


@pytest.mark.parametrize("payload, expected_status_code, expected_response", [
    ({"signal": "11"}, 200, "ECU Reset"),
    ({"signal": "99"}, 404, None),
    ({"DUMMY": "27"}, 400, None)
])
@patch.object(signal_interpreter_app, "run")
@patch.object(sys, "argv",
              ["signal-interpreter-server", "--file_path", YAML_FILE_PATH])
def test_application_with_yaml_file(mock_run, payload, expected_status_code, expected_response):
    main()
    mock_run()
    signal_interpreter_app.testing = True
    signal_interpreter = signal_interpreter_app.test_client()
    with signal_interpreter as client:
        response = client.post("/", json=payload)
        assert response.get_json() == expected_response
        assert response.status_code == expected_status_code
