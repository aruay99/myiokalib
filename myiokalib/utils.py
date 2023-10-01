from .exceptions import (
    APIException,
    InvalidRequestError,
    UnauthorizedError,
    ForbiddenError,
    NotFoundError
)

def handle_response(response, order_id=None):
    if response.status_code in [200, 201]:
        return response.json()
    elif response.status_code == 204:
        return "Successfully deleted"
    elif response.status_code == 400:
        raise InvalidRequestError(response.json()['error_message'])
    elif response.status_code == 401:
        raise UnauthorizedError(response.json()['error_message'])
    elif response.status_code == 403:
        raise ForbiddenError(response.json()['error_message'])
    elif response.status_code == 404:
        if order_id:
            raise NotFoundError(f"Order with ID {order_id} not found.")
        else:
            raise NotFoundError(response.json()['error_message'])
    else:
        raise APIException(f"An error occurred: HTTP {response.status_code}")
