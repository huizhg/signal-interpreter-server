"""routes module"""
from flask import Flask, request, jsonify
from src.json_parser import JsonParser

json_parser = JsonParser()
signal_interpreter_app = Flask(__name__)


@signal_interpreter_app.route("/", methods=["POST"])
def interpret_signal():
    """interpret the signal"""
    data = request.get_json()
    # we do not want to overload the existing data in the json_parser
    # when we call get_signal_title from postman, we compare it with our existing "database"
    # json_parser.data = data 
    signal_title = json_parser.get_signal_title(data["signal"])
    return jsonify(signal_title)
