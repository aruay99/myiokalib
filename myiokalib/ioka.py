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
        self.card = Card(api_key)
        self.webhook = Webhook(api_key)