from myiokalib.resources import Order, Payment, Customer, Card, Webhook
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