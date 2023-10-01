import pytest
import responses

from myiokalib.resources.payment import Payment

BASE_URL = 'https://stage-api.ioka.kz/v2/orders/'


@responses.activate
def test_get_payments():
    order_id = 1
    responses.add(responses.GET, f'{BASE_URL}/{order_id}/payments',
                  json={'data': 'test_data'}, status=200)
    payment = Payment()
    result = payment.get_payments()
    assert result == {'data': 'test_data'}


@responses.activate
def test_create_card_payment():
    order_id = 1
    responses.add(responses.POST, f'{BASE_URL}/{order_id}/payments/card',
                  json={'customer': 'created'}, status=201)

    # Create an instance of the Payment class
    payment = Payment()

    # Call the create_card_payment method on the instance
    result = payment.create_card_payment( order_id='order_id', pan='pan', exp='exp', cvc='cvc')


@responses.activate
def test_create_tool_payment():
    responses.add(responses.POST, f'{BASE_URL}/{order_id}/payments/tool',
                  json={'payment': 'created'}, status=201)
    payment = Payment()
    result = payment.create_tool_payment( order_id='order_id', tool_type='APPLE_PAY')
    assert result == {'payment': 'created'}


@responses.activate
def test_get_payment_by_id():
    responses.add(responses.GET, f'{BASE_URL}/order_id/payments/payment_id',
                  json={'payment': 'details'}, status=200)
    payment = Payment()
    result = payment.get_payment_by_id( order_id='order_id', payment_id='payment_id')
    assert result == {'payment': 'details'}
