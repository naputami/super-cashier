from prettytable import PrettyTable

class Transaction:
    def __init__(self):
        self.cart = {}
    
    def search_name(self, name):
        found = False
        for key in self.cart:
            if key == name:
                found = True
                break
        return found

    def add_item(self, name, qty, price):
        if name == "":
            print("Item name cannot be empty.")
        else:
            try:
                self.cart[name] = [int(qty), int(price), int(qty)*int(price)]
                print(f'{name} is added to cart.')
            except:
                print("Price and quantity must be integer")

    def check_order(self):
        if len(self.cart) == 0:
            print("The cart is empty. Please add an item.")
        else:
            table = PrettyTable()
            table.field_names = ["item name", "quantity", "unit price", "amount"]

            for key, value in self.cart.items():
                row = [key] + value
                table.add_row(row)
            
            print(table)
    
    def update_name(self, old_name, new_name):
        self.cart[new_name] = self.cart.pop(old_name)
        print(f'{old_name} changed to {new_name}')
        

    def update_price(self, name, new_price):
        try:
            self.cart[name][1] = int(new_price)
            self.cart[name][2] = self.cart[name][0] * self.cart[name][1]
            print(f'{name} price is updated to {new_price}')
        except:
            print("Price must be integer")

    def update_qty(self, name, new_qty):
        try:
            self.cart[name][0] = int(new_qty)
            self.cart[name][2] = self.cart[name][0] * self.cart[name][1]
            print(f'{name} quantity is updated to {new_qty}')
        except:
            print("Quantity must be integer")


    def delete_item(self, name):
        self.cart.pop(name)
        print(f'{name} is deleted from cart.')
       

    def reset_transaction(self):
        self.cart.clear()
        print("All items have been removed from cart.")

    def check_out(self):
        if len(self.cart) == 0:
            print("The cart is empty. Please add an item.")
        else:
            subtotal = 0
            disc = 0

            for item in self.cart:
                subtotal += self.cart[item][2]
            
            if subtotal >= 500000:
                disc = 0.07
                total = subtotal - (subtotal * disc)
            elif subtotal >= 300000:
                disc = 0.06
                total = subtotal - (subtotal * disc)
            elif subtotal >= 200000:
                disc = 0.05
                total = subtotal - (subtotal * disc)
            else:
                total = subtotal

            
            print(f'Subtotal: {subtotal}\nDiscount: {disc:.0%}\nTotal: {total:.2f}')
            print("Thank you for shopping here!")
