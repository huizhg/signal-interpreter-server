"""ParserFactory class"""
class ParserFactory:
    def __init__(self):
        self._parsers = {}
        self._signal_database_format = None

    def set_signal_database_format(self, signal_database_format):
        """ set signal database format"""
        self._signal_database_format = signal_database_format

    def register_parser(self, file_format, parser):
        """register parser to the factory"""
        self._parsers[file_format] = parser()

    def get_parser(self):
        """get parser"""
        parser = self._parsers.get(self._signal_database_format)
        if not parser:
            raise ValueError(self._signal_database_format)
        return parser
