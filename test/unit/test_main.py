from argparse import ArgumentParser
from unittest.mock import patch
from src.main import parse_arguments, main, init
from src.json_parser import JsonParser
from src.routes import signal_interpreter_app


class MockArgs:
    file_path = "path/to/file"


@patch.object(ArgumentParser, "add_argument")
@patch.object(ArgumentParser, "parse_args", return_value=MockArgs)
def test_parse_arguments(mock_parse_args, mock_add_argument):
    assert parse_arguments() == MockArgs
    mock_parse_args.assert_called_once()
    mock_add_argument.assert_called_with("--file_path")


@patch.object(signal_interpreter_app, "run")
@patch.object(JsonParser, "load_file")
@patch("src.main.parse_arguments", return_value=MockArgs)
def test_main(mock_parse_arguments, mock_load_file, mock_run):
    main()
    mock_parse_arguments.assert_called_once()
    file_path = MockArgs.file_path
    mock_load_file.assert_called_with(file_path)
    mock_run.assert_called_once()


@patch("src.main.main")
@patch("src.main.__name__", "__main__")
def test_init(mock_main):
    init()
    mock_main.assert_called_once()
