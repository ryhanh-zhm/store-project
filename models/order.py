class Order:
    def __init__(self, order_id, username, products, status="placed"):
        self.order_id = order_id
        self.username = username
        self.products = products  # List of (product_id, quantity)
        self.status = status

    def __str__(self):
        items = ", ".join([f"{pid} x{qty}" for pid, qty in self.products])
        return f"Order #{self.order_id} by {self.username}: {items} [{self.status}]"