from transaction import Transaction

print("")
print("=" * 30)
print("Welcome to SuperCashier")
print("=" * 30)

customer_id = input("Enter your customer id here: ")
print(f'Your customer id: {customer_id}')
trnsct_123 = Transaction()

while True:
    print('''
    Please select the menu.
    1. Add item to cart
    2. Check order
    3. Update item in cart
    4. Delete an item in cart
    5. Reset Transaction.
    6. Check out order
    ''')

    user_input = input("chosen menu: ")
    if user_input == "1":
            item_name = input("Input item name: ")
            item_price = input("Input item price: ")
            item_qty = input("Input item quantity: ")
            trnsct_123.add_item(item_name, item_qty, item_price)

    elif user_input == "2":
        if len(trnsct_123.cart) == 0:
            print("The cart is empty. Please add an item.")
        else: 
            trnsct_123.check_order()

    elif user_input == "3":
        print(''' 
                \nWhat will you update?\n1. item name\n2. item price\n3. item quantity
                ''')
        user_input_update = input("Input choice: ")
        if user_input_update == "1":
            item_to_update = input("Please input the name of the item that will be updated: ")
            new_name = input("Input new name: ")
            trnsct_123.update_item_name(item_to_update, new_name)
        elif user_input_update == "2":
            item_to_update = input("Please input the name of the item that will be updated: ")
            new_price = input("Input new price: ")
            trnsct_123.update_item_price(item_to_update, new_price)
        elif user_input_update == "3":
            item_to_update = input("Please input the name of the item that will be updated: ")
            new_qty = input("Input new quantity: ")
            trnsct_123.update_item_qty(item_to_update, new_qty)
        else:
            print("The selected option is not available! Please select an option from the menu.")

    elif user_input == "4":
        item_to_delete =  input("Please input the name of the item that will be deleted: ")
        trnsct_123.delete_item(item_to_delete)

    elif user_input == "5":
        print("Are you sure to remove all items from cart?")
        print("1. yes")
        print("2. no")
        user_confirm = input("type your answer here: ")
        if user_confirm == "1":
            trnsct_123.reset_transaction()
        elif user_confirm == "2":
            continue
        else:
            print("Please select a valid option!")
    elif user_input == "6":
        if len(trnsct_123.cart) == 0:
            print("The cart is empty. Please add an item.")
        else:
            trnsct_123.check_out()
            trnsct_123.insert_to_table("checkout.db")
            break
    else:
        print("Selected menu is not available. Please reinput available menu.")