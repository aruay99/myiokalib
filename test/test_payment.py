import pytest
import responses

from myiokalib.resources.payment import Payment

BASE_URL = 'https://api.example.com/v2'


@responses.activate
def test_get_payments():
    responses.add(responses.GET, f'{BASE_URL}/orders/payments',
                  json={'data': 'test_data'}, status=200)
    payment = Payment()
    result = payment.get_payments(api_key='test_api_key')
    assert result == {'data': 'test_data'}


@responses.activate
def test_create_card_payment():
    responses.add(responses.POST, f'{BASE_URL}/orders/order_id/payments/card',
                  json={'customer': 'created'}, status=201)

    # Create an instance of the Payment class
    payment = Payment()

    # Call the create_card_payment method on the instance
    result = payment.create_card_payment(api_key='test_api_key', order_id='order_id', pan='pan', exp='exp', cvc='cvc')


@responses.activate
def test_create_tool_payment():
    responses.add(responses.POST, f'{BASE_URL}/orders/order_id/payments/tool',
                  json={'payment': 'created'}, status=201)
    payment = Payment()
    result = payment.create_tool_payment(api_key='test_api_key', order_id='order_id', tool_type='APPLE_PAY')
    assert result == {'payment': 'created'}


@responses.activate
def test_get_payment_by_id():
    responses.add(responses.GET, f'{BASE_URL}/orders/order_id/payments/payment_id',
                  json={'payment': 'details'}, status=200)
    payment = Payment()
    result = payment.get_payment_by_id(api_key='test_api_key', order_id='order_id', payment_id='payment_id')
    assert result == {'payment': 'details'}
