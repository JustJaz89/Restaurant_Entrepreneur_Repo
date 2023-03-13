from pizza import Pizza
from pasta import Pasta
from salad import Salad

class Order:
    def __init__(self, dish_name, price):
        self.dish_name = dish_name
        self.price = price