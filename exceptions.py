class InvalidArgumentError(Exception):
    """This is a custom exception class that handles
     all ArgumentErrors, such as missing required argument,
     invalid argument or invalid currency code/symbol."""
    def __init__(self, message):
        self.message = message
        self.code = 400


class RequestError(Exception):
    """This is a custom exception class that handles
    all RequestErrors, such as TimeOut, Connection
    errors, etc."""

    def __init__(self, message, code):
        self.message = message
        self.code = code
