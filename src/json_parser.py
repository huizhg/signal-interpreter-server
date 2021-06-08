""" A Json Parser module"""

import json


class JsonParser:
    """A Json Parser class, used to load and parse json file"""
    def __init__(self):
        # class constructor
        self.data = None

    def load_file(self, file_path):
        """load json file"""
        with open(file_path) as file:
            self.data = json.load(file)

    def get_signal_title(self, identifier):
        """given identifier, search the signal title"""
        for service in self.data["services"]:
            if service["id"] == identifier:
                return service["title"]
        return None
