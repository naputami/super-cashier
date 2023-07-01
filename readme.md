# Super Cashier

## Background
The Super Cashier App enables customers to conveniently add items, quantities, and unit prices. 
The app performs automatic calculations of the total price and applicable discounts during the checkout process.
The Supermarket Self-Service Cashier App also provides functionality for inputting the name, unit price, and quantity of the checkouted items into an SQLite3 database, ensuring seamless record-keeping and data management.

## Requirements
To ensure proper functionality, the Super Cashier App requires the following packages/languanges to be installed:  
1. Python 
2. PrettyTable
3. SQLite3

## Program Objective
The objectives of the program are as follows:  
1. Adding items to the cart, including their quantity and unit price.
2. Searching for item names within the cart.
3. Deleting an item or all items from the cart.
4. Updating the name, price, or quantity of items in the cart.
5. Displaying the items currently in the cart.
6. Calculating total payment and discount.
7. Inserting name, quantity, and price of check outed item to SQLite database.


## Code Flow
The program follows a specific flow, as outlined below:
1. Initialization: The program starts by initializing the Transaction class, setting up the necessary components.
2. Menu Options: The customer is presented with a menu containing various options to choose from:
	- Add Item: The customer can add items to the cart by providing the item's name, quantity, and price.
	- Check Order: This option displays the items currently in the cart, allowing the customer to review their selection.
	- Update Item Name: The customer can update the name of an item by specifying the item's current name and the desired new name.
	- Update Item Price: This option enables the customer to update the price of an item by entering the item's name and the new price.
	- Update Item Quantity: The customer can adjust the quantity of an item by entering the item's name and the desired new quantity.
	- Delete Item: If the customer wants to remove an item from the cart, they can select this option and provide the item's name.
	- Reset Transaction: Choosing this option will clear the entire cart.
	- Checkout Item: When the customer is ready to check out, they can select this option. The program will calculate the total price and any applicable discounts. The name, price, and quantity of items being checked out will also be added to an SQLite database.
	- Quit: If the customer wishes to exit the program, they can choose this option.

The flow chart of the program is presented below.
```mermaid
flowchart TD
	A([start]) --> B[input item with add_item]
	B --> C{add more item}
	C --> |yes| B
	C --> |no| D{update item}
	D --> |yes| E[update item name, quantity, or price]
	D --> |no| F{delete an item}
	E --> F
	F --> |yes| G[delete item with delete_item]
	F --> |no| H{reset transaction}
	G --> H
	H --> |yes| I[reset transaction with reset_transaction]
	H --> |no| K{check order}
	I --> K
	K --> |yes| L[check order with check_order]
	K --> |no| C
	L --> M{is the order ok?}
	M --> |yes|N{check out item}
	M --> |no| C
	N --> |yes| O[calculate total price and discount with check_out]
	N --> |no| C
	O --> P[input data to database with insert_to_database]
	P --> Q([finish])
```
## How To Run This Program
To get started with this project, please follow the steps below:
1. Install the required dependencies by ensuring that Python, SQLite3, and PrettyTable are installed on your local computer.
2. Clone this repository to your local machine using your preferred method. This can be done by running the following command in your terminal  
```
git clone https://github.com/naputami/SuperCashier-Pacmann.git
```
3. Once the repository is cloned, navigate to the project's directory in your terminal.
4. To launch the program, run the main.py file using the following command:  
```
python main.py
```
By following these steps, you will be able to install the necessary dependencies, clone the repository, and run the program on your local machine.

