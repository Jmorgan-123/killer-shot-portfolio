import csv
import os
import datetime
import json
from tabulate import tabulate

# Function to load existing data from the file
def load_data(filename):
    try:
        with open(filename, "r") as file:
            data = json.load(file)
        return data if isinstance(data, list) else []
    except FileNotFoundError:
        return []

# Function to save data to the file
def save_data(data, filename):
    with open(filename, "w") as file:
        json.dump(data, file, indent=2)

# Load existing data
product_list = load_data('products.txt')
transactions = load_data('transactions.txt')

class BensonKiosk:
    def __init__(self):
        self.transactions = []

    def record_transaction(self, item, quantity, price, transaction_type):
        timestamp = datetime.datetime.now().strftime('%a %B %d, %Y %H:%M:%S')
        transaction = {
            'timestamp': timestamp,
            'item': item,
            'quantity': quantity,
            'price': price,
            'type': transaction_type
        }
        self.transactions.append(transaction)

    def export_to_csv(self, filename='transactions.csv'):
        with open(filename, 'w', newline='') as csvfile:
            fieldnames = ['timestamp', 'item', 'quantity', 'price', 'type']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()

            for transaction in self.transactions:
                writer.writerow(transaction)

    def calculate_profit_loss(self):
        total_income = sum(transaction['price'] for transaction in self.transactions if transaction['type'] == 'Sale')
        total_expenses = sum(transaction['price'] for transaction in self.transactions if transaction['type'] == 'Expense')
        profit_loss = total_income - total_expenses
        return profit_loss

# Create an instance of BensonKiosk
manager = BensonKiosk()

def call_functions():
    while True:
        print("\nBusiness Management System\n")
        print("1: Record Sale")
        print("2: Record Expense")
        print("3: Export Transactions to CSV")
        print("4: Calculate Profit/Loss")
        print("5: Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            item = input("Enter the item sold: ")
            quantity = int(input("Enter the quantity sold: "))
            price = float(input("Enter the price per unit: "))
            manager.record_transaction(item, quantity, price, 'Sale')

        elif choice == '2':
            item = input("Enter the expense item: ")
            quantity = int(input("Enter the quantity purchased: "))
            price = float(input("Enter the price per unit: "))
            manager.record_transaction(item, quantity, price, 'Expense')

        elif choice == '3':
            filename = input("Enter the filename to export to (default is transactions.csv): ")
            manager.export_to_csv(filename)

        elif choice == '4':
            result = manager.calculate_profit_loss()
            print(f"Profit/Loss: ${result}")

        elif choice == '5':
            print("Exiting the program.")
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

    # Save updated transactions data to the file
    save_data(manager.transactions, 'transactions.txt')

if __name__ == "__main__":
    call_functions()
