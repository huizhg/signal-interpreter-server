# pylint: disable=missing-function-docstring
# pylint: disable=missing-module-docstring
from unittest.mock import patch, mock_open
import pytest
from src.self_defined_exception import SignalNotFoundError


def test_get_signal_title_with_valid_identifier(yaml_parser_instance):
    assert yaml_parser_instance.get_signal_title("11") == "ECU Reset"


def test_get_signal_title_with_invalid_identifier(yaml_parser_instance):
    with pytest.raises(SignalNotFoundError):
        yaml_parser_instance.get_signal_title("99")


VALID_JSON_DATA_1 = '{"json" : "This is a JSON"}'
PARSED_JSON_DATA_1 = {"json": "This is a JSON"}
VALID_JSON_DATA_2 = '{"json" : "This is a JSON 2"}'
PARSED_JSON_DATA_2 = {"json": "This is a JSON 2"}
VALID_JSON_DATA_3 = '{"json" : "This is a JSON 3"}'
PARSED_JSON_DATA_3 = {"json": "This is a JSON 3"}


@pytest.mark.parametrize("item, expected_result", [
    (VALID_JSON_DATA_1, PARSED_JSON_DATA_1),
    (VALID_JSON_DATA_2, PARSED_JSON_DATA_2),
    (VALID_JSON_DATA_3, PARSED_JSON_DATA_3),
])
def test_load_file(item, expected_result, yaml_parser_instance):
    with patch("builtins.open", mock_open(read_data=item)):
        yaml_parser_instance.load_file("path/to/json/file")
        assert yaml_parser_instance.data == expected_result
