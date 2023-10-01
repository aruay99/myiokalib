
import pytest
import responses
from myiokalib.resources.customer import Customer

BASE_URL = 'https://api.ioka.com/v2/customers'

@responses.activate
def test_get_customers():
    responses.add(responses.GET, BASE_URL, json={'data': 'test_data'}, status=200)
    customer = Customer()
    data = customer.get_customers(api_key='test_api_key', limit=10, page=1)
    assert data['data'] == 'test_data'

@responses.activate
def test_create_customer():
    responses.add(responses.POST, BASE_URL, json={'customer': 'created'}, status=201)
    customer = Customer()
    data = customer.create_customer(api_key='test_api_key', external_id='external_id', email='email@example.com', phone='1234567890')
    assert data['customer'] == 'created'

@responses.activate
def test_get_customer_by_id():
    responses.add(responses.GET, f'{BASE_URL}/customer_id', json={'customer': 'details'}, status=200)
    customer = Customer()
    data = customer.get_customer_by_id(customer_access_token='test_token', customer_id='customer_id')
    assert data['customer'] == 'details'

@responses.activate
def test_delete_customer_by_id():
    responses.add(responses.DELETE, f'{BASE_URL}/customer_id', status=204)
    customer = Customer()
    response = customer.delete_customer_by_id(api_key='test_api_key', customer_id='customer_id')
    assert response is None

@responses.activate
def test_get_customer_events():
    responses.add(responses.GET, f'{BASE_URL}/customer_id/events', json={'events': 'list'}, status=200)
    customer = Customer()
    data = customer.get_customer_events(customer_id='customer_id')
    assert data['events'] == 'list'