## Code Explanation
### import required library
```
from prettytable import PrettyTable
from datetime import datetime
import sqlite3
from sqlite3 import Error
```
### Transaction Class Method
#### constructor
```
def __init__(self):
        """
        Constructor for creating an attribute named cart. 
        The attribute is a dictionary with item name as key and a list as its value.
        The list contains information about quantity, price, and item payment amount.
        """
        self.cart = {}
```
#### search_item(name)
```
def search_name(self, name):
	"""
	A method for ensuring the searched name is available in cart attributes
	Args:
	    name (str)
	return
	    found (boolean)
	"""
	found = False
	for key in self.cart:
	    if key == name:
		found = True
		break
	return found
```
#### show_item()
```
def show_order(self):
	"""
	A method for displaying information about item name, quantity, and payment amount in a table.
	The table is generated by PrettyTable.
	
	Args: -
	Return: -
	"""
	#print date and time
	now = datetime.now()
	formatted_date = now.strftime("%Y-%m-%d %H:%M:%S")
	print(f'Date and Time: {formatted_date}')
	print()
	
	table = PrettyTable()
	table.field_names = ["item name", "quantity", "unit price", "amount"]
	
	for key, value in self.cart.items():
	    row = [key] + value
	    table.add_row(row)
	    
	print(table)
```
#### add_item(name, qty, price)
```
def add_item(self, name, qty, price):
	"""
	A method for adding item name, quantity, and price to cart.
	Item name is key in cart attribute whose value is a list.
	The list contains:
	    - quantity (int) at index 0
	    - price (int) at index 1
	    - total amount (int) at index 2 that obtained from multiplication between quantity and price.
	
	Args:
	    -name(str)
	    -qty(str)
	    -price(str)
	
	return: -
	"""
	
	#ensuring that item name is inputted
	if name == "":
	    print("Item name cannot be empty.")
	else:
	    #error handling for casting quantity and price from string to integer.
	    try:
		int_qty = int(qty)
		int_price = int(price)
	
		#raising exception when qty or price are smaller than 1
		if int_price < 1 or int_qty < 1:
		    raise Exception
		self.cart[name] = [int_qty, int_price, int_price * int_qty]
		print(f'{name} is successfully added to cart.')
	    except:
		print("Price and quantity must be integer and not smaller than 1")
```
#### check_order()
```
def check_order(self):
	"""
	A method for checking order. It will show information about items in cart.
	
	Args: -
	Return: -
	"""
	if len(self.cart) == 0:
	    print("The cart is empty. Please add an item.")
	else:
	    #show item in cart
	    print("Items in cart.")
	    self.show_order()
```
#### update_name(old_name, new_name)
```
def update_name(self, old_name, new_name):
	"""
	A method for updating item name in cart.
	
	Args:
	    -old_name (str)
	    -new_name (str)
	"""
	self.cart[new_name] = self.cart.pop(old_name)
	print(f'{old_name} changed to {new_name}')
```
#### update_price(name, new_price)
```
def update_price(self, name, new_price):
        """
        A method for updating item price in cart.

        Args:
            -name (str)
            -new_price (str)
        Return: -
        """
        #error handling for casting new_price from string to integer
        try:
            int_newprice = int(new_price)

            #raise exception when new price is 0
            if int_newprice < 1:
                raise Exception
            
            self.cart[name][1] = int_newprice
            #updating total amount
            self.cart[name][2] = self.cart[name][0] * self.cart[name][1]
            print(f'{name} price is updated to {new_price}')
        except:
            print("Price must be integer not smaller than 1")
```
#### update_qty(name, new_qty)
```
def update_qty(self, name, new_qty):
        """
        A method for updating item quantity in cart.

        Args:
            -name (str)
            -new_qty (str)
        Return: -
        """
        try:
            #error handling for casting new_qty from string to integer
            int_newqty = int(new_qty)
            
            #raise exception when new quantity is 0
            if int_newqty == 0:
                raise Exception
            self.cart[name][0] = int_newqty

            #updating total amount
            self.cart[name][2] = self.cart[name][0] * self.cart[name][1]
            print(f'{name} quantity is updated to {new_qty}')
        except:
            print("Quantity must be integer and not smaller than 1")
```
#### delete_item(name)
```
def delete_item(self, name):
        """
        A method for deleting an item in cart.

        Args:
            -name (str)
        Return: -
        """
        self.cart.pop(name)
        print(f'{name} is deleted from cart.')
```
#### reset_transaction()
```
def reset_transaction(self):
        """
        A method for clearing all items in cart.

        Args: -
        Return: -
        """
        self.cart.clear()
        print("All items are removed from cart.")
```
#### check_out()
```
def check_out(self):
        """
        A method for: 
            -showing check outed items
            -calculate discount and total payment
                if total payment > 500.0000, user will get 7% discount.
                if total payment > 300.0000, user will get 6% discount.
                if total payment > 200.0000, user will get 5% discount.
            -return check outed item name, quantity, and price data for database processing.

        Args: -
        Return: list of tuples
        """
        if len(self.cart) == 0:
            print("The cart is empty. Please add an item.")
        else:
            print("==========  RECEIPT ==========\n")
            self.show_order()
            subtotal = 0
            disc = 0

        #subtotal calculation
            for item in self.cart:
                subtotal += self.cart[item][2]
            
            #discount and total payment calculation
            if subtotal > 500000:
                disc = 0.07
                total = subtotal - (subtotal * disc)
            elif subtotal > 300000:
                disc = 0.06
                total = subtotal - (subtotal * disc)
            elif subtotal > 200000:
                disc = 0.05
                total = subtotal - (subtotal * disc)
            else:
                total = subtotal
        
            print(f'\nSubtotal: {subtotal}\nDiscount: {disc:.0%}\nTotal: {total:.1f}')
        
            print("Thank you for shopping here!")

            #creating list of tuples for database record
            item_checkout = []
            for key, value in self.cart.items():
                """
                key = item name (str)
                value[0] = quantity (int)
                value[1] = price (int)
                value[2] = amount (int)
                """
                item_checkout.append((key, value[0], value[1], value[2]))
            
            return item_checkout
```
### def insert_to_database(dbfile, data)
```
def insert_to_database(dbfile, data):
    """
    A function for inserting check outed item data to sqlite3 database.
    Args:
        -dbfile (str) : name of database file
        -data (list of tuples) : check outed item data
    Return: - 
    """
    #error handling for inserting record to database
    try:
        connection = sqlite3.connect(dbfile)
        cursor = connection.cursor()

        cursor.execute(''' CREATE TABLE IF NOT EXISTS checkout_items (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    item_name TEXT NOT NULL,
                    quantity INTEGER NOT NULL,
                    unit_price INTEGER NOT NULL,
                    amount INTEGER NOT NULL
                )
        ''')

        cursor.executemany("INSERT INTO checkout_items(item_name, quantity, unit_price, amount) VALUES (?,?,?,?)", data)
        print("Check outed item is succesfully added to database!")
        
        connection.commit()
        connection.close()
    except Error as e:
        print(e)
```
### main.py
```
from transaction import Transaction
from db_helper import insert_to_database

#transaction class initialization
trnsct_123 = Transaction()

#Looping for displaying and running the menu
while True:
    print("")
    print("=" * 30)
    print("Welcome to SuperCashier")
    print("=" * 30)
    print('''
    Please select the menu.
    1. Add item to cart
    2. Check order
    3. Update item name in cart
    4. Update item price in cart
    5. Update item quantity in cart
    6. Delete an item in cart
    7. Reset Transaction.
    8. Check out order
    9. Quit program
    ''')

    user_input = input("chosen menu: ")
    if user_input == "1":
        item_name = input("item name: ").title()
        item_price = input("item price: ")
        item_qty = input("item quantity: ")
        trnsct_123.add_item(item_name, item_qty, item_price)

    elif user_input == "2":
        trnsct_123.check_order()

    elif user_input in ["3", "4", "5"]:
        item_name_update = input("item name to be updated: ").title()
        if trnsct_123.search_name(item_name_update): 
            if user_input == "3":
                new_name = input("new name: ").title()
                trnsct_123.update_name(item_name_update, new_name)
            elif user_input == "4":
                new_price = input("new price: ")
                trnsct_123.update_price(item_name_update, new_price)
            else:
                new_qty = input("new quantity: ")
                trnsct_123.update_qty(item_name_update, new_qty)
        else:
            print(f'{item_name_update} is not found in cart.')

    elif user_input == "6":
        item_name_delete = input("item name to be deleted: ").title()
        if trnsct_123.search_name(item_name_delete):
            trnsct_123.delete_item(item_name_delete)
        else:
            print(f'{item_name_delete} is not found in cart.')

    elif user_input == "7":
        trnsct_123.reset_transaction()

    elif user_input == "8":
        checkout_data = trnsct_123.check_out()
        #insert check outed item data to database
        insert_to_database("checkout.db", checkout_data)
        break
        
    elif user_input == "9":
        print("Thank you for using this program")
        print("Closing the program ...")
        break
    
    else:
        print("Selected menu is not available. Please reinput available menu.")
```
## Test Case
1. Customer wants to add two items using add_item() method. The items will be added as follow:  
- item name: Ayam goreng, qty: 2, unit price: 20000
- item name: Pasta gigi, qty: 3, unit price: 150000  
Output:  
![test case 1](img/test_case_1.jpg)

2. Customer wants to delete Pasta gigi from the cart using delete_item() method.  
Output:  
![test case 2](img/test_case_2.jpg)

3. Customer wants to delete all items in the cart using reset_transaction() method.  
Output:  
![test case 3](img/test_case_3.jpg)

4. After finishing shopping, the program will calculate total payment and discount.  
Output:  
![test case 4](img/test_case_4.jpg)
## Conclusion
The program successfully achieves its intended objectives and runs as expected. Nevertheless, there are areas identified for improvement:  
1. Database Enhancement: Enhance the database to allow for more detailed storage of customer and transaction data.
2. User Interface Refinement: Address the user interface to ensure a more user-friendly and simplified application experience.
