
from ..utils import handle_response
import requests
from myiokalib.ioka import IokaAPI
BASE_URL = 'https://stage-api.ioka.kz/v2/orders'


class Payment:
    def __init__(self, api_key=None):
        self.api_key = IokaAPI.load_api_key()


    def create_card_payment(self, order_id, pan, exp, cvc):
        url = f'{BASE_URL}/{order_id}/payments/card'
        headers = {
            'Content-Type': 'application/json'
        }
        data = {
            'pan': pan,
            'exp': exp,
            'cvc': cvc
        }
        response = requests.post(url, headers=headers, json=data)

        if response.status_code == 201:
            return response.json()
        else:
            return handle_response(response)  # Handle other non-successful responses


    def get_payment_by_id(self, order_id, payment_id):
        url = f'{BASE_URL}/{order_id}/payments/{payment_id}'
        headers = {'API-KEY': self.api_key}
        response = requests.get(url, headers=headers)
        return handle_response(response)