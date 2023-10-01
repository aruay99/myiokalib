# tests/test_order.py
import pytest
import responses
from myiokalib.resources.order import Order
from myiokalib.exceptions import InvalidRequestError, IokaAPIError, NotFoundError

@responses.activate
def test_order_creation_success():
    responses.add(
        responses.POST,
        'https://api.ioka.com/v2/orders',
        json={'order_id': '12345'},
        status=201
    )

    order = Order()
    response = order.create(api_key='test_api_key', amount=100)
    assert response == {'order_id': '12345'}

@responses.activate
def test_order_creation_invalid_request():
    responses.add(
        responses.POST,
        'https://api.ioka.com/v2/orders',
        json={'error_message': 'Invalid request'},
        status=400
    )

    order = Order()
    with pytest.raises(InvalidRequestError, match='Invalid request'):
        order.create(api_key='test_api_key', amount=100)

@responses.activate
def test_order_creation_api_error():
    responses.add(
        responses.POST,
        'https://api.ioka.com/v2/orders',
        status=500
    )

    order = Order()
    with pytest.raises(IokaAPIError, match='An error occurred: HTTP 500'):
        order.create(api_key='test_api_key', amount=100)

@responses.activate
def test_get_orders_success():
    responses.add(
        responses.GET,
        'https://api.ioka.com/v2/orders',
        json=[
            {
                "created_at": "string",
                "shop_id": "string",
                "id": "string",
                "status": "EXPIRED",
                "amount": 0,
                "currency": "KZT",
                "capture_method": "AUTO",
                "external_id": "string",
                "description": "string",
                "extra_info": {},
                "mcc": "string",
                "acquirer": "string",
                "customer_id": "string",
                "card_id": "string",
                "attempts": 50,
                "due_date": "string",
                "checkout_url": "http://example.com"
            }
        ],
        status=200
    )

    order = Order()
    response = order.get_orders(api_key='test_api_key', page=1, limit=10)
    assert response == [
        {
            "created_at": "string",
            "shop_id": "string",
            "id": "string",
            "status": "EXPIRED",
            "amount": 0,
            "currency": "KZT",
            "capture_method": "AUTO",
            "external_id": "string",
            "description": "string",
            "extra_info": {},
            "mcc": "string",
            "acquirer": "string",
            "customer_id": "string",
            "card_id": "string",
            "attempts": 50,
            "due_date": "string",
            "checkout_url": "http://example.com"
        }
    ]

@responses.activate
def test_get_orders_invalid_request():
    responses.add(
        responses.GET,
        'https://api.ioka.com/v2/orders',
        json={'error_message': 'Invalid request'},
        status=400
    )

    order = Order()
    with pytest.raises(InvalidRequestError, match='Invalid request'):
        order.get_orders(api_key='test_api_key', page=1, limit=10)

@responses.activate
def test_get_orders_api_error():
    responses.add(
        responses.GET,
        'https://api.ioka.com/v2/orders',
        status=500
    )

    order = Order()
    with pytest.raises(IokaAPIError, match='An error occurred: HTTP 500'):
        order.get_orders(api_key='test_api_key', page=1, limit=10)

@responses.activate
def test_get_order_by_id_success():
    responses.add(
        responses.GET,
        'https://api.ioka.com/v2/orders/12345',
        json={
            "id": "12345",
            "status": "EXPIRED",
            # ... other fields ...
        },
        status=200
    )

    order = Order()
    response = order.get_order_by_id(api_key='test_api_key', order_id='12345')
    assert response == {
        "id": "12345",
        "status": "EXPIRED",
        # ... other fields ...
    }

@responses.activate
def test_get_order_by_id_not_found():
    responses.add(
        responses.GET,
        'https://api.ioka.com/v2/orders/12345',
        status=404
    )

    order = Order()
    with pytest.raises(NotFoundError, match='Order with ID 12345 not found.'):
        order.get_order_by_id(api_key='test_api_key', order_id='12345')

@responses.activate
def test_update_order_by_id():
    # Mock the API response
    responses.add(
        responses.PATCH,
        'https://api.ioka.com/v2/orders/order_id',
        json={'id': 'order_id', 'amount': 50000},
        status=200
    )

    order = Order()
    updated_order_data = order.update_order_by_id(api_key='your_api_key', order_id='order_id', amount=50000)

    assert updated_order_data == {'id': 'order_id', 'amount': 50000}

@responses.activate
def test_update_order_by_id_not_found():
    # Mock the API response for order not found
    responses.add(
        responses.PATCH,
        'https://api.ioka.com/v2/orders/non_existent_order_id',
        json={'error_message': 'Order not found'},
        status=404
    )

    order = Order()
    with pytest.raises(NotFoundError, match='Order with ID non_existent_order_id not found.'):
        order.update_order_by_id(api_key='your_api_key', order_id='non_existent_order_id', amount=50000)

@responses.activate
def test_update_order_by_id_invalid_request():
    # Mock the API response for invalid request
    responses.add(
        responses.PATCH,
        'https://api.ioka.com/v2/orders/order_id',
        json={'error_message': 'Invalid amount'},
        status=400
    )

    order = Order()
    with pytest.raises(InvalidRequestError, match='Invalid amount'):
        order.update_order_by_id(api_key='your_api_key', order_id='order_id', amount=-50000)

@responses.activate
def test_cancel_order():
    # Mock the API response
    responses.add(
        responses.POST,
        'https://api.ioka.com/v2/orders/order_id/cancel',
        json={'id': 'order_id', 'status': 'CANCELED'},
        status=200
    )

    order = Order()
    canceled_order_data = order.cancel_order(api_key='your_api_key', order_id='order_id', reason='Customer requested cancelation')

    assert canceled_order_data == {'id': 'order_id', 'status': 'CANCELED'}

@responses.activate
def test_cancel_order_not_found():
    # Mock the API response for order not found
    responses.add(
        responses.POST,
        'https://api.ioka.com/v2/orders/non_existent_order_id/cancel',
        json={'error_message': 'Order not found'},
        status=404
    )

    order = Order()
    with pytest.raises(NotFoundError, match='Order with ID non_existent_order_id not found.'):
        order.cancel_order(api_key='your_api_key', order_id='non_existent_order_id', reason='Customer requested cancelation')

@responses.activate
def test_cancel_order_invalid_request():
    # Mock the API response for invalid request
    responses.add(
        responses.POST,
        'https://api.ioka.com/v2/orders/order_id/cancel',
        json={'error_message': 'Invalid reason'},
        status=400
    )

    order = Order()
    with pytest.raises(InvalidRequestError, match='Invalid reason'):
        order.cancel_order(api_key='your_api_key', order_id='order_id', reason='')

@responses.activate
def test_get_receipt():
    # Mock the API response
    responses.add(
        responses.GET,
        'https://api.ioka.com/v2/orders/order_id/receipt',
        json={'receipt_data': 'some_data'},
        status=200
    )

    order = Order()
    receipt_data = order.get_receipt(api_key='your_api_key', order_id='order_id')

    assert receipt_data == {'receipt_data': 'some_data'}

@responses.activate
def test_get_receipt_not_found():
    # Mock the API response for order not found
    responses.add(
        responses.GET,
        'https://api.ioka.com/v2/orders/non_existent_order_id/receipt',
        json={'error_message': 'Order not found'},
        status=404
    )

    order = Order()
    with pytest.raises(NotFoundError, match='Order with ID non_existent_order_id not found.'):
        order.get_receipt(api_key='your_api_key', order_id='non_existent_order_id')

