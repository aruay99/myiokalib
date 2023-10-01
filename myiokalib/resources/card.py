import requests
from ..utils import handle_response
from ..exceptions import APIException

BASE_URL = 'https://api.example.com/v2'


class Card:

    def create_binding(self, customer_id, pan, exp, cvc, holder=None, token=None):
        url = f'{BASE_URL}/customers/{customer_id}/bindings'
        headers = {'Authorization': f'Bearer {token}'}
        data = {
            'pan': pan,
            'exp': exp,
            'cvc': cvc,
            'holder': holder
        }
        response = requests.post(url, headers=headers, json=data)
        return handle_response(response)

    def get_cards(self, customer_id, token=None):
        url = f'{BASE_URL}/customers/{customer_id}/cards'
        headers = {'Authorization': f'Bearer {token}'}
        response = requests.get(url, headers=headers)
        return handle_response(response)

    def get_card_by_id(self, customer_id, card_id, token=None):
        url = f'{BASE_URL}/customers/{customer_id}/cards/{card_id}'
        headers = {'Authorization': f'Bearer {token}'}
        response = requests.get(url, headers=headers)
        return handle_response(response)

    def delete_card_by_id(self, customer_id, card_id, token=None):
        url = f'{BASE_URL}/customers/{customer_id}/cards/{card_id}'
        headers = {'Authorization': f'Bearer {token}'}
        response = requests.delete(url, headers=headers)
        return handle_response(response)
