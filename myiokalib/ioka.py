from myiokalib.resources.customer import Customer
from myiokalib.resources.order import Order
from myiokalib.resources.card import Card
from myiokalib.resources.payment import Payment
from myiokalib.resources.webhook import Webhook
# Create a variable to store the API key
api_key = None

# Function to initialize the API key
def init(api_key_value):
    global api_key
    api_key = api_key_value

# Define the classes and functions for user interaction
class IokaAPI:
    def __init__(self, api_key):
        self.api_key = api_key
        self.order = Order(api_key)
        self.payment = Payment(api_key)
        self.customer = Customer(api_key)
        self.card = Card()
        self.webhook = Webhook(api_key)

    def create_binding(self, customer_id, pan, exp, cvc, holder=None):
        return self.card.create_binding(customer_id, pan, exp, cvc, holder, token=self.api_key)

    def get_cards(self, customer_id):
        return self.card.get_cards(customer_id, token=self.api_key)

    def get_card_by_id(self, customer_id, card_id):
        return self.card.get_card_by_id(customer_id, card_id, token=self.api_key)

    def delete_card_by_id(self, customer_id, card_id):
        return self.card.delete_card_by_id(customer_id, card_id, token=self.api_key)

    def get_customers(self, limit=10, page=1, to_dt=None, from_dt=None, date_category=None,
                      customer_id=None, external_id=None, status=None):
        return self.customer.get_customers(
            limit=limit, page=page, to_dt=to_dt, from_dt=from_dt,
            date_category=date_category, customer_id=customer_id,
            external_id=external_id, status=status, token=self.api_key
        )

    def create_customer(self, external_id, email, phone, fingerprint=None, phone_check_date=None, channel=None):
        return self.customer.create_customer(
            external_id, email, phone, fingerprint=fingerprint,
            phone_check_date=phone_check_date, channel=channel, token=self.api_key
        )

    def get_customer_by_id(self, customer_access_token, customer_id):
        return self.customer.get_customer_by_id(customer_access_token, customer_id)

    def delete_customer_by_id(self, customer_id):
        return self.customer.delete_customer_by_id(customer_id, token=self.api_key)

    def get_customer_events(self, customer_id):
        return self.customer.get_customer_events(customer_id)


    def create_order(self, amount, currency="KZT", capture_method="AUTO", external_id=None,
                    description=None, mcc=None, extra_info=None, attempts=10, due_date=None,
                    customer_id=None, card_id=None, back_url=None, success_url=None,
                    failure_url=None, template=None):
        return self.order.create(
            amount, currency=currency, capture_method=capture_method,
            external_id=external_id, description=description, mcc=mcc,
            extra_info=extra_info, attempts=attempts, due_date=due_date,
            customer_id=customer_id, card_id=card_id, back_url=back_url,
            success_url=success_url, failure_url=failure_url, template=template,
            token=self.api_key
        )

    def get_orders(self, page=1, limit=10, to_dt=None, from_dt=None, date_category=None,
                   order_id=None, external_id=None, order_status=None, amount_category=None,
                   fixed_amount=None, min_amount=None, max_amount=None):
        return self.order.get_orders(
            page=page, limit=limit, to_dt=to_dt, from_dt=from_dt,
            date_category=date_category, order_id=order_id,
            external_id=external_id, order_status=order_status,
            amount_category=amount_category, fixed_amount=fixed_amount,
            min_amount=min_amount, max_amount=max_amount, token=self.api_key
        )

    def get_order_by_id(self, order_id):
        return self.order.get_order_by_id(order_id)

    def update_order_by_id(self, order_id, amount):
        return self.order.update_order_by_id(order_id, amount, token=self.api_key)

    def cancel_order(self, order_id, reason):
        return self.order.cancel_order(order_id, reason, token=self.api_key)

    def get_receipt(self, order_id):
        return self.order.get_receipt(order_id)

    def get_payments(self, page=1, limit=10):
        return self.payment.get_payments(page=page, limit=limit, token=self.api_key)

    def create_card_payment(self, order_id, pan, exp, cvc):
        return self.payment.create_card_payment(order_id, pan, exp, cvc, token=self.api_key)

    def create_tool_payment(self, order_id, tool_type, apple_pay=None, google_pay=None):
        return self.payment.create_tool_payment(order_id, tool_type, apple_pay, google_pay, token=self.api_key)

    def get_payment_by_id(self, order_id, payment_id):
        return self.payment.get_payment_by_id(order_id, payment_id)

    def get_webhooks(self):
        return self.webhook.get_webhooks(token=self.api_key)

    def create_webhook(self, url, events):
        return self.webhook.create_webhook(url, events, token=self.api_key)

    def get_webhook_by_id(self, webhook_id):
        return self.webhook.get_webhook_by_id(webhook_id, token=self.api_key)

    def delete_webhook_by_id(self, webhook_id):
        return self.webhook.delete_webhook_by_id(webhook_id, token=self.api_key)

    def update_webhook_by_id(self, webhook_id, url, events):
        return self.webhook.update_webhook_by_id(webhook_id, url, events, token=self.api_key)




