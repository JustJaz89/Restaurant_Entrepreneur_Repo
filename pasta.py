from order import Order

class Pasta(Order):

    def __init__(self):
        super().__init__("Pasta")

    def dish_name(self, food):
        self.pasta = food

    def price(self, int):
        self.pasta = (12)