# pylint: disable=missing-function-docstring
# pylint: disable=missing-module-docstring
from unittest.mock import patch, mock_open
import pytest
from src.json_parser import JsonParser
from src.self_defined_exception import SignalNotFoundError


@pytest.mark.parametrize("item, expected_result", [
    ("11", "ECU Reset"),
    ("3E", "Tester Present"),
    ("27", "Security Access"),
    ("34", "Request Download"),

])
def test_get_signal_title(item, expected_result):
    json_parser = JsonParser()
    json_parser.data = {"services": [{"title": "ECU Reset", "id": "11"}, {"title": "Tester Present", "id": "3E"},
                                     {"title": "Security Access", "id": "27"},
                                     {"title": "Request Download", "id": "34"}]}
    assert json_parser.get_signal_title(item) == expected_result


def test_get_signal_title_with_invalid_identifier(json_parser_instance):
    with pytest.raises(SignalNotFoundError):
        json_parser_instance.get_signal_title("99")


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
def test_load_file(item, expected_result):
    with patch("builtins.open", mock_open(read_data=item)):
        json_parser = JsonParser()
        json_parser.load_file("path/to/json/file")
        assert json_parser.data == expected_result
