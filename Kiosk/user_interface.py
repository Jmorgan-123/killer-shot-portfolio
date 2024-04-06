import json
from datetime import datetime

class UserInterface:
    def __init__(self, business_logic):
        self.business_logic = business_logic

    def display_menu(self):
        print("\nBusiness Management System\n")
        print("1. Add Product")
        print("2. Update Product")
        print("3. Record Transaction")
        print("4. View Transactions")
        print("5. Generate Balance Sheet")
        print("6. Exit")

    def add_product(self):
        name = input("Enter product name: ")
        buying_price = float(input("Enter buying price: "))
        selling_price = float(input("Enter selling price: "))
        quantity = int(input("Enter quantity: "))
        product = {
            "name": name,
            "buying_price": buying_price,
            "selling_price": selling_price,
            "quantity": quantity
        }
        self.business_logic.add_product(product)
        print("Product added successfully.")

    def update_product(self):
        product_id = int(input("Enter product ID: "))
        product_list = self.business_logic.get_product_list()
        if product_id >= 0 and product_id < len(product_list):
            updated_product = product_list[product_id]
            updated_product["buying_price"] = float(input("Enter new buying price: "))
            updated_product["selling_price"] = float(input("Enter new selling price: "))
            updated_product["quantity"] = int(input("Enter new quantity: "))
            self.business_logic.save_data()
            print("Product updated successfully.")
        else:
            print("Invalid product ID.")

    def record_transaction(self):
        item = input("Enter item name: ")
        quantity = int(input("Enter quantity: "))
        price = float(input("Enter price: "))
        transaction_type = input("Enter transaction type (Sale/Expense): ").lower()
        if transaction_type in ["sale", "expense"]:
            transaction = {
                "item": item,
                "quantity": quantity,
                "price": price,
                "type": transaction_type,
                "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            }
            self.business_logic.add_transaction(transaction)
            print("Transaction recorded successfully.")
        else:
            print("Invalid transaction type.")

    def view_transactions(self):
        transactions = self.business_logic.get_transactions()
        print("Transactions:")
        for transaction in transactions:
            print(f"Type: {transaction['type']}, Item: {transaction['item']}, "
                  f"Quantity: {transaction['quantity']}, Price: {transaction['price']}, "
                  f"Timestamp: {transaction['timestamp']}")

    def generate_balance_sheet(self):
        products = self.business_logic.get_product_list()
        transactions = self.business_logic.get_transactions()
        total_inventory_value = sum(product["buying_price"] * product["quantity"] for product in products)
        total_sales = sum(transaction["price"] * transaction["quantity"] for transaction in transactions if transaction["type"] == "sale")
        total_expenses = sum(transaction["price"] * transaction["quantity"] for transaction in transactions if transaction["type"] == "expense")
        total_profit = total_sales - total_expenses
        print(f"Total Inventory Value: ${total_inventory_value}")
        print(f"Total Sales: ${total_sales}")
        print(f"Total Expenses: ${total_expenses}")
        print(f"Total Profit: ${total_profit}")

    def start(self):
        while True:
            self.display_menu()
            choice = input("Enter your choice (1-6): ")
            if choice == '1':
                self.add_product()
            elif choice == '2':
                self.update_product()
            elif choice == '3':
                self.record_transaction()
            elif choice == '4':
                self.view_transactions()
            elif choice == '5':
                self.generate_balance_sheet()
            elif choice == '6':
                print("Exiting the program.")
                break
            else:
                print("Inva
