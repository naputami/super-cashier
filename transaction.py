from prettytable import PrettyTable
from helpers import *
import sqlite3


class Transaction:
    def __init__(self):
        """
        Constructor for creating an attribute named cart. 
        The attribute is a list of dictionaries which contains information about item name, price, quantity, and amount
        """
        self.cart = []
    
    def insert_to_table(self, dbfile):
        """
        A function for inserting check outed item data to sqlite3 database.
        Args:
            -dbfile (str) : name of database file
        Return: - 
        """
        #create list of tuples of dictionaries' values in cart
        data =[tuple(item.values()) for item in self.cart]

        #error handling for inserting record to database
        try:
            connection = sqlite3.connect(dbfile)
            cursor = connection.cursor()

            cursor.execute(''' CREATE TABLE IF NOT EXISTS transactions (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        item_name VARCHAR(50) NOT NULL,
                        quantity INTEGER NOT NULL,
                        unit_price INTEGER NOT NULL,
                        amount INTEGER NOT NULL,
                        discount INTEGER NOT NULL,
                        new_amount INTEGER NOT NULL
                    )
            ''')

            cursor.executemany("INSERT INTO transactions(item_name, unit_price, quantity, amount, discount, new_amount) VALUES (?,?,?,?,?,?)", data)
            print("Check outed item is succesfully added to database!")
            
            connection.commit()
            connection.close()
        except sqlite3.Error as e:
            print(e)
    

    def add_item(self, name, qty, price):
        """
        A method for adding item name, quantity, and price to cart.
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
            #create dictionary for new item
            new_item = {}
            new_item["name"] = name.title()
            
            #error handling for casting quantity and price from string to integer.
            try:
                int_price = int(price)
                int_qty = int(qty)

                #raise exception if price or quantity smaller than 0
                if int_price < 1 or int_qty < 1:
                    raise Exception
                
                new_item["price"] = int(price)
                new_item["quantity"] = int(qty)
                new_item["amount"] = int(price) * int(qty)
                self.cart.append(new_item)
                print(f'{name.title()} is sucessfully added to cart!')
            except:
                print("\nprice and quantity must be integer and not smaller than 0!\n")

    def check_order(self):
        """
        A method for checking order. It will show information about items in cart.

        Args: -
        Return: -
        """
        show_date_time()
        table = PrettyTable()
        table.field_names = self.cart[0].keys()
        for item in self.cart:
            table.add_row([item["name"], change_currency(item["price"]), item["quantity"], change_currency(item["amount"])])
        print(table)
            
    
    def update_item_name(self, old_name, new_name):
        """
        A method for updating item name in cart.

        Args:
            -old_name (str)
            -new_name (str)
        """
        item_index = find_index(self.cart, old_name)
        if item_index != -1:
            self.cart[item_index]["name"] = new_name.title()
            print(f'{old_name.title()} changed to {new_name.title()}')
        else:
            print(f'Can\'t found {old_name.title()} in cart. Please input another item name')
        

    def update_item_price(self, name, new_price):
        """
        A method for updating item price in cart.

        Args:
            -name (str)
            -new_price (str)
        Return: -
        """
        item_index = find_index(self.cart, name)
        if item_index != -1:
            try:
                #error handling for casting new_price from string to integer
                int_new_price = int(new_price)

                #raise ecveption if new_price is smaller than 0
                if int_new_price < 0:
                    raise Exception
                
                self.cart[item_index]["price"] = int_new_price
                self.cart[item_index]["amount"] = int_new_price * self.cart[item_index]["quantity"]
                print(f'{name.title()} price changed to {new_price}')
            except:
                print("Price must be integer and not smaller than 0!")
        else:
            print(f'Can\'t found {name.title()} in cart. Please input another item name')

    def update_item_qty(self, name, new_qty):
        """
        A method for updating item quantity in cart.

        Args:
            -name (str)
            -new_qty (str)
        Return: -
        """
        item_index = find_index(self.cart, name)
        if item_index != -1:
            try:
                #error handling for casting new_qty from string to integer
                int_new_qty = int(new_qty)
                
                #raise exception if new_qty is smaller than 0
                if int_new_qty < 0:
                    raise Exception
                
                self.cart[item_index]["quantity"] = int_new_qty
                self.cart[item_index]["amount"] = int_new_qty * self.cart[item_index]["price"]
                print(f'{name.title()} quantity changed to {new_qty}')
            except:
                print("Quantity must be integer and not smaller than 0!")
        else:
            print(f'Can\'t found {name.title()} in cart. Please input another item name')


    def delete_item(self, name):
        """
        A method for deleting an item in cart.

        Args:
            -name (str)
        Return: -
        """
        item_index = find_index(self.cart, name)

        if item_index != -1:
            del self.cart[item_index]
            print(f'{name.title()} is sucessfully removed from cart.')
        else:
            print(f'Can\'t found {name.title()} in cart. Please input another item name')
       

    def reset_transaction(self):
        """
        A method for clearing all items in cart.

        Args: -
        Return: -
        """
        self.cart.clear()
        print("All items are sucessfully removed from cart!")


    def check_out(self):
        """
        A method for: 
            -showing check outed items
            -calculate discount and total payment
                if item amount > 500.0000, user will get 7% discount.
                if item amount > 300.0000, user will get 6% discount.
                if item amount > 200.0000, user will get 5% discount.

        Args: -
        Return: -
        """
        for item in self.cart:
            if item["amount"] > 500_000:
                item.update(disc_calculation(0.07, item["amount"]))
            elif item["amount"] > 300_000:
                item.update(disc_calculation(0.06, item["amount"]))
            elif item["amount"] > 200_000:
                item.update(disc_calculation(0.05, item["amount"]))
            else:
                item.update(disc_calculation(0, item["amount"]))

        total_payment = 0 
        table = PrettyTable()
        table.field_names = self.cart[0].keys()
        for item in self.cart:
            total_payment += item["amount after discount"]
            table.add_row([item["name"], change_currency(item["price"]), item["quantity"], change_currency(item["amount"]), change_currency(item["discount"]), change_currency(item["amount after discount"])])
        
        print("="*35 , " RECEIPT ", "="*35)
        print()
        show_date_time()
        print(table)
        print(f'Total payment: {change_currency(total_payment)}')
        print("Thank you for shopping here")