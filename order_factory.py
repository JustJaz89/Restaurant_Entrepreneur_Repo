from pizza import Pizza
from pasta import Pasta
from salad import Salad

class OrderFactory():

    def create_order(self, type):
        if type == "pizza":
            return Pizza()
        elif type == "pasta":
            return Pasta()
        elif type == "salad":
            return Salad()