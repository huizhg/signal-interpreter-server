"""routes module"""
from flask import Flask, request, jsonify
from src.json_parser import JsonParser
from flask import abort
from src.self_defined_exception import SignalNotFoundError
import logging
logger = logging.getLogger(__name__)

json_parser = JsonParser()
signal_interpreter_app = Flask(__name__)


@signal_interpreter_app.route("/", methods=["POST"])
def interpret_signal():
    """interpret the signal"""
    data = request.get_json()
    json_parser.data = data
    try:
        signal_title = json_parser.get_signal_title(data["signal"])
    except SignalNotFoundError as err:
        logger.exception("Signal not found exception occured %s", err)
        abort(404, description="Signal not found")
    return jsonify(signal_title)
