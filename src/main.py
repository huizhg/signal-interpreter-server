"""main module"""
import argparse

from src.json_parser import JsonParser
from src.routes import signal_interpreter_app
from src.routes import parserFactory
import logging

from src.xml_parser import XmlParser
from src.yaml_parser import YamlParser

logger = logging.getLogger(__name__)


def parse_arguments():
    """parse the input arguments"""
    parser = argparse.ArgumentParser()
    parser.add_argument('--file_path')
    return parser.parse_args()


def select_parser(file_path):
    """select parser from factory"""
    file_path = str(file_path)
    index_of_dot = file_path.find('.')
    file_format = file_path[index_of_dot + 1: len(file_path)]
    parserFactory.set_signal_database_format(file_format)
    logger.debug("Set the signal database format: %s", file_format)
    parser = parserFactory.get_parser()
    return parser


def main():
    """entry function"""
    parserFactory.register_parser("xml", XmlParser)
    parserFactory.register_parser("json", JsonParser)
    parserFactory.register_parser("yaml", YamlParser)
    args = parse_arguments()
    file_path = args.file_path
    parser = select_parser(file_path)
    parser.load_file(file_path)
    logger.info("Load database from:  %s", file_path)
    signal_interpreter_app.run()


def init():
    """start the program"""
    if __name__ == "__main__":
        main()


init()
