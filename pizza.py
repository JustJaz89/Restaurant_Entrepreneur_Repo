from order import Order

class Pizza(Order):
    def __init__(self):
        super().__init__("Pizza", 10)

example_one = Order("Order Name", 0)
example_two = Pizza()