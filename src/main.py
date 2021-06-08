"""main module"""
import argparse
from src.routes import signal_interpreter_app
from src.routes import json_parser


def parse_arguments():
    """parse the input arguments"""
    parser = argparse.ArgumentParser()
    parser.add_argument('--file_path')
    return parser.parse_args()


def main():
    """entry function"""
    args = parse_arguments()
    file_path = args.file_path
    json_parser.load_file(file_path)
    signal_interpreter_app.run()


def init():
    if __name__ == "__main__":
        main()


init()
