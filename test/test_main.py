from argparse import ArgumentParser
from unittest.mock import patch
from src.main import parse_arguments


class MockArgs:
    file_path = "path/to/file"


@patch.object(ArgumentParser, "add_argument")
@patch.object(ArgumentParser, "parse_args", return_value=MockArgs)
def test_main(mock_parse_args, mock_add_argument):
    assert parse_arguments() == MockArgs
    mock_parse_args.assert_called_once()
    mock_add_argument.assert_called_with("--file_path")
