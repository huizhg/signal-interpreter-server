# pylint: disable=missing-function-docstring
# pylint: disable=missing-module-docstring
# pylint: disable=line-too-long
from unittest.mock import patch, mock_open
from collections import OrderedDict
import pytest
from src.self_defined_exception import SignalNotFoundError


def test_load_file(xml_parser_instance):
    with patch('builtins.open', mock_open(read_data='<services><service id="11"><title>ECU Reset</title>'
                                                    '</service></services>')):
        xml_parser_instance.load_file('path/to/file')
        assert xml_parser_instance.data == {
            'services': OrderedDict([('service', OrderedDict([('@id', '11'), ('title', 'ECU Reset')]))])
        }


def test_get_signal_title_with_valid_identifier(xml_parser_instance):

    assert xml_parser_instance.get_signal_title("11") == "ECU Reset"


def test_get_signal_title_with_invalid_identifier(xml_parser_instance):
    with pytest.raises(SignalNotFoundError):
        xml_parser_instance.get_signal_title("99")
