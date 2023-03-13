from pizza import Pizza

class Logger:
    def __init__(self):
        self.transaction_count = 0
        self.daily_sales = 0

    def log_transaction(self, customer_order, store_number):
        self.transaction_count += 1
        doc = open("log.txt", "a")
        for item in customer_order:
            self.daily_sales += item.price

            doc.write(f"""\nPurchase at New Yorker Pizza store #{store_number}
            Current transaction count: {self.transaction_count}
            Dish Ordered: {item.dish_name}
            Item Price: {item.price}
            Combined Daily Income: {self.daily_sales}\n\n""")
        doc.close()

customer_order = [Pizza(), Pizza(), Pizza()]
log = Logger()
store_number = 777

log.log_transaction(customer_order, store_number)