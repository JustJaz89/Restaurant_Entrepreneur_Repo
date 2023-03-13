class Franchise:
    def __init__(self, location_number):
        self.location_number = location_number

    def place_order(self):
        self.ask_for_order = input(f"""What are you ordering?
        Type '1' for pizza, '2' for pasta, '3' for salad. """)

# location_number(int)
        
# OrderFactory.create_order()
# logger.log_transaction()