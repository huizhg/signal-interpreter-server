from src.routes import signal_interpreter_app
from src.routes import json_parser
import argparse


def parse_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument('--file_path')
    return parser.parse_args()


def main():
    args = parse_arguments()
    file_path = args.file_path
    json_parser.load_file(file_path)
    signal_interpreter_app.run()


if __name__ == "__main__":
    main()
