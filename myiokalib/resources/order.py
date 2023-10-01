
import requests
from ..utils import handle_response


class Order:
    BASE_URL = 'https://api.ioka.com/v2/orders'

    def __init__(self, api_key=None):
        self.api_key = api_key


    def create(self, amount, currency="KZT", capture_method="AUTO", external_id=None,
               description=None, mcc=None, extra_info=None, attempts=10, due_date=None,
               customer_id=None, card_id=None, back_url=None, success_url=None,
               failure_url=None, template=None):

        headers = {
            'Authorization': f'Bearer {self.api_key}',
            'Content-Type': 'application/json'
        }

        payload = {
            "amount": amount,
            "currency": currency,
            "capture_method": capture_method,
            "external_id": external_id,
            "description": description,
            "mcc": mcc,
            "extra_info": extra_info,
            "attempts": attempts,
            "due_date": due_date,
            "customer_id": customer_id,
            "card_id": card_id,
            "back_url": back_url,
            "success_url": success_url,
            "failure_url": failure_url,
            "template": template
        }

        response = requests.post(self.BASE_URL, headers=headers, json=payload)
        return handle_response(response)

    def get_orders(self, page=1, limit=10, to_dt=None, from_dt=None, date_category=None,
                   order_id=None, external_id=None, order_status=None, amount_category=None,
                   fixed_amount=None, min_amount=None, max_amount=None):
        headers = {
            'Authorization': f'Bearer {self.api_key}'
        }

        params = {
            "page": page,
            "limit": limit,
            "to_dt": to_dt,
            "from_dt": from_dt,
            "date_category": date_category,
            "order_id": order_id,
            "external_id": external_id,
            "order_status": order_status,
            "amount_category": amount_category,
            "fixed_amount": fixed_amount,
            "min_amount": min_amount,
            "max_amount": max_amount
        }

        response = requests.get(self.BASE_URL, headers=headers, params=params)
        return handle_response(response)

    def get_order_by_id(self, order_id):


        headers = {
            'Authorization': f'Bearer {self.api_key}'
        }

        url = f'{self.BASE_URL}/{order_id}'
        response = requests.get(url, headers=headers)
        return handle_response(response, order_id)
    def update_order_by_id(self, order_id, amount):

        headers = {
            'Authorization': f'Bearer {self.api_key}',
            'Content-Type': 'application/json'
        }

        payload = {
            "amount": amount
        }

        url = f'{self.BASE_URL}/{order_id}'
        response = requests.patch(url, headers=headers, json=payload)
        return handle_response(response, order_id)

    def cancel_order(self, order_id, reason):

        headers = {
            'Authorization': f'Bearer {self.api_key}',
            'Content-Type': 'application/json'
        }

        payload = {
            "reason": reason
        }

        url = f'{self.BASE_URL}/{order_id}/cancel'
        response = requests.post(url, headers=headers, json=payload)
        return handle_response(response, order_id)

    def get_receipt(self, order_id):

        headers = {
            'Authorization': f'Bearer {self.api_key}'
        }

        url = f'{self.BASE_URL}/{order_id}/receipt'
        response = requests.get(url, headers=headers)
        return handle_response(response, order_id)



