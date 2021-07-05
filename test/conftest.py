""" Shared fixtures """
# pylint: disable=missing-function-docstring
import pytest
from src.routes import signal_interpreter_app
from src.parser_factory import ParserFactory
from src.json_parser import JsonParser
from src.xml_parser import XmlParser
from src.yaml_parser import YamlParser


@pytest.fixture
def signal_interpreter_app_instance():
    signal_interpreter_app.testing = True
    return signal_interpreter_app.test_client()


@pytest.fixture
def parser_factory_instance():
    return ParserFactory()


@pytest.fixture
def json_parser_instance():
    json_parser = JsonParser()
    json_parser.data = {"services": [{"title": "ECU Reset", "id": "11"}]}
    return json_parser


@pytest.fixture
def xml_parser_instance():
    xml_parser = XmlParser()
    xml_parser.data = {"services": {"service": [{"title": "ECU Reset", "@id": "11"}]}}
    return xml_parser


@pytest.fixture
def yaml_parser_instance():
    yaml_parser = YamlParser()
    yaml_parser.data = {"services": [{"title": "ECU Reset", "id": "11"}]}
    return yaml_parser
