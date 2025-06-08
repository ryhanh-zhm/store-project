from models.user import User

class Customer(User):
    def __init__(self, username):
        super().__init__(username)
        self.cart = []

    def add_to_cart(self, product_id):
        self.cart.append(product_id)
        print(f"Product {product_id} added to cart.")

    def place_order(self, orders_df):
        if self.cart:
            new_order = {
                'order_id': len(orders_df) + 1,
                'username': self.username,
                'products': ','.join(self.cart),
                'status': 'placed'
            }
            orders_df.loc[len(orders_df)] = new_order
            self.cart.clear()
            print("Order placed successfully.")
        else:
            print("Your cart is empty.")