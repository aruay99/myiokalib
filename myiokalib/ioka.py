from myiokalib.resources.customer import Customer
from myiokalib.resources.order import Order
from myiokalib.resources.card import Card
from myiokalib.resources.payment import Payment
from myiokalib.resources.webhook import Webhook
# Create a variable to store the API key
api_key = None






class IokaAPI:
    def __init__(self, api_key):
        self.api_key = api_key

def initialize_ioka(api_key):
    return IokaAPI(api_key)




