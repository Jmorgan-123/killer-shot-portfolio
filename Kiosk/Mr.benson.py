import datetime
import json
from tabulate import tabulate

# Function to load existing data from the file
def load_data():
    try:
        with open("products.txt", "r") as file:
            data = json.load(file)
        return data if isinstance(data, list) else []
    except FileNotFoundError:
        return []

# Function to load existing transactions from the file
def load_transactions():
    try:
        with open("transactions.txt", "r") as file:
            transactions = json.load(file)
        return transactions if isinstance(transactions, list) else []
    except FileNotFoundError:
        return []

# Function to save data to the file
def save_data(data, filename):
    with open(filename, "w") as file:
        json.dump(data, file, indent=2)

# Load existing data
product_list = load_data()
transactions = load_transactions()



# Create a product function
def products():

    action = input("Do you want to add a product? Y/N: ").lower()
    if action == "y":
        name_of_product = input("Enter name of product: ")
        buying_price = int(input("Enter the buying price: "))
        selling_price = int(input("Enter the selling price: "))
        quantity_of_products = int(input("How many do you have?: "))
        total_price = quantity_of_products * buying_price
        description_of_product = input("Enter description of product: ")
        exp_date = input("Enter expiry date for product yyyy-mm-dd: ").split("-")
        year, month, day = (int(item) for item in exp_date)
        d = datetime.datetime(year, month, day)
        product_list.append(
            {
                'name': name_of_product, 
                'buying_price': buying_price,
                'selling_price': selling_price,
                'quantity_of_products': quantity_of_products,
                'total_price' : total_price,
                'description_of_product': description_of_product,
                'exp_date': d.strftime('%a %B %d, %Y'),
            }
        )
    else:
        print("Something is wrong")

    # Save the updated data to the file
    save_data(product_list, 'products.txt')

    total_prices = [product['total_price'] for product in product_list]
    total_investment = sum(total_prices)
    
    table = tabulate(product_list, headers='keys', tablefmt='pretty')
    print(table)
    print(f"Total Investment {total_investment}")

    return f"Total investment {total_investment}"



# Function to update details of a product
def update_product(product_list, product_name):
    for product in product_list:
        if product['name'].lower() == product_name.lower():
            print(f"Current details of {product_name}:")
            print(tabulate([product], headers='keys', tablefmt='pretty'))

            # Prompt user for the fields to update
            fields_to_update = ['buying_price', 'selling_price', 'quantity_of_products',
                                'description_of_product', 'exp_date']

            for field in fields_to_update:
                user_input = input(f"Enter the new {field.replace('_', ' ')} (press Enter to keep current value): ")
                if user_input:
                    if field == 'exp_date':
                        year, month, day = (int(item) for item in user_input.split('-'))
                        d = datetime.datetime(year, month, day)
                        product[field] = d.strftime('%a %B %d, %Y')
                    else:
                        product[field] = int(user_input) if user_input.isnumeric() else user_input

            # Update quantity and recalculate total price
            new_quantity = product.get('quantity_of_products', 0)
            new_buying_price = product.get('buying_price', 0)
            product['total_price'] = new_quantity * new_buying_price

            print(f"\nDetails of {product_name} updated successfully.")
            print(tabulate([product], headers='keys', tablefmt='pretty'))

            # Save the updated data to the file
            save_data(product_list, 'products.txt')
            return

    print(f"Product with name {product_name} not found.")



# Function to view details of a product
def view_product(product_list, product_name):
    for product in product_list:
        if product['name'].lower() == product_name.lower():
            print(f"Details of {product_name}:")
            print(tabulate([product], headers='keys', tablefmt='pretty'))
            return

    print(f"Product with name {product_name} not found.")
    
# Function to view all products
def view_all_products(product_list):
    table = tabulate(product_list, headers='keys', tablefmt='pretty')
    print(table)


# Function to remove a product
def remove_product(product_list, product_name):
    for i, product in enumerate(product_list):
        if product['name'].lower() == product_name.lower():
            print(f"Details of {product_name} to be removed:")
            print(tabulate([product], headers='keys', tablefmt='pretty'))

            # Confirm with the user before removal
            confirm = input("Are you sure you want to remove this product? (yes/no): ").lower()
            if confirm == 'yes':
                del product_list[i]
                print(f"\n{product_name} removed successfully.")
                # Save the updated data to the file
                save_data(product_list, 'products.txt')
            else:
                print(f"\n{product_name} was not removed.")
            return

    print(f"Product with name {product_name} not found.")


# Function to sell a product
def sell_product(product_list, transactions, product_name):
    for product in product_list:
        if product['name'].lower() == product_name.lower():
            print(f"Current details of {product_name}:")
            print(tabulate([product], headers='keys', tablefmt='pretty'))

            # Prompt user for the quantity to sell
            quantity_to_sell = int(input(f"How many {product_name}s do you want to sell? "))
            if quantity_to_sell > product['quantity_of_products']:
                print("Error: Not enough quantity available for sale.")
                return

            # Update quantity and recalculate total price
            product['quantity_of_products'] -= quantity_to_sell
            product['total_price'] = product['quantity_of_products'] * product['buying_price']

            # Add transaction record
            transaction = {
                'product_name': product_name,
                'quantity_sold': quantity_to_sell,
                'selling_price': product['selling_price'],
                'total_sale': quantity_to_sell * product['selling_price'],
                'timestamp': datetime.datetime.now().strftime('%a %B %d, %Y %H:%M:%S'),
            }
            transactions.append(transaction)

            print(f"\n{quantity_to_sell} {product_name}s sold successfully.")
            print(f"Updated details of {product_name}:")
            print(tabulate([product], headers='keys', tablefmt='pretty'))

            # Save the updated data to the file
            save_data(product_list, "products.txt")
            save_data(transactions, "transactions.txt")
            return

    print(f"Product with name {product_name} not found.")

# Function to view all transactions
def view_transactions(transactions):
    if not transactions:
        print("No transactions available.")
        return

    table = tabulate(transactions, headers='keys', tablefmt='pretty')
    print("All Transactions:")
    print(table)

# Function to create a balance sheet
def balance_sheet(product_list, transactions):
    total_inventory_value = sum([product['total_price'] for product in product_list])
    total_sales = sum([transaction['total_sale'] for transaction in transactions])
    total_profit = total_sales - total_inventory_value

    print("\nBalance Sheet:")
    print(f"Total Inventory Value: KES{total_inventory_value}")
    print(f"Total Sales: KES{total_sales}")
    print(f"Total Profit: KES{total_profit}")

def call_functions():
    
    while True:
        print("Action Choice:")
        print("1: Add Product")
        print("2: Update Product")
        print("3: View Specific Product")
        print("4: View All Products")
        print("5: Delete a product")
        print("6: Sell a product")
        print("7: View Transactions")
        print("8: Generate a balance sheet")
        action = int(input("Choose an action with number: \n"))

        if action == 1:
            products()
            print(products())
        elif action == 2:
            product_name = input("Enter product name you want to update: ")
            update_product(product_list, product_name)
        elif action == 3:
            product_name = input("Enter product name you want to view details of the product: ")
            view_product(product_list, product_name)
        elif action == 4:
            view_all_products(product_list)
        elif action == 5:
            product_name = input("Enter product name you want to delete: ")
            remove_product(product_list, product_name)
        elif action == 6:
            product_name = input("What product would you like to sell: ")
            sell_product(product_list, transactions,product_name)
        elif action == 7:
            view_transactions(transactions)
        elif action == 8:
            balance_sheet(product_list, transactions)
        else:
            break


call_functions()
