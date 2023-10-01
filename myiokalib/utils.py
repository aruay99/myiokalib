from .exceptions import (
    APIException,
    InvalidRequestError,
    UnauthorizedError,
    ForbiddenError,
    NotFoundError,
    IokaAPIError
)
def handle_response(response, order_id=None):
    if response.status_code == 200:
        return response.json()
    elif response.status_code == 400:
        # Check if 'error_message' key exists in the response JSON
        error_message = response.json().get('error_message', 'Unknown error')
        raise InvalidRequestError(error_message)
    elif response.status_code == 401:
        error_message = response.json().get('error_message', 'Unauthorized')
        raise UnauthorizedError(error_message)
    elif response.status_code == 403:
        error_message = response.json().get('error_message', 'Forbidden')
        raise ForbiddenError(error_message)
    elif response.status_code == 404:
        error_message = response.json().get('error_message', 'Not Found')
        raise NotFoundError(error_message)
    # Handle other status codes as needed
    else:
        raise IokaAPIError(f"HTTP Error {response.status_code}")

    return None  # Return None for cases where an error is raised

