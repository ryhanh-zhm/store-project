import pandas as pd
from models.customer import Customer
from models.admin import Admin
from utils.file_handler import load_data, save_data

class Store:
    def __init__(self):
        self.users = load_data("data/users.csv")
        self.products = load_data("data/products.csv")
        self.orders = load_data("data/orders.csv")
        self.current_user = None

    def main_menu(self):
        while True:
            print("\n1. Register/Login as Customer")
            print("2. Login as Admin")
            print("3. Exit")
            choice = input("Choose an option: ")
            if choice == "1":
                self.customer_login()
            elif choice == "2":
                self.admin_login()
            elif choice == "3":
                break

    def customer_login(self):
        username = input("Username: ")
        password = input("Password: ")
        user = self.users[(self.users.username == username) & (self.users.password == password) & (self.users.role == "customer")]
        if not user.empty:
            self.current_user = Customer(username)
            self.customer_menu()
        else:
            print("Login failed")

    def admin_login(self):
        username = input("Admin Username: ")
        password = input("Password: ")
        user = self.users[(self.users.username == username) & (self.users.password == password) & (self.users.role == "admin")]
        if not user.empty:
            self.current_user = Admin(username)
            self.admin_menu()
        else:
            print("Login failed")

    def customer_menu(self):
        while True:
            print("\n1. View Products")
            print("2. Add to Cart")
            print("3. Remove from Cart")
            print("4. Place Order")
            print("5. Back")
            choice = input("Choose an option: ")
            if choice == "1":
                print(self.products)
            elif choice == "2":
                product_id = input("Enter Product ID: ")
                quantity = int(input("Enter quantity: "))
                self.current_user.add_to_cart(product_id, quantity)
            elif choice == "3":
                product_id = input("Enter Product ID to remove: ")
                self.current_user.remove_from_cart(product_id)
            elif choice == "4":
                self.current_user.place_order(self.orders)
                save_data("data/orders.csv", self.orders)
            elif choice == "5":
                break

    def admin_menu(self):
        while True:
            print("\n1. Add Product")
            print("2. Remove Product")
            print("3. View Orders")
            print("4. Back")
            choice = input("Choose an option: ")
            if choice == "1":
                self.current_user.add_product(self.products)
                save_data("data/products.csv", self.products)
            elif choice == "2":
                self.current_user.remove_product(self.products)
                save_data("data/products.csv", self.products)
            elif choice == "3":
                print(self.orders)
            elif choice == "4":
                break