import requests
from ..utils import handle_response
from ..exceptions import APIException

BASE_URL = 'https://stage-api.ioka.kz/v2'
from ..ioka import IokaAPI


class Card:
    def __init__(self, api_key=None):
        self.api_key = IokaAPI.load_api_key()

    def get_cards(self, customer_id):
        url = f'{BASE_URL}/customers/{customer_id}/cards'
        headers = {'API_KEY': self.api_key}
        print(f"API Key: {self.api_key}")
        print(f"Request URL: {url}")
        response = requests.get(url, headers=headers)
        return handle_response(response)

    def get_card_by_id(self, customer_id, card_id):
        url = f'{BASE_URL}/customers/{customer_id}/cards/{card_id}'
        headers = {'API_KEY': self.api_key}
        response = requests.get(url, headers=headers)
        return handle_response(response)

    def delete_card_by_id(self, customer_id, card_id):
        url = f'{BASE_URL}/customers/{customer_id}/cards/{card_id}'
        headers = {'API_KEY': self.api_key}
        response = requests.delete(url, headers=headers)
        return handle_response(response)
