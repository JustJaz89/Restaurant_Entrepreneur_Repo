from order import Order

class Pizza(Order):

    def __init__(self):
        super().__init__("Pizza")

    def dish_name(self, food):
        self.pizza = food

    def price(self, int):
        self.pizza = (10)