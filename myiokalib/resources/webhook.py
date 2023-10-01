import requests
from ..utils import handle_response
from ..exceptions import APIException

BASE_URL = 'https://api.example.com/v2'


class Webhook:
    def get_webhooks(self, api_key):
        url = f'{BASE_URL}/webhooks'
        headers = {'Authorization': f'Bearer {api_key}'}
        response = requests.get(url, headers=headers)
        return handle_response(response)

    def create_webhook(self, api_key, url, events):
        url = f'{BASE_URL}/webhooks'
        headers = {'Authorization': f'Bearer {api_key}'}
        data = {
            'url': url,
            'events': events
        }
        response = requests.post(url, headers=headers, json=data)
        return handle_response(response)

    def get_webhook_by_id(self, api_key, webhook_id):
        url = f'{BASE_URL}/webhooks/{webhook_id}'
        headers = {'Authorization': f'Bearer {api_key}'}
        response = requests.get(url, headers=headers)
        return handle_response(response)

    def delete_webhook_by_id(self, api_key, webhook_id):
        url = f'{BASE_URL}/webhooks/{webhook_id}'
        headers = {'Authorization': f'Bearer {api_key}'}
        response = requests.delete(url, headers=headers)
        return handle_response(response)

    def update_webhook_by_id(self, api_key, webhook_id, url, events):
        url = f'{BASE_URL}/webhooks/{webhook_id}'
        headers = {'Authorization': f'Bearer {api_key}'}
        data = {
            'url': url,
            'events': events
        }
        response = requests.patch(url, headers=headers, json=data)
        return handle_response(response)
