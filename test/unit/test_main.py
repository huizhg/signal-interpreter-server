# pylint: disable=missing-function-docstring
# pylint: disable=missing-module-docstring
from argparse import ArgumentParser
from unittest.mock import patch
from src.main import parse_arguments, main, init, select_parser
from src.json_parser import JsonParser
from src.routes import signal_interpreter_app
from src.parser_factory import ParserFactory


class MockArgs:
    file_path = "path/to/file"


class MockParser:
    pass


@patch.object(ArgumentParser, "add_argument")
@patch.object(ArgumentParser, "parse_args", return_value=MockArgs)
def test_parse_arguments(mock_parse_args, mock_add_argument):
    assert parse_arguments() == MockArgs
    mock_parse_args.assert_called_once()
    mock_add_argument.assert_called_with("--file_path")


@patch.object(ParserFactory, "get_parser", return_value=JsonParser)
@patch.object(ParserFactory, "set_signal_database_format")
def test_select_parser(mock_set_signal_database_format, mock_get_parser):
    select_parser("file_path.json")
    mock_set_signal_database_format.assert_called_with("json")
    mock_get_parser.assert_called_once()


@patch.object(signal_interpreter_app, "run")
@patch.object(JsonParser, "load_file")
@patch("src.main.select_parser", return_value=JsonParser)
@patch("src.main.parse_arguments", return_value=MockArgs)
@patch.object(ParserFactory, "register_parser")
def test_main(mock_register_parser, mock_parse_arguments, mock_select_parser, mock_load_file, mock_run):
    main()
    mock_register_parser.assert_called()
    mock_register_parser.assert_called()
    mock_register_parser.assert_called()
    mock_parse_arguments.assert_called_once()
    file_path = MockArgs.file_path
    mock_select_parser.assert_called_with(file_path)
    mock_load_file.assert_called_with(file_path)
    mock_run.assert_called_once()


@patch("src.main.main")
@patch("src.main.__name__", "__main__")
def test_init(mock_main):
    init()
    mock_main.assert_called_once()
