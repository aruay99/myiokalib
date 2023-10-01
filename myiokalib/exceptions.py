
class IokaBaseException(Exception):
    """Base exception class for Ioka library."""
    pass


class InvalidRequestError(IokaBaseException):
    """Exception raised for invalid requests (400 errors)."""
    def __init__(self, message="Invalid request"):
        super().__init__(message)


class UnauthorizedError(IokaBaseException):
    """Exception raised for unauthorized requests (401 errors)."""
    def __init__(self, message="Unauthorized"):
        super().__init__(message)


class ForbiddenError(IokaBaseException):
    """Exception raised for forbidden requests (403 errors)."""
    def __init__(self, message="Forbidden"):
        super().__init__(message)


class NotFoundError(IokaBaseException):
    """Exception raised for not found requests (404 errors)."""
    def __init__(self, message="Not found"):
        super().__init__(message)


class IokaAPIError(IokaBaseException):
    """Exception raised for other API errors."""
    def __init__(self, message="An error occurred"):
        super().__init__(message)

class APIException(Exception):
    pass

