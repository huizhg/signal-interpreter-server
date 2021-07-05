""" A Json Parser module"""
# pylint: disable=missing-function-docstring
from src.self_defined_exception import SignalNotFoundError
import logging
import xmltodict
import xml.etree.ElementTree as ET

logger = logging.getLogger(__name__)


class XmlParser:
    """A Json Parser class, used to load and parse json file"""

    def __init__(self):
        # class constructor
        self.data = None

    def load_file(self, file_path):
        """load json file"""
        logger.info("load xml file from: %s", file_path)
        tree = ET.parse(file_path)
        data = tree.getroot()
        xml_string = ET.tostring(data, encoding="utf-8", method="xml")
        data = xmltodict.parse(xml_string)
        data = dict(data)
        self.data = data

    def get_signal_title(self, identifier):
        """given identifier, search the signal title"""
        for services in self.data["services"].values():
            for service in services:
                if service["@id"] == identifier:
                    return service["title"]
        raise SignalNotFoundError("Signal not found")
