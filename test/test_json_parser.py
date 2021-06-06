from unittest.mock import patch
from src.json_parser import JsonParser


def test_get_signal_title():
    json_parser = JsonParser()
    json_parser.data = {"services": [{"title": "ECU Reset", "id": "11"}]}
    assert json_parser.get_signal_title("11") == "ECU Reset"
