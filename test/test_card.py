import pytest
import responses
from myiokalib.resources.card import Card

BASE_URL = 'https://api.example.com/v2'


@responses.activate
def test_create_binding():
    responses.add(
        responses.POST,
        f'{BASE_URL}/customers/customer_id/bindings',
        json={'id': 'binding_id'},
        status=201
    )
    card = Card()
    result = card.create_binding(
        customer_id='customer_id',
        pan='pan',
        exp='exp',
        cvc='cvc',
        token='test_token'
    )
    assert result == {'id': 'binding_id'}


@responses.activate
def test_get_cards():
    responses.add(
        responses.GET,
        f'{BASE_URL}/customers/customer_id/cards',
        json=[{'id': 'card1'}, {'id': 'card2'}],
        status=200
    )
    card = Card()
    result = card.get_cards(
        customer_id='customer_id',
        token='test_token'
    )
    assert result == [{'id': 'card1'}, {'id': 'card2'}]

@responses.activate
def test_get_card_by_id():
    responses.add(
        responses.GET,
        f'{BASE_URL}/customers/customer_id/cards/card_id',
        json={'id': 'card_id', 'pan': '****1234'},
        status=200
    )
    card = Card()
    result = card.get_card_by_id(
        customer_id='customer_id',
        card_id='card_id',
        token='test_token'
    )
    assert result == {'id': 'card_id', 'pan': '****1234'}


@responses.activate
def test_delete_card_by_id():
    responses.add(
        responses.DELETE,
        f'{BASE_URL}/customers/customer_id/cards/card_id',
        status=204
    )
    card = Card()
    result = card.delete_card_by_id(
        customer_id='customer_id',
        card_id='card_id',
        token='test_token'
    )
    assert result == "Successfully deleted"


