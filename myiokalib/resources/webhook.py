import requests
from ..utils import handle_response
from ..exceptions import APIException

BASE_URL = 'https://stage-api.ioka.kz/v2/webhooks'


class Webhook:
    def __init__(self, api_key=None):
        self.api_key = api_key
    def get_webhooks(self):
        url = f'{BASE_URL}/webhooks'
        headers = {'Authorization': f'Bearer {self.api_key}'}
        response = requests.get(url, headers=headers)
        return handle_response(response)

    def create_webhook(self, url, events):
        url = f'{BASE_URL}/webhooks'
        headers = {'Authorization': f'Bearer {self.api_key}'}
        data = {
            'url': url,
            'events': events
        }
        response = requests.post(url, headers=headers, json=data)
        return handle_response(response)

    def get_webhook_by_id(self, webhook_id):
        url = f'{BASE_URL}/webhooks/{webhook_id}'
        headers = {'Authorization': f'Bearer {self.api_key}'}
        response = requests.get(url, headers=headers)
        return handle_response(response)

    def delete_webhook_by_id(self, webhook_id):
        url = f'{BASE_URL}/webhooks/{webhook_id}'
        headers = {'Authorization': f'Bearer {self.api_key}'}
        response = requests.delete(url, headers=headers)
        return handle_response(response)

    def update_webhook_by_id(self, webhook_id, url, events):
        url = f'{BASE_URL}/webhooks/{webhook_id}'
        headers = {'Authorization': f'Bearer {self.api_key}'}
        data = {
            'url': url,
            'events': events
        }
        response = requests.patch(url, headers=headers, json=data)
        return handle_response(response)
