from ..utils import handle_response
import requests
from ..ioka import IokaAPI
import datetime


class Order:
    BASE_URL = 'https://stage-api.ioka.kz/v2/orders'

    def __init__(self, api_key=None):
        self.api_key = IokaAPI.load_api_key()

    def create(self, amount: int, currency="KZT", capture_method="AUTO", external_id=None,
               description=None, mcc=None, extra_info={ }, attempts=10, due_date=None,
               customer_id=None, card_id=None, back_url=None, success_url=None,
               failure_url=None, template=None):
        headers = {
            'API-KEY': self.api_key,
            'Content-Type': 'application/json'
        }

        if due_date is None:
            # You can set a default value like 7 days from now
            due_date = datetime.datetime.now() + datetime.timedelta(days=7)

        payload = {
            "amount": int(amount),
            "currency": currency,
            "capture_method": capture_method,
            "external_id": external_id,
            "description": description,
            "mcc": mcc,
            "extra_info": extra_info,
            "attempts": attempts,
            "customer_id": customer_id,
            "card_id": card_id,
            "back_url": back_url,
            "due_date": due_date.isoformat() if due_date else None,
            "success_url": success_url,
            "failure_url": failure_url,
            "template": template
        }


        response = requests.post(self.BASE_URL, headers=headers, json=payload)
        return response



    def get_orders(self, page=1, limit=10, to_dt=None, from_dt=None, date_category=None,
                   order_id=None, external_id=None, order_status=None, amount_category=None,
                   fixed_amount=None, min_amount=None, max_amount=None):
        headers = {
            'API-KEY': self.api_key,
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
            'API-KEY': self.api_key,
        }

        url = f'{self.BASE_URL}/{order_id}'
        response = requests.get(url, headers=headers)
        return handle_response(response, order_id)

    def update_order_by_id(self, order_id, amount):
        headers = {
            'API-KEY': self.api_key,
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
            'API-KEY': self.api_key,
            'Content-Type': 'application/json'
        }

        payload = {
            "reason": reason
        }

        url = f'{self.BASE_URL}/{order_id}/cancel'
        response = requests.post(url, headers=headers, json=payload)
        return handle_response(response, order_id)


