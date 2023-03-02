from pizza import Pizza
from pasta import Pasta
from salad import Salad

class Order:

    def dish_name(self, food):
        self.pizza = food
        self.pasta = food
        self.salad = food

    def price(self, int):
        self.pizza = ("10")
        self.pasta = (12)
        self.salad = (8)