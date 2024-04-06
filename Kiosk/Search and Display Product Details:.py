import csv
import json
import datetime
import matplotlib.pyplot as plt

class BusinessLogic:
    def __init__(self):
        self.product_list = []  # Load product data from file during initialization
        self.transactions = []  # Load transaction data from file during initialization

    def search_product(self, name):
        for product in self.product_list:
            if product['name'].lower() == name.lower():
                return product
        return None

    def view_profit_loss(self, start_date, end_date):
        start_dt = datetime.datetime.strptime(start_date, '%Y-%m-%d')
        end_dt = datetime.datetime.strptime(end_date, '%Y-%m-%d')
        transactions_in_period = [t for t in self.transactions if start_dt <= t['timestamp'] <= end_dt]
        total_income = sum(t['price'] * t['quantity'] for t in transactions_in_period if t['type'] == 'Sale')
        total_expenses = sum(t['price'] * t['quantity'] for t in transactions_in_period if t['type'] == 'Expense')
        return total_income - total_expenses

    def alert_low_stock(self, threshold):
        low_stock_products = [product for product in self.product_list if product['quantity'] < threshold]
        if low_stock_products:
            print("Alert: The following products are low in stock:")
            for product in low_stock_products:
                print(product['name'])

    def export_reports(self):
        with open('transactions_report.csv', 'w', newline='') as csvfile:
            fieldnames = ['timestamp', 'item', 'quantity', 'price', 'type']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(self.transactions)

        with open('inventory_report.csv', 'w', newline='') as csvfile:
            fieldnames = ['name', 'buying_price', 'selling_price', 'quantity']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(self.product_list)

    def display_graphs(self):
        dates = [t['timestamp'] for t in self.transactions]
        sales = [t['quantity'] * t['price'] for t in self.transactions if t['type'] == 'Sale']
        expenses = [t['quantity'] * t['price'] for t in self.transactions if t['type'] == 'Expense']

        plt.figure(figsize=(10, 5))
        plt.plot(dates, sales, label='Sales')
        plt.plot(dates, expenses, label='Expenses')
        plt.xlabel('Date')
        plt.ylabel('Amount ($)')
        plt.title('Sales and Expenses Over Time')
        plt.legend()
        plt.show()

# Example usage
business_logic = BusinessLogic()

# Assuming product_list and transactions are loaded from files or added programmatically

# Search and display product details
product = business_logic.search_product('Bread')
if product:
    print("Product Found:")
    print(product)
else:
    print("Product not found.")

# View profit/loss for specific period
profit_loss = business_logic.view_profit_loss('2024-01-01', '2024-12-31')
print(f"Profit/Loss for the year: ${profit_loss}")

# Alert for low stock
business_logic.alert_low_stock(10)

# Export reports
business_logic.export_reports()

# Display graphs
business_logic.display_graphs()
