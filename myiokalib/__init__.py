
from .ioka import IokaAPI
from .resources import Order, Payment, Customer,Card,Webhook

__all__ = ["IokaAPI", "Order", "Payment", "Customer", "Card", "Webhook"]

def init(api_key_value):
    global api_key
    api_key = api_key_value

