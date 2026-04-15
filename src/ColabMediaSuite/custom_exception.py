
class InvalidURLException(Exception):
    """Raised when a URL is invalid or unreachable."""
    
    def __init__(self, message=None):
        if message is None:
            message = "The provided URL is invalid."
        super().__init__(message)