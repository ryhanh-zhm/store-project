class Cart:
    def __init__(self):
        self.items = {} 

    def add(self, product_id, quantity):
        self.items[product_id] = self.items.get(product_id, 0) + quantity

    def remove(self, product_id):
        if product_id in self.items:
            del self.items[product_id]

    def clear(self):
        self.items.clear()

    def __str__(self):
        return str(self.items)