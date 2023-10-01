
from ..utils import handle_response
import requests

class Customer:
    BASE_URL = 'https://stage-api.ioka.kz/v2/customers'  # Replace with the actual base URL

    def __init__(self, api_key=None):
        self.api_key = api_key

    def get_customers(self, limit=10, page=1, to_dt=None, from_dt=None, date_category=None,
                      customer_id=None, external_id=None, status=None):
        headers = {'Authorization': f'Bearer {self.api_key}'}
        params = {
            "limit": limit,
            "page": page,
            "to_dt": to_dt,
            "from_dt": from_dt,
            "date_category": date_category,
            "customer_id": customer_id,
            "external_id": external_id,
            "status": status
        }
        response = requests.get(self.BASE_URL, headers=headers, params=params)
        return handle_response(response)

    def create_customer(self, external_id, email, phone, fingerprint=None, phone_check_date=None, channel=None):
        headers = {'Authorization': f'Bearer {self.api_key}', 'Content-Type': 'application/json'}
        payload = {
            "external_id": external_id,
            "email": email,
            "phone": phone,
            "fingerprint": fingerprint,
            "phone_check_date": phone_check_date,
            "channel": channel
        }
        response = requests.post(self.BASE_URL, headers=headers, json=payload)
        return handle_response(response)

    def get_customer_by_id(self, customer_access_token, customer_id):
        headers = {'Authorization': f'Bearer {customer_access_token}'}
        url = f'{self.BASE_URL}/{customer_id}'
        response = requests.get(url, headers=headers)
        return handle_response(response)

    def delete_customer_by_id(self, customer_id):
        headers = {'Authorization': f'Bearer {self.api_key}'}
        url = f'{self.BASE_URL}/{customer_id}'
        response = requests.delete(url, headers=headers)
        result = handle_response(response)
        if response.status_code == 204:
            return  # implicitly return None
        else:
            return result

    def get_customer_events(self, customer_id):
        url = f'{self.BASE_URL}/{customer_id}/events'
        response = requests.get(url)
        return handle_response(response)
