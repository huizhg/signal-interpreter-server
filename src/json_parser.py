""" A Json Parser module"""
from src.self_defined_exception import SignalNotFoundError
import logging
import json

logger = logging.getLogger(__name__)

class JsonParser:
    """A Json Parser class, used to load and parse json file"""
    def __init__(self):
        # class constructor
        self.data = None

    def load_file(self, file_path):
        """load json file"""
        with open(file_path) as file:
            logger.info("load json file from: %s", file_path)
            self.data = json.load(file)

    def get_signal_title(self, identifier):
        """given identifier, search the signal title"""
        for service in self.data["services"]:
            if service["id"] == identifier:
                logger.info("get signal: %s", identifier)
                logger.debug("get title: %s", service["title"])
                return service["title"]
        raise SignalNotFoundError("Signal not found")
