from order import Order

class Salad(Order):

    def __init__(self):
        super().__init__("Salad")

    def dish_name(self, food):
        self.salad = food

    def price(self, int):
        self.salad = (8)