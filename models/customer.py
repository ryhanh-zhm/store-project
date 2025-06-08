from models.user import User

class Customer(User):
    def __init__(self, username):
        super().__init__(username)
        self.cart = {}  # key: product_id, value: quantity

    def add_to_cart(self, product_id, quantity):
        if product_id in self.cart:
            self.cart[product_id] += quantity
        else:
            self.cart[product_id] = quantity
        print(f"Added {quantity} of product {product_id} to cart.")

    def remove_from_cart(self, product_id):
        if product_id in self.cart:
            del self.cart[product_id]
            print(f"Product {product_id} removed from cart.")
        else:
            print("Product not found in cart.")

    def place_order(self, orders_df):
        if self.cart:
            product_list = [f"{pid}:{qty}" for pid, qty in self.cart.items()]
            new_order = {
                'order_id': len(orders_df) + 1,
                'username': self.username,
                'products': ';'.join(product_list),
                'status': 'placed'
            }
            orders_df.loc[len(orders_df)] = new_order
            self.cart.clear()
            print("Order placed successfully.")
        else:
            print("Your cart is empty.")