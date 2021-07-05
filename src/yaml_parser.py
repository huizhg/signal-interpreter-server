""" A Json Parser module"""
from src.self_defined_exception import SignalNotFoundError
import logging
import yaml

logger = logging.getLogger(__name__)


class YamlParser:
    """A Json Parser class, used to load and parse json file"""
    def __init__(self):
        # class constructor
        self.data = None

    def load_file(self, file_path):
        """load json file"""
        with open(file_path, "r") as file:
            logger.info("load yaml file from: %s", file_path)
            dataMap = yaml.safe_load(file.read())
            self.data = dataMap

    def get_signal_title(self, identifier):
        """given identifier, search the signal title"""
        for service in self.data["services"]:
            if service["id"] == identifier:
                logger.info("get signal: %s", identifier)
                logger.debug("get title: %s", service["title"])
                return service["title"]
        raise SignalNotFoundError("Signal not found")
