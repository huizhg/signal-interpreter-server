class SignalNotFoundError(Exception):
    """Signal not found in the database"""
    def __init__(self, message):
        self.message = message
