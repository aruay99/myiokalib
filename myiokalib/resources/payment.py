
from ..utils import handle_response
import requests
BASE_URL = 'https://api.example.com/v2'


class Payment:

    def get_payments(self, api_key, page=1, limit=10):
        url = f'{BASE_URL}/orders/payments'
        headers = {'Authorization': f'Bearer {api_key}'}
        params = {'page': page, 'limit': limit}
        response = requests.get(url, headers=headers, params=params)
        return handle_response(response)

    def create_card_payment(self, api_key, order_id, pan, exp, cvc):
        url = f'{BASE_URL}/orders/{order_id}/payments/card'
        headers = {'Authorization': f'Bearer {api_key}'}
        data = {
            'pan': pan,
            'exp': exp,
            'cvc': cvc
        }
        response = requests.post(url, headers=headers, json=data)
        return handle_response(response)

    def create_tool_payment(self, api_key, order_id, tool_type, apple_pay=None, google_pay=None):
        url = f'{BASE_URL}/orders/{order_id}/payments/tool'
        headers = {'Authorization': f'Bearer {api_key}'}
        data = {
            'tool_type': tool_type,
            'apple_pay': apple_pay,
            'google_pay': google_pay
        }
        response = requests.post(url, headers=headers, json=data)
        return handle_response(response)

    def get_payment_by_id(self, api_key, order_id, payment_id):
        url = f'{BASE_URL}/orders/{order_id}/payments/{payment_id}'
        headers = {'Authorization': f'Bearer {api_key}'}
        response = requests.get(url, headers=headers)
        return handle_response(response)