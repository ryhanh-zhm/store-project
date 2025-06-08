from models.user import User

class Admin(User):
    def add_product(self, products_df):
        pid = input("Product ID: ")
        name = input("Name: ")
        price = float(input("Price: "))
        stock = int(input("Stock: "))
        products_df.loc[len(products_df)] = {'product_id': pid, 'name': name, 'price': price, 'stock': stock}
        print("Product added.")

    def remove_product(self, products_df):
        pid = input("Product ID to remove: ")
        products_df.drop(products_df[products_df.product_id == pid].index, inplace=True)
        print("Product removed.")