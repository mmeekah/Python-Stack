class Store:
    def __init__(self, name, items):
        self.name = name
        self.items = items


    def add_item(self, name, price):
        item = {"name": name, "price": price}
        self.items.append(item)


    def stock_price(self):
        return sum([item["price"] for item in self.items])
