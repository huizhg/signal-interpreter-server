# pylint: disable=missing-function-docstring
# pylint: disable=missing-module-docstring, protected-access, missing-class-docstring
import pytest


class MockParser:  # pylint: disable=too-few-public-methods
    pass


def test_set_signal_database_format(parser_factory_instance):
    parser_factory_instance.set_signal_database_format("FORMAT")
    assert parser_factory_instance._signal_database_format == "FORMAT"


def test_register_format(parser_factory_instance):
    parser_factory_instance.register_parser("FORMAT", MockParser)
    assert isinstance(parser_factory_instance._parsers["FORMAT"], MockParser)


def test_get_parser(parser_factory_instance):
    parser_factory_instance._parsers["FORMAT"] = MockParser
    parser_factory_instance._signal_database_format = "FORMAT"
    assert parser_factory_instance.get_parser() == MockParser


def test_get_parser_with_invalid_format(parser_factory_instance):
    with pytest.raises(ValueError):
        parser_factory_instance.get_parser()
